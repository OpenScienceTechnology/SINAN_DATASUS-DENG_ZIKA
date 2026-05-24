"""
============================================================
  DATASUS SINAN — Pipeline de Download e Conversão DBC → CSV / CSV.GZ
  Dengue · Zika Vírus
============================================================
  Descrição:
    Este script automatiza o processo de obtenção dos microdados de Dengue e
    Zika do SINAN-DATASUS, realizando as seguintes etapas para cada arquivo
    .dbc listado:
      1. Download do arquivo .dbc do servidor FTP do DATASUS.
      2. Descompressão do .dbc para .dbf usando a biblioteca datasus-dbc.
      3. Conversão do .dbf para:
         - CSV plano (utf-8-sig, compatível com Excel) → salvo em csv_archive/
         - CSV comprimido (.csv.gz) → salvo em gz_archive/ (ideal para ML / Big Data)
    O script também gera relatórios detalhados de execução, incluindo:
      - Status de cada arquivo (OK, PULADO, ERRO)
      - Número de registros e colunas processados
      - Tamanho dos arquivos em cada etapa
      - Tempo gasto por arquivo e tempo total
      - Demonstração de como ler os arquivos gerados em Python (pandas)
============================================================
  Dados de interesse: Arquivos de Microdados · DATASUS
  Fonte     : https://alpaca.quantilica.com/dados
  Dengue    : https://alpaca.quantilica.com/dados/sinan-deng
  Zika Vírus: https://alpaca.quantilica.com/dados/sinan-zika
============================================================
  Estrutura de pastas gerada (na pasta de execução do script):

    Source/
    ├── Dengue/
    │   ├── dbc_archive/              ← .dbc originais (Dengue)
    │   ├── csv_archive/              ← .csv planos    (Dengue)
    │   ├── gz_archive/               ← .csv.gz        (Dengue)
    │   └── log_datasus_sinan_dengue.txt
    ├── Zika/
    │   ├── dbc_archive/              ← .dbc originais (Zika)
    │   ├── csv_archive/              ← .csv planos    (Zika)
    │   ├── gz_archive/               ← .csv.gz        (Zika)
    │   └── log_datasus_sinan_zika.txt
    └── log_datasus_sinan_dengue_zika.txt   ← relatório consolidado

============================================================
  Dependências:
    pip install dbfread pandas datasus-dbc texttable tqdm
============================================================
"""

import os
import sys
import time
import gzip
import csv
import shutil
import urllib.request
import datetime
import traceback

from dbfread import DBF
import pandas as pd
from datasus_dbc import decompress
from texttable import Texttable
from tqdm import tqdm

# ─────────────────────────────────────────────────────────────
#  CONFIGURAÇÕES GLOBAIS
# ─────────────────────────────────────────────────────────────

# Pasta base = pasta onde o script está localizado
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, "Source")

MAX_TENTATIVAS  = 3
PAUSA_RETRY_SEG = 5
ENCODING_DBF    = "iso-8859-1"   # padrão DATASUS
ENCODING_CSV    = "utf-8-sig"    # BOM → compatível com Excel
CHUNK_SIZE      = 262144         # 256 KB — streaming GZ com boa performance

# ─────────────────────────────────────────────────────────────
#  URLs — DENGUE
# ─────────────────────────────────────────────────────────────
DENGUE_URLS = [
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR15.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR16.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR17.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR18.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR19.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR20.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR21.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR22.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR23.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR24.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/PRELIM/DENGBR25.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/PRELIM/DENGBR26.dbc",
]

# ─────────────────────────────────────────────────────────────
#  URLs — ZIKA
# ─────────────────────────────────────────────────────────────
ZIKA_URLS = [
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR16.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR17.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR18.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR19.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR20.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR21.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR22.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR23.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR24.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/PRELIM/ZIKABR25.dbc",
    "ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/PRELIM/ZIKABR26.dbc",
]

# ─────────────────────────────────────────────────────────────
#  MAPA DE DATASETS
#  Cada entry define nome, URLs, pasta-raiz e arquivo de log
# ─────────────────────────────────────────────────────────────
DATASETS = [
    {
        "nome":     "Dengue",
        "sigla":    "DENG",
        "urls":     DENGUE_URLS,
        "dir":      os.path.join(SOURCE_DIR, "Dengue"),
        "log_nome": "log_datasus_sinan_dengue.txt",
    },
    {
        "nome":     "Zika",
        "sigla":    "ZIKA",
        "urls":     ZIKA_URLS,
        "dir":      os.path.join(SOURCE_DIR, "Zika"),
        "log_nome": "log_datasus_sinan_zika.txt",
    },
]

