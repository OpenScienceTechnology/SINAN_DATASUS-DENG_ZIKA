# 🦟 DATASUS SINAN — Pipeline DBC → CSV / CSV.GZ

## Dengue · Zika Vírus · Epidemiologia · Ciência de Dados

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![DATASUS](https://img.shields.io/badge/DATASUS-SINAN-green)
![Status](https://img.shields.io/badge/status-estável-success)
![BigData](https://img.shields.io/badge/Big%20Data-ready-orange)
![MachineLearning](https://img.shields.io/badge/Machine%20Learning-enabled-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

# 📌 Sobre o Projeto

O **DATASUS SINAN Pipeline** é um sistema automatizado em Python desenvolvido para realizar o processamento completo dos microdados epidemiológicos do **SINAN/DATASUS**, com foco nos agravos:

* 🦟 Dengue
* 🧬 Zika Vírus

O pipeline executa automaticamente:

✅ Download dos arquivos `.dbc` do DATASUS
✅ Descompressão `.dbc → .dbf`
✅ Conversão `.dbf → .csv`
✅ Compressão `.csv → .csv.gz`
✅ Organização automática das pastas
✅ Relatórios completos de processamento
✅ Logs detalhados de execução
✅ Preparação de datasets para:

* 📊 Data Science
* 🤖 Machine Learning
* 🧠 Deep Learning
* ☁️ Big Data
* 📈 Business Intelligence
* 🔬 Epidemiologia Computacional

---

# 🧠 Objetivos do Projeto

Este projeto foi desenvolvido para:

* Automatizar a obtenção de microdados do SINAN
* Facilitar análises epidemiológicas em larga escala
* Reduzir o tempo de preparação dos dados
* Disponibilizar datasets prontos para IA e ML
* Criar uma estrutura reutilizável para pesquisas científicas
* Otimizar o armazenamento com arquivos `.csv.gz`

---

# 🏛 Fonte Oficial dos Dados

## 🔗 DATASUS — SINAN

* 🌐 FTP DATASUS
  ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/

## 🔗 Repositório de Dados

* 🌐 Dengue
  https://alpaca.quantilica.com/dados/sinan-deng

* 🌐 Zika Vírus
  https://alpaca.quantilica.com/dados/sinan-zika

---

# ⚙️ Funcionalidades

## ✅ Download Automático

O script realiza o download automático dos arquivos:

```text
DENGBR15.dbc
DENGBR16.dbc
...
ZIKABR26.dbc
```

Com:

* 🔁 Retry automático
* 📡 Controle de falhas
* 📊 Barra de progresso (`tqdm`)
* 🛡 Verificação de integridade

---

## ✅ Conversão DBC → DBF

Utiliza:

```python
datasus-dbc
```

Para descompressão dos arquivos proprietários do DATASUS.

---

## ✅ Conversão DBF → CSV

Conversão otimizada em streaming:

* 💾 Baixo consumo de RAM
* 🚀 Alta performance
* 📄 Compatível com Excel (`utf-8-sig`)
* 🔄 Processamento de grandes volumes

---

## ✅ Compressão CSV → GZIP

Geração automática de:

```text
.csv.gz
```

Ideal para:

* ☁️ Cloud Computing
* 📊 Pandas
* 🧠 Machine Learning
* 🗃 Big Data

---

## ✅ Relatórios Automáticos

O sistema gera:

* 📄 Logs individuais
* 📄 Log consolidado
* 📊 Estatísticas de arquivos
* 📈 Tempo de execução
* 📉 Taxa de compressão
* 📦 Tamanho dos datasets
* ❌ Relatório de erros

---

# 🗂 Estrutura de Pastas

```text
Source/
├── Dengue/
│   ├── dbc_archive/
│   ├── csv_archive/
│   ├── gz_archive/
│   └── log_datasus_sinan_dengue.txt
│
├── Zika/
│   ├── dbc_archive/
│   ├── csv_archive/
│   ├── gz_archive/
│   └── log_datasus_sinan_zika.txt
│
└── log_datasus_sinan_dengue_zika.txt
```

---

# 📦 Instalação

## 🔧 Requisitos

* Python 3.10+
* Pip atualizado

---

## 📥 Clone o Repositório

```bash
git clone https://github.com/seuusuario/seurepositorio.git
```

---

## 📦 Instale as Dependências

```bash
pip install dbfread pandas datasus-dbc texttable tqdm
```

---

# ▶️ Como Executar

```bash
python SINAN-DATASUS_Data_Epidemiological_Bulletin_DENG_ZIKA_v1.0.py
```

---

# 🔄 Fluxo do Pipeline

```text
FTP DATASUS
     ↓
Download .dbc
     ↓
Descompressão .dbf
     ↓
Conversão .csv
     ↓
Compressão .csv.gz
     ↓
Logs + Relatórios
```

---

# 📊 Exemplo de Leitura com Pandas

## 📄 CSV

```python
import pandas as pd

df = pd.read_csv(
    "Source/Dengue/csv_archive/DENGBR23.csv",
    encoding="utf-8-sig"
)

print(df.head())
```

---

## 🗜 CSV.GZ

```python
import pandas as pd

df = pd.read_csv(
    "Source/Zika/gz_archive/ZIKABR23.csv.gz",
    compression="gzip",
    encoding="utf-8-sig"
)

print(df.shape)
```

---

# 🚀 Processamento em Chunks

Ideal para datasets gigantes.

```python
chunks = pd.read_csv(
    "Source/Dengue/gz_archive/DENGBR23.csv.gz",
    compression="gzip",
    chunksize=100_000
)

for chunk in chunks:
    print(chunk.shape)
```

---

# 🧠 Aplicações em Ciência de Dados

Este projeto pode ser utilizado em:

## 📊 Análise Exploratória

* Distribuição espacial
* Séries temporais
* Sazonalidade epidemiológica
* Correlação geográfica

---

## 🤖 Machine Learning

* Random Forest
* XGBoost
* LightGBM
* CatBoost
* Regressão
* Árvores de decisão

---

## 🧠 Deep Learning

* LSTM
* Redes neurais
* Transformers
* Modelos temporais

---

## 🌎 Geoprocessamento

* Mapas epidemiológicos
* Heatmaps
* GIS
* GeoPandas

---

## ☁️ Big Data

Compatível com:

* Apache Spark
* Dask
* Ray
* Polars
* DuckDB

---

# 📈 Exemplo com Scikit-Learn

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X = df.drop(columns=["CLASSI_FIN"])
y = df["CLASSI_FIN"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)
```

---

# 📋 Logs Gerados

## 📝 Logs Individuais

```text
log_datasus_sinan_dengue.txt
log_datasus_sinan_zika.txt
```

---

## 📝 Log Consolidado

```text
log_datasus_sinan_dengue_zika.txt
```

Incluem:

* ✔ Arquivos processados
* ❌ Arquivos com erro
* 📊 Estatísticas
* ⏱ Tempo total
* 📦 Compressão
* 📈 Registros processados

---

# ⚡ Otimizações Implementadas

## 🚀 Streaming de Dados

Evita carregamento completo em memória.

---

## 🚀 Compressão em Chunks

Reduz uso de RAM.

---

## 🚀 Retry Automático

Maior robustez contra falhas de rede.

---

## 🚀 Idempotência

Arquivos já processados são ignorados automaticamente.

---

# 📊 Performance

O pipeline foi projetado para trabalhar com:

* 📦 Arquivos gigantes
* 💾 Baixo consumo de memória
* ⚡ Processamento contínuo
* ☁️ Ambientes cloud
* 🧠 Modelos de IA

---

# 🔐 Codificação Utilizada

| Etapa | Encoding   |
| ----- | ---------- |
| DBF   | iso-8859-1 |
| CSV   | utf-8-sig  |

---

# 🧩 Bibliotecas Utilizadas

| Biblioteca  | Função               |
| ----------- | -------------------- |
| pandas      | Manipulação de dados |
| dbfread     | Leitura DBF          |
| datasus-dbc | Descompressão DBC    |
| tqdm        | Barra de progresso   |
| texttable   | Tabelas formatadas   |
| gzip        | Compressão           |

---

# 🖥 Compatibilidade

✅ Windows
✅ Linux
✅ macOS
✅ WSL
✅ Ambientes Cloud

---

# 📚 Casos de Uso

* 🦟 Vigilância epidemiológica
* 🏥 Saúde pública
* 📈 Painéis BI
* 🤖 IA aplicada à saúde
* 📊 Modelagem preditiva
* 🌎 Estudos geoespaciais
* 📑 Pesquisa científica

---

# 🧪 Possíveis Extensões Futuras

* ☁️ Upload automático para Google Cloud
* 🗃 Integração com PostgreSQL
* ⚡ Apache Spark
* 📊 Dashboard Streamlit
* 🌎 Visualização geográfica
* 🤖 Modelos preditivos automáticos
* 📡 API REST epidemiológica

---

# 👨‍💻 Autor

Projeto desenvolvido para:

* 📊 Ciência de Dados
* 🏥 Epidemiologia Computacional
* 🤖 Inteligência Artificial
* 📈 Big Data em Saúde Pública

---

# 📜 Licença

Este projeto pode ser utilizado para:

✅ Pesquisa acadêmica
✅ Estudos epidemiológicos
✅ Ciência de Dados
✅ Saúde Pública

---

# ⭐ Contribuição

Contribuições são bem-vindas:

* 🐛 Correções
* 🚀 Melhorias
* 📊 Novas análises
* ☁️ Integrações
* 🤖 IA aplicada

---

# ❤️ Agradecimentos

* 🏛 DATASUS
* 🇧🇷 Ministério da Saúde
* 📊 Comunidade Python
* 🧠 Comunidade Open Source

---

# 📌 Observações

⚠️ Os dados disponibilizados pelo DATASUS podem sofrer alterações sem aviso prévio.

⚠️ Arquivos preliminares (`PRELIM`) podem conter atualizações futuras.

⚠️ Recomenda-se o uso de ambientes com armazenamento adequado devido ao volume dos datasets.

---

# 📞 Contato

📧 Sugestões, melhorias e colaborações são bem-vindas.

---

# ⭐ Se este projeto foi útil...

Deixe uma estrela no repositório ⭐