# Log consolidado (Dengue + Zika juntos)
LOG_CONSOLIDADO = os.path.join(SOURCE_DIR, "log_datasus_sinan_dengue_zika.txt")


# ═════════════════════════════════════════════════════════════
#  UTILITÁRIOS GERAIS
# ═════════════════════════════════════════════════════════════

def tamanho_humano(bytes_: int) -> str:
    """Converte bytes para string legível (B / KB / MB / GB)."""
    if bytes_ == 0:
        return "0 B"
    for unidade in ["B", "KB", "MB", "GB"]:
        if bytes_ < 1024:
            return f"{bytes_:.1f} {unidade}"
        bytes_ /= 1024
    return f"{bytes_:.1f} TB"


def cabecalho(texto: str, largura: int = 68) -> str:
    """Linha decorativa para separar seções no log."""
    linha = "═" * largura
    return f"\n{linha}\n  {texto}\n{linha}"


def subcabecalho(texto: str, largura: int = 60) -> str:
    linha = "─" * largura
    return f"\n{linha}\n  {texto}\n{linha}"


def log(msg: str, *arquivos) -> None:
    """Imprime no terminal e grava em um ou mais arquivos de log."""
    print(msg)
    for arq in arquivos:
        if arq:
            arq.write(msg + "\n")
            arq.flush()


# ═════════════════════════════════════════════════════════════
#  TEXTTABLE — HELPERS PARA TABELAS FORMATADAS
# ═════════════════════════════════════════════════════════════

def tabela_resultados(resultados: list, titulo: str = "") -> str:
    """
    Gera uma tabela Texttable com o resumo dos arquivos processados.
    Colunas: Nº | Arquivo | Status | Registros | Colunas | DBC | CSV | GZ | Red% | Tempo
    """
    t = Texttable(max_width=110)
    t.set_deco(Texttable.HEADER | Texttable.BORDER | Texttable.VLINES)
    t.set_cols_align(["r", "l", "c", "r", "r", "r", "r", "r", "r", "r"])
    t.set_cols_valign(["m"] * 10)
    t.set_cols_dtype(["t"] * 10)
    t.set_cols_width([3, 12, 14, 11, 7, 9, 9, 9, 6, 7])

    t.header(["Nº", "Arquivo", "Status", "Registros", "Cols",
               "DBC", "CSV", "GZ", "Red%", "Tempo"])

    for r in resultados:
        t.add_row([
            str(r["idx"]),
            r["nome_base"],
            r["status"],
            f"{r['registros']:,}" if r["registros"] else "-",
            str(r["colunas"])    if r["colunas"]    else "-",
            tamanho_humano(r["tam_dbc"]) if r["tam_dbc"] else "-",
            tamanho_humano(r["tam_csv"]) if r["tam_csv"] else "-",
            tamanho_humano(r["tam_gz"])  if r["tam_gz"]  else "-",
            f"{r['razao_gz']:.1f}%"      if r["razao_gz"] else "-",
            f"{r['duracao_s']:.1f}s",
        ])

    cabec = f"\n  {titulo}\n" if titulo else ""
    return cabec + t.draw()


def tabela_totais(resultados: list, duracao_total: float) -> str:
    """
    Gera uma tabela Texttable com os totais/sumário da execução.
    """
    ok_lista = [r for r in resultados if r["status"] == "OK"]
    pulados  = [r for r in resultados if r["status"] == "PULADO"]
    erros    = [r for r in resultados if r["status"].startswith("ERRO")]

    total_reg = sum(r["registros"] for r in ok_lista)
    total_dbc = sum(r["tam_dbc"]   for r in resultados if r["tam_dbc"])
    total_csv = sum(r["tam_csv"]   for r in resultados if r["tam_csv"])
    total_gz  = sum(r["tam_gz"]    for r in resultados if r["tam_gz"])

    t = Texttable(max_width=55)
    t.set_deco(Texttable.HEADER | Texttable.BORDER | Texttable.VLINES)
    t.set_cols_align(["l", "r"])
    t.set_cols_dtype(["t", "t"])
    t.set_cols_width([28, 20])
    t.header(["Métrica", "Valor"])

    t.add_row(["Arquivos processados (OK)",   str(len(ok_lista))])
    t.add_row(["Arquivos pulados",            str(len(pulados))])
    t.add_row(["Arquivos com erro",           str(len(erros))])
    t.add_row(["Total de registros",          f"{total_reg:,}"])
    t.add_row(["Espaço dbc_archive/",         tamanho_humano(total_dbc)])
    t.add_row(["Espaço csv_archive/",         tamanho_humano(total_csv)])
    t.add_row(["Espaço gz_archive/",          tamanho_humano(total_gz)])
    t.add_row(["Tempo total",                 f"{duracao_total:.1f}s ({duracao_total/60:.1f} min)"])
    t.add_row(["Fim da execução",             datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])

    return t.draw()


def tabela_erros(resultados: list) -> str:
    """Gera tabela Texttable apenas com os arquivos que falharam."""
    erros = [r for r in resultados if r["status"].startswith("ERRO")]
    if not erros:
        return "  Nenhum erro registrado."

    t = Texttable(max_width=100)
    t.set_deco(Texttable.HEADER | Texttable.BORDER | Texttable.VLINES)
    t.set_cols_align(["r", "l", "l", "l"])
    t.set_cols_dtype(["t", "t", "t", "t"])
    t.set_cols_width([3, 12, 16, 55])
    t.header(["Nº", "Arquivo", "Status", "Descrição do Erro"])

    for r in erros:
        t.add_row([str(r["idx"]), r["nome_base"], r["status"], r["erro"] or "-"])

    return t.draw()


def tabela_consolidada(resumo_datasets: list) -> str:
    """
    Gera tabela Texttable com comparativo Dengue × Zika.
    resumo_datasets = lista de dicts com chaves: nome, ok, pulados, erros,
                      registros, dbc, csv, gz, duracao
    """
    t = Texttable(max_width=90)
    t.set_deco(Texttable.HEADER | Texttable.BORDER | Texttable.VLINES)
    t.set_cols_align(["l", "r", "r", "r", "r", "r", "r", "r", "r"])
    t.set_cols_dtype(["t"] * 9)
    t.set_cols_width([8, 5, 7, 5, 13, 10, 10, 10, 12])
    t.header(["Dataset", "OK", "Pulados", "Erros",
               "Registros", "DBC total", "CSV total", "GZ total", "Tempo (min)"])

    for ds in resumo_datasets:
        t.add_row([
            ds["nome"],
            str(ds["ok"]),
            str(ds["pulados"]),
            str(ds["erros"]),
            f"{ds['registros']:,}",
            tamanho_humano(ds["dbc"]),
            tamanho_humano(ds["csv"]),
            tamanho_humano(ds["gz"]),
            f"{ds['duracao']/60:.1f}",
        ])

    return t.draw()


# ═════════════════════════════════════════════════════════════
#  GERENCIAMENTO DE PASTAS
# ═════════════════════════════════════════════════════════════

def criar_estrutura_pastas(dataset_dir: str, nome_dataset: str) -> tuple:
    """
    Cria a hierarquia de subpastas para um dataset.
    Retorna (dbc_dir, csv_dir, gz_dir).
    """
    dbc_dir = os.path.join(dataset_dir, "dbc_archive")
    csv_dir = os.path.join(dataset_dir, "csv_archive")
    gz_dir  = os.path.join(dataset_dir, "gz_archive")

    for pasta in (SOURCE_DIR, dataset_dir, dbc_dir, csv_dir, gz_dir):
        os.makedirs(pasta, exist_ok=True)

    print(f"  📁 Source/{nome_dataset}/dbc_archive : {dbc_dir}")
    print(f"  📁 Source/{nome_dataset}/csv_archive : {csv_dir}")
    print(f"  📁 Source/{nome_dataset}/gz_archive  : {gz_dir}")

    return dbc_dir, csv_dir, gz_dir


# ═════════════════════════════════════════════════════════════
#  ETAPAS DO PIPELINE
# ═════════════════════════════════════════════════════════════

def baixar_dbc(url: str, destino: str, *loggers) -> bool:
    """
    Download do .dbc com retry automático e barra de progresso tqdm.
    Retorna True em sucesso, False em falha definitiva.
    """
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        try:
            log(f"  ↓ Download (tentativa {tentativa}/{MAX_TENTATIVAS}): {url}", *loggers)

            pbar = tqdm(
                unit="B", unit_scale=True, unit_divisor=1024,
                desc="    ↓ DBC ", ncols=72, miniters=1,
                bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            )

            def reporthook(bloco_num: int, tam_bloco: int, tam_total: int) -> None:
                if pbar.total is None and tam_total > 0:
                    pbar.total = tam_total
                pbar.update(tam_bloco)

            urllib.request.urlretrieve(url, destino, reporthook=reporthook)
            pbar.close()

            tamanho = os.path.getsize(destino)
            if tamanho < 200:
                raise ValueError(f"Arquivo suspeito — apenas {tamanho} bytes.")

            log(f"  ✔ Download OK  [{tamanho_humano(tamanho)}]", *loggers)
            return True

        except Exception as exc:
            try:
                pbar.close()
            except Exception:
                pass
            log(f"  ✘ Tentativa {tentativa} falhou: {exc}", *loggers)
            if os.path.exists(destino):
                os.remove(destino)
            if tentativa < MAX_TENTATIVAS:
                log(f"  ⏳ Aguardando {PAUSA_RETRY_SEG}s antes de tentar novamente…", *loggers)
                time.sleep(PAUSA_RETRY_SEG)

    return False


def descomprimir_dbc(caminho_dbc: str, caminho_dbf: str, *loggers) -> bool:
    """
    Descomprime .dbc → .dbf usando datasus_dbc.
    Exibe spinner tqdm enquanto aguarda (operação single-threaded sem API de progresso).
    """
    try:
        tam_dbc = os.path.getsize(caminho_dbc)
        log(f"  ⚙  Descomprimindo DBC → DBF  [{tamanho_humano(tam_dbc)}]…", *loggers)

        # datasus_dbc.decompress não expõe callback de progresso;
        # usamos tqdm em modo spinner (indeterminate) para o usuário saber que está vivo.
        with tqdm(
            total=None,
            desc="    ⚙  DBC→DBF",
            unit=" bloco",
            ncols=72,
            bar_format="{l_bar}{bar} [{elapsed}]",
        ) as pbar:
            import threading

            concluido = {"ok": False, "exc": None}

            def _executar():
                try:
                    decompress(caminho_dbc, caminho_dbf)
                    concluido["ok"] = True
                except Exception as e:
                    concluido["exc"] = e

            t = threading.Thread(target=_executar, daemon=True)
            t.start()
            while t.is_alive():
                pbar.update(1)
                time.sleep(0.5)
            t.join()

        if concluido["exc"]:
            raise concluido["exc"]
        if not concluido["ok"]:
            raise RuntimeError("Descompressão terminou sem sucesso.")

        tam_dbf = os.path.getsize(caminho_dbf)
        log(f"  ✔ DBF gerado  [{tamanho_humano(tam_dbf)}]", *loggers)
        return True

    except Exception as exc:
        log(f"  ✘ Erro na descompressão: {exc}", *loggers)
        return False


def converter_para_csv_e_gz(
    caminho_dbf: str,
    caminho_csv: str,
    caminho_gz:  str,
    *loggers,
) -> dict | None:
    """
    Lê o DBF em modo streaming e gera:
      - CSV plano  (utf-8-sig) → csv_archive/    [streaming, sem carregar tudo na RAM]
      - CSV.GZ     (comprimido) → gz_archive/    [streaming por chunks]

    ⚠️  A abordagem pd.DataFrame(iter(dbf_dados)) carrega TUDO na memória e trava
    para arquivos grandes (ex.: DENGBR15 → 734 MB de DBF).
    Aqui usamos csv.DictWriter iterando registro a registro com tqdm.

    Retorna dict com metadados ou None em caso de erro.
    """
    try:
        dbf_dados = DBF(caminho_dbf, encoding=ENCODING_DBF)

        # Contagem de registros vem do cabeçalho do DBF (operação rápida, não lê dados)
        n_linhas  = len(dbf_dados)
        log(f"  📖 Streaming DBF → CSV  ({n_linhas:,} registros detectados no cabeçalho)…", *loggers)

        # ── Streaming DBF → CSV plano ──────────────────────────────
        # Itera um registro por vez: uso de RAM constante, independente do tamanho.
        n_colunas  = 0
        writer_csv = None
        t_inicio   = time.time()

        with open(caminho_csv, "w", encoding=ENCODING_CSV, newline="") as f_csv:
            with tqdm(
                total=n_linhas,
                desc="    📖 DBF→CSV",
                unit="reg",
                unit_scale=True,
                ncols=72,
                bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} reg [{elapsed}<{remaining}, {rate_fmt}]",
            ) as pbar:
                for record in dbf_dados:
                    row = dict(record)
                    if writer_csv is None:
                        fieldnames = list(row.keys())
                        n_colunas  = len(fieldnames)
                        writer_csv = csv.DictWriter(f_csv, fieldnames=fieldnames)
                        writer_csv.writeheader()
                    writer_csv.writerow(row)
                    pbar.update(1)

        tam_csv   = os.path.getsize(caminho_csv)
        vel_reg_s = n_linhas / max(time.time() - t_inicio, 0.001)
        log(
            f"  ✔ CSV salvo  [{tamanho_humano(tam_csv)}] · "
            f"{n_linhas:,} reg × {n_colunas} cols · "
            f"{vel_reg_s:,.0f} reg/s",
            *loggers,
        )

        # ── Streaming CSV → CSV.GZ ─────────────────────────────────
        log("  🗜  Comprimindo → gz_archive/ (streaming por chunks)…", *loggers)
        with open(caminho_csv, "rb") as f_in, \
             gzip.open(caminho_gz, "wb") as f_out:
            with tqdm(
                total=tam_csv,
                desc="    🗜  CSV→GZ ",
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                ncols=72,
                bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
            ) as pbar:
                while True:
                    chunk = f_in.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    f_out.write(chunk)
                    pbar.update(len(chunk))

        tam_gz = os.path.getsize(caminho_gz)
        razao  = (1 - tam_gz / tam_csv) * 100 if tam_csv else 0.0
        log(f"  ✔ CSV.GZ salvo [{tamanho_humano(tam_gz)}]  (redução: {razao:.1f}%)", *loggers)

        return {
            "registros": n_linhas,
            "colunas":   n_colunas,
            "tam_csv":   tam_csv,
            "tam_gz":    tam_gz,
            "razao_gz":  razao,
        }

    except Exception as exc:
        log(f"  ✘ Erro na conversão: {exc}", *loggers)
        log(traceback.format_exc(), *loggers)
        return None


# ═════════════════════════════════════════════════════════════
#  RELATÓRIO DE LEITURA (snippets pandas)
# ═════════════════════════════════════════════════════════════

def gerar_relatorio_leitura(resultados: list, nome_dataset: str, *loggers) -> None:
    """
    Demonstra como carregar os arquivos gerados em Python e exibe
    um resumo de leitura por arquivo.
    """
    log(subcabecalho(f"DEMONSTRAÇÃO DE LEITURA — {nome_dataset}"), *loggers)

    for r in resultados:
        if r["status"] != "OK":
            continue

        nome = r["nome_base"]
        log(f"\n  [{nome}]", *loggers)

        caminho_csv = r["caminho_csv"]
        if os.path.exists(caminho_csv):
            try:
                df_csv = pd.read_csv(caminho_csv, encoding=ENCODING_CSV, nrows=3)
                log(f"    pd.read_csv('csv_archive/{nome}.csv')  "
                    f"→ shape {df_csv.shape}", *loggers)
            except Exception as exc:
                log(f"    Erro ao ler CSV: {exc}", *loggers)

        caminho_gz = r["caminho_gz"]
        if os.path.exists(caminho_gz):
            try:
                df_gz = pd.read_csv(caminho_gz, compression="gzip",
                                    encoding=ENCODING_CSV, nrows=3)
                log(f"    pd.read_csv('gz_archive/{nome}.csv.gz', compression='gzip')  "
                    f"→ shape {df_gz.shape}", *loggers)
            except Exception as exc:
                log(f"    Erro ao ler CSV.GZ: {exc}", *loggers)


# ═════════════════════════════════════════════════════════════
#  PIPELINE POR DATASET
# ═════════════════════════════════════════════════════════════

def processar_dataset(ds: dict, log_consolidado) -> tuple:
    """
    Executa o pipeline completo para um dataset (Dengue ou Zika).

    Parâmetros
    ----------
    ds              : dict com chaves nome, sigla, urls, dir, log_nome
    log_consolidado : file object do log geral (aberto para escrita)

    Retorna
    -------
    (resultados: list[dict], duracao_total: float)
    """
    nome_ds  = ds["nome"]
    urls     = ds["urls"]
    base_dir = ds["dir"]
    log_path = os.path.join(base_dir, ds["log_nome"])

    inicio_geral = time.time()

    # Garante que a pasta do dataset existe antes de abrir o log
    os.makedirs(base_dir, exist_ok=True)

    with open(log_path, "w", encoding="utf-8") as log_ds:

        # Cabeçalho do log individual
        log(cabecalho(f"DATASUS SINAN-{ds['sigla']} — Pipeline DBC → CSV / CSV.GZ"), log_ds, log_consolidado)
        log(f"  Dataset       : {nome_ds}", log_ds, log_consolidado)
        log(f"  Início        : {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", log_ds, log_consolidado)
        log(f"  Pasta base    : {base_dir}", log_ds, log_consolidado)
        log(f"  Total arquivos: {len(urls)}\n", log_ds, log_consolidado)

        # Cria subpastas
        print(cabecalho(f"Criando estrutura de pastas — {nome_ds}"))
        dbc_dir, csv_dir, gz_dir = criar_estrutura_pastas(base_dir, nome_ds)

        log(f"  dbc_archive/  : {dbc_dir}", log_ds, log_consolidado)
        log(f"  csv_archive/  : {csv_dir}", log_ds, log_consolidado)
        log(f"  gz_archive/   : {gz_dir}\n", log_ds, log_consolidado)

        resultados: list[dict] = []

        for idx, url in enumerate(urls, start=1):
            nome_dbc  = url.split("/")[-1]            # ex: DENGBR23.dbc
            nome_base = nome_dbc.replace(".dbc", "")  # ex: DENGBR23

            caminho_dbc = os.path.join(dbc_dir, nome_dbc)
            caminho_dbf = os.path.join(base_dir, f"{nome_base}.dbf")  # temporário
            caminho_csv = os.path.join(csv_dir,  f"{nome_base}.csv")
            caminho_gz  = os.path.join(gz_dir,   f"{nome_base}.csv.gz")

            resultado = {
                "idx":         idx,
                "nome_base":   nome_base,
                "url":         url,
                "caminho_dbc": caminho_dbc,
                "caminho_csv": caminho_csv,
                "caminho_gz":  caminho_gz,
                "status":      "PENDENTE",
                "registros":   0,
                "colunas":     0,
                "tam_dbc":     0,
                "tam_csv":     0,
                "tam_gz":      0,
                "razao_gz":    0.0,
                "erro":        "",
                "duracao_s":   0.0,
            }

            log(subcabecalho(f"[{idx:02d}/{len(urls)}]  {nome_dbc}  [{nome_ds}]"),
                log_ds, log_consolidado)
            log(f"  URL : {url}", log_ds, log_consolidado)
            log(f"  DBC → {caminho_dbc}", log_ds, log_consolidado)
            log(f"  CSV → {caminho_csv}", log_ds, log_consolidado)
            log(f"  GZ  → {caminho_gz}",  log_ds, log_consolidado)

            inicio = time.time()

            # ── Pula se CSV e GZ já existem (idempotência) ──────────
            if os.path.exists(caminho_csv) and os.path.exists(caminho_gz):
                log("  ⏭  CSV e CSV.GZ já existem — pulando.", log_ds, log_consolidado)
                resultado["status"]  = "PULADO"
                resultado["tam_dbc"] = os.path.getsize(caminho_dbc) if os.path.exists(caminho_dbc) else 0
                resultado["tam_csv"] = os.path.getsize(caminho_csv)
                resultado["tam_gz"]  = os.path.getsize(caminho_gz)
                resultado["duracao_s"] = round(time.time() - inicio, 2)
                resultados.append(resultado)
                continue

            # ── 1. Download .dbc → dbc_archive/ ─────────────────────
            if not os.path.exists(caminho_dbc):
                ok = baixar_dbc(url, caminho_dbc, log_ds, log_consolidado)
                if not ok:
                    resultado["status"]    = "ERRO_DOWNLOAD"
                    resultado["erro"]      = "Falha no download após todas as tentativas."
                    resultado["duracao_s"] = round(time.time() - inicio, 2)
                    resultados.append(resultado)
                    continue
            else:
                log("  ⏭  DBC já existe em dbc_archive/ — pulando download.", log_ds, log_consolidado)

            resultado["tam_dbc"] = os.path.getsize(caminho_dbc)

            # ── 2. Descompressão .dbc → .dbf (temporário) ───────────
            ok = descomprimir_dbc(caminho_dbc, caminho_dbf, log_ds, log_consolidado)
            if not ok:
                resultado["status"]    = "ERRO_DECOMPRESS"
                resultado["erro"]      = "Falha na descompressão DBC→DBF."
                resultado["duracao_s"] = round(time.time() - inicio, 2)
                resultados.append(resultado)
                continue

            # ── 3. Conversão DBF → CSV + GZ ──────────────────────────
            meta = converter_para_csv_e_gz(
                caminho_dbf, caminho_csv, caminho_gz,
                log_ds, log_consolidado,
            )

            # Remove DBF temporário independente do resultado
            if os.path.exists(caminho_dbf):
                os.remove(caminho_dbf)
                log("  🗑  DBF temporário removido.", log_ds, log_consolidado)

            if meta is None:
                resultado["status"] = "ERRO_CONVERSAO"
                resultado["erro"]   = "Falha na conversão DBF→CSV/GZ."
            else:
                resultado.update({
                    "status":    "OK",
                    "registros": meta["registros"],
                    "colunas":   meta["colunas"],
                    "tam_csv":   meta["tam_csv"],
                    "tam_gz":    meta["tam_gz"],
                    "razao_gz":  meta["razao_gz"],
                })

            resultado["duracao_s"] = round(time.time() - inicio, 2)
            resultados.append(resultado)
            log(f"  ⏱  Tempo do arquivo: {resultado['duracao_s']:.1f}s",
                log_ds, log_consolidado)

        # ── Demonstração de leitura ──────────────────────────────────
        gerar_relatorio_leitura(resultados, nome_ds, log_ds, log_consolidado)

        # ── Relatório final do dataset ───────────────────────────────
        duracao_total = round(time.time() - inicio_geral, 2)

        log(cabecalho(f"RELATÓRIO FINAL — {nome_ds.upper()}"), log_ds, log_consolidado)

        # Tabela principal (por arquivo)
        tbl_arq = tabela_resultados(
            resultados,
            titulo=f"Detalhamento por arquivo · {nome_ds}",
        )
        log(tbl_arq, log_ds, log_consolidado)

        # Tabela de totais
        log(f"\n  Totais · {nome_ds}", log_ds, log_consolidado)
        tbl_tot = tabela_totais(resultados, duracao_total)
        log(tbl_tot, log_ds, log_consolidado)

        # Tabela de erros
        erros = [r for r in resultados if r["status"].startswith("ERRO")]
        if erros:
            log(f"\n  Arquivos com erro · {nome_ds}", log_ds, log_consolidado)
            tbl_err = tabela_erros(resultados)
            log(tbl_err, log_ds, log_consolidado)

        log(f"\n  📄 Log individual salvo em: {log_path}", log_ds, log_consolidado)
        log(subcabecalho(f"FIM DO PIPELINE — {nome_ds.upper()}"), log_ds, log_consolidado)

    return resultados, duracao_total


# ═════════════════════════════════════════════════════════════
#  SNIPPETS PARA USO EM ANÁLISE / ML
# ═════════════════════════════════════════════════════════════

SNIPPETS_ML = '''\
# ══════════════════════════════════════════════════════════════
#  SNIPPETS — Como usar os arquivos gerados em Python / ML
#
#  Estrutura de pastas:
#    Source/Dengue/dbc_archive/   → DENGBRXX.dbc
#    Source/Dengue/csv_archive/   → DENGBRXX.csv
#    Source/Dengue/gz_archive/    → DENGBRXX.csv.gz
#    Source/Zika/dbc_archive/     → ZIKABRXX.dbc
#    Source/Zika/csv_archive/     → ZIKABRXX.csv
#    Source/Zika/gz_archive/      → ZIKABRXX.csv.gz
# ══════════════════════════════════════════════════════════════

import pandas as pd
import glob, os

# ── 1. Carregar um único CSV (Dengue) ─────────────────────────
df = pd.read_csv("Source/Dengue/csv_archive/DENGBR23.csv", encoding="utf-8-sig")

# ── 2. Carregar um único CSV.GZ (Zika, memória eficiente) ─────
df = pd.read_csv("Source/Zika/gz_archive/ZIKABR23.csv.gz",
                 compression="gzip", encoding="utf-8-sig")

# ── 3. Concatenar TODOS os anos de Dengue ─────────────────────
arqs_deng = sorted(glob.glob("Source/Dengue/gz_archive/DENGBR*.csv.gz"))
df_dengue = pd.concat(
    [pd.read_csv(f, compression="gzip", encoding="utf-8-sig") for f in arqs_deng],
    ignore_index=True,
)
print("Dengue:", df_dengue.shape)

# ── 4. Concatenar TODOS os anos de Zika ───────────────────────
arqs_zika = sorted(glob.glob("Source/Zika/gz_archive/ZIKABR*.csv.gz"))
df_zika = pd.concat(
    [pd.read_csv(f, compression="gzip", encoding="utf-8-sig") for f in arqs_zika],
    ignore_index=True,
)
print("Zika:", df_zika.shape)

# ── 5. Leitura em chunks (datasets muito grandes) ─────────────
chunks = pd.read_csv(
    "Source/Dengue/gz_archive/DENGBR23.csv.gz",
    compression="gzip",
    encoding="utf-8-sig",
    chunksize=100_000,    # processa 100k linhas por vez
)
for chunk in chunks:
    pass  # seu processamento aqui

# ── 6. Uso com Scikit-learn ───────────────────────────────────
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Source/Dengue/gz_archive/DENGBR23.csv.gz",
                 compression="gzip", encoding="utf-8-sig")

df.dropna(axis=1, how="all", inplace=True)

for col in df.select_dtypes(include="object").columns:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

X = df.drop(columns=["CLASSI_FIN"])   # ajuste para sua coluna alvo
y = df["CLASSI_FIN"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
'''


# ═════════════════════════════════════════════════════════════
#  MAIN
# ═════════════════════════════════════════════════════════════

def main():
    inicio_global = time.time()
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Garante que a pasta Source/ existe antes de abrir o log consolidado
    os.makedirs(SOURCE_DIR, exist_ok=True)

    print(cabecalho("DATASUS SINAN — Dengue + Zika · Pipeline DBC → CSV / CSV.GZ"))
    print(f"  Início : {timestamp}")
    print(f"  Source : {SOURCE_DIR}")
    print(f"  Log    : {LOG_CONSOLIDADO}\n")

    todos_resumos: list[dict] = []

    with open(LOG_CONSOLIDADO, "w", encoding="utf-8") as log_geral:

        log(cabecalho("DATASUS SINAN — DENGUE + ZIKA · Pipeline Consolidado"),
            log_geral)
        log(f"  Início          : {timestamp}", log_geral)
        log(f"  Pasta Source/   : {SOURCE_DIR}", log_geral)
        log(f"  Datasets        : {', '.join(ds['nome'] for ds in DATASETS)}", log_geral)
        log(f"  Total de URLs   : {sum(len(ds['urls']) for ds in DATASETS)}", log_geral)

        # ── Processa cada dataset (Dengue, Zika) ────────────────────
        for ds in DATASETS:
            resultados, duracao = processar_dataset(ds, log_geral)

            ok_lista = [r for r in resultados if r["status"] == "OK"]
            pulados  = [r for r in resultados if r["status"] == "PULADO"]
            erros    = [r for r in resultados if r["status"].startswith("ERRO")]

            todos_resumos.append({
                "nome":      ds["nome"],
                "ok":        len(ok_lista),
                "pulados":   len(pulados),
                "erros":     len(erros),
                "registros": sum(r["registros"] for r in ok_lista),
                "dbc":       sum(r["tam_dbc"]   for r in resultados if r["tam_dbc"]),
                "csv":       sum(r["tam_csv"]   for r in resultados if r["tam_csv"]),
                "gz":        sum(r["tam_gz"]    for r in resultados if r["tam_gz"]),
                "duracao":   duracao,
            })

        # ── Relatório consolidado (Dengue × Zika) ───────────────────
        duracao_global = round(time.time() - inicio_global, 2)

        log(cabecalho("RELATÓRIO CONSOLIDADO — DENGUE × ZIKA"), log_geral)

        tbl_cons = tabela_consolidada(todos_resumos)
        log("\n  Comparativo por dataset\n", log_geral)
        log(tbl_cons, log_geral)

        total_geral_reg = sum(ds["registros"] for ds in todos_resumos)
        total_geral_csv = sum(ds["csv"]       for ds in todos_resumos)
        total_geral_gz  = sum(ds["gz"]        for ds in todos_resumos)
        total_geral_dbc = sum(ds["dbc"]       for ds in todos_resumos)

        t_geral = Texttable(max_width=55)
        t_geral.set_deco(Texttable.HEADER | Texttable.BORDER | Texttable.VLINES)
        t_geral.set_cols_align(["l", "r"])
        t_geral.set_cols_dtype(["t", "t"])
        t_geral.set_cols_width([30, 18])
        t_geral.header(["Métrica Global", "Valor"])
        t_geral.add_row(["Total de registros (ambos)",   f"{total_geral_reg:,}"])
        t_geral.add_row(["Espaço total dbc_archive/",    tamanho_humano(total_geral_dbc)])
        t_geral.add_row(["Espaço total csv_archive/",    tamanho_humano(total_geral_csv)])
        t_geral.add_row(["Espaço total gz_archive/",     tamanho_humano(total_geral_gz)])
        t_geral.add_row(["Tempo total da execução",       f"{duracao_global:.1f}s ({duracao_global/60:.1f} min)"])
        t_geral.add_row(["Fim da execução",               datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])

        log("\n  Totais globais\n", log_geral)
        log(t_geral.draw(), log_geral)

        log(f"\n  📄 Log consolidado : {LOG_CONSOLIDADO}", log_geral)
        for ds in DATASETS:
            log_path = os.path.join(ds["dir"], ds["log_nome"])
            log(f"  📄 Log {ds['nome']:<8}    : {log_path}", log_geral)

        log(cabecalho("FIM DO PIPELINE CONSOLIDADO"), log_geral)

    # ── Exibe snippets de uso ────────────────────────────────────────
    print("\n" + "═" * 68)
    print("  SNIPPETS PARA ANÁLISE / ML")
    print("═" * 68)
    print(SNIPPETS_ML)

    print(cabecalho("ESTRUTURA DE PASTAS GERADA"))
    print(f"""
  {SOURCE_DIR}/
  ├── Dengue/
  │   ├── dbc_archive/
  │   ├── csv_archive/
  │   ├── gz_archive/
  │   └── log_datasus_sinan_dengue.txt
  ├── Zika/
  │   ├── dbc_archive/
  │   ├── csv_archive/
  │   ├── gz_archive/
  │   └── log_datasus_sinan_zika.txt
  └── log_datasus_sinan_dengue_zika.txt
""")


if __name__ == "__main__":
    main()
