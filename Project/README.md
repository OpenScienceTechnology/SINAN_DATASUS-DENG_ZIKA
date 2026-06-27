# SIPREV — Sistema Inteligente de Previsão Epidemiológica de Dengue · v1.3

Análise epidemiológica e **modelagem preditiva** de **Dengue** em
**Campo Grande/MS** (IBGE `5002704` · SINAN `500270`), a partir dos microdados
do **SINAN/DATASUS** (2015–2026).

Versão **1.3 (estendida)** — **~20.900 linhas** — com **300 bibliotecas
catalogadas** (100 ML + 100 DL + 100 NN), novos módulos de **RNN**, **ANN** e
**NLP**, modelagem preditiva unificada (previsão · predição · prevenção ·
comparação), **download automático dos dados com barra de progresso** e geração
de material para artigo de **pesquisa sobre tecnologia emergente**.

---

## 📦 Arquivos entregues (`update/`)

| Arquivo | Descrição |
|---|---|
| `SIPREV_Data_Epidemiological_DENG_v1.3.py` | Programa Python completo e autossuficiente (~20.900 linhas) |
| `SIPREV_Data_Epidemiological_DENG_v1.3.ipynb` | Notebook Jupyter equivalente, **multi-célula** (371 células) |
| `README.md` | Este documento |

Ambos os arquivos são **independentes** e produzem os mesmos resultados.

---

## ✅ Onde executa

| Ambiente | `.py` | `.ipynb` |
|---|---|---|
| **Google Colab** | via terminal | ✅ upload + *Run all* |
| **Google Cloud Console / Cloud Shell** | ✅ via terminal | ✅ via terminal |
| **Máquina local** (Anaconda / Python 3.12–3.14) | ✅ `python ...v1.3.py` | ✅ Jupyter (*Run all*) |

> **Recomendado:** Python **3.14** (ou **3.12** completo / **Anaconda**) — reúnem
> mais bibliotecas. O programa **detecta o ambiente**, instala dependências em
> nuvem e **degrada com segurança** quando uma biblioteca opcional está ausente.
> **DL/RNN/ANN/NLP usam PyTorch + scikit-learn** (rodam sem TensorFlow).

---

## ▶ Como executar

### Local (terminal)
```bash
# Use o Python com mais bibliotecas (3.14 ou 3.12) ou Anaconda
python SIPREV_Data_Epidemiological_DENG_v1.3.py
```

### Notebook (Jupyter / Colab)
Abra o `.ipynb` e execute **todas as células em ordem** (*Run all*).
A **última célula** chama `main_v4()`, que (se necessário) **baixa os dados**,
executa todo o pipeline e gera o **ZIP**.

### Dados ausentes? São baixados automaticamente (com barra de progresso)
```python
garantir_dados_local()    # localiza ou BAIXA DENGBR15..26.csv (log inline: URL+nome, início/fim)
```

### Sem internet/dados? Valide com dados sintéticos
```python
executar_demo_sintetica()
```

---

## 🧠 300 bibliotecas catalogadas (100 por categoria)

```python
compilar_300_bibliotecas()        # 100 ML + 100 DL + 100 NN (detecção de versão)
catalogo_machine_learning_100()   # 100 bibliotecas de Machine Learning
catalogo_deep_learning_100()      # 100 bibliotecas de Deep Learning
catalogo_neural_networks_100()    # 100 bibliotecas de Neural Networks
```
Exportadas em TXT/LOG (Texttable), CSV e XLSX.

---

## 🤖 Modelos (previsão · predição · prevenção · comparação)

### 1–3. Machine Learning · Deep Learning · Neural Networks (Grandes Modelos)
Dezenas de arquiteturas: florestas/boosting (XGBoost, LightGBM, CatBoost),
GLM, GP, SVR, ensembles (Stacking/Voting); LSTM/GRU, TCN/WaveNet, Transformer,
N-BEATS/N-HiTS, InceptionTime, PatchTST, Autoformer, TiDE, DLinear, MLP-Mixer…;
Deep Dense, Residual, Wide&Deep, TabNet, FT-Transformer, AutoInt, DeepFM, DCN…
Inclui **backtesting walk-forward**, **intervalos de predição (P10/P50/P90)**,
seleção de variáveis, tuning, clusterização sazonal e detecção de anomalias.

### 4. 🧬 Recurrent Neural Networks (RNNs) — **novo**
RNN simples (Elman), RNN empilhada, RNN bidirecional, RNN com atenção,
híbrido LSTM→GRU e BiGRU profunda (`executar_rnn_grandes_modelos`).

### 5. 🧬 Artificial Neural Networks (ANNs) — **novo**
Perceptron, ANN rasa, ANN profunda, ANN larga e ANN clássica (tanh)
(`executar_ann_grandes_modelos`).

### 6. 🧠 Natural Language Processing (NLP) — **novo**
Constrói um **corpus de resumos clínicos** a partir das variáveis estruturadas
e aplica **frequência de termos, n-gramas, modelagem de tópicos (LDA)** e
nuvem de palavras (`executar_nlp`).

### 7. Modelagem preditiva / análise / processamento
```python
comparacao_preditiva_global(df)   # compara modelos + ENSEMBLE + backtesting
relatorio_prevencao(df)           # risco + recomendações (TXT/PDF)
cenarios_prevencao(df)            # otimista / realista / pessimista
processamento_dados_completo(df)  # perfil, memória, correlação, features
leaderboard_unificado()           # ranking entre todas as categorias
```

### Rede de Coocorrência (NetworkX)
Sintomas, sinais de alarme, gravidade, sintomas×desfecho e variáveis entre
modelos (centralidades, comunidades, GraphML/PNG/HTML).

---

## 📜 Exibição inline e exportação

- **Todas** as saídas (gráficos, mapas, tabelas, dashboards) são exibidas
  **inline durante a execução**.
- **Download** dos dados com **barra de progresso inline** (início/fim + URL + nome).
- Exportação em **PNG, HTML, TXT, LOG, CSV, XLSX, PDF, JSON, PARQUET, GraphML, MD**.
- Pacote final: **`SIPREV_DENG_MS_EpiAnalysis_<data_hora>.zip`** (com todos os itens;
  baixado automaticamente no Colab).

```
output/
├── graficos/  ├── mapas/  ├── dashboards/  ├── relatorios/  ├── dados/
└── SIPREV_DENG_MS_EpiAnalysis_<data_hora>.zip
```

---

## 📝 Material para artigo (tecnologia emergente)

```python
gera_rascunho_artigo()         # rascunho de artigo científico (Markdown)
relatorio_tecnico_completo()   # relatório técnico completo (Markdown)
gerar_model_cards_v12()        # fichas técnicas das arquiteturas
```

---

## 🔧 Requisitos

**Essenciais:** numpy, pandas, scipy, matplotlib, seaborn, scikit-learn, texttable.
**Recomendados:** networkx, torch, xgboost, lightgbm, catboost, statsmodels,
plotly, kaleido, folium, openpyxl, xlsxwriter, fpdf2, wordcloud (NLP, opcional).

```bash
pip install numpy pandas scipy matplotlib seaborn scikit-learn texttable \
            networkx torch xgboost lightgbm catboost statsmodels \
            plotly kaleido folium openpyxl xlsxwriter fpdf2 wordcloud
```
> No Colab/Cloud Shell a instalação é automática. Localmente, prefira **Python
> 3.14/3.12** ou **Anaconda** (mais bibliotecas).

---

## ⚙️ Entradas principais

| Comando | Ação |
|---|---|
| `main_v4()` | Pipeline completo v1.3 (dados → base → ML/DL/NN/RNN/ANN/NLP → ZIP) |
| `executar_extras_v4(df)` | Apenas RNN · ANN · NLP |
| `garantir_dados_local()` | Localiza ou baixa os CSVs (barra de progresso) |
| `executar_demo_sintetica()` | Validação completa com dados sintéticos |
| `listar_modulos_v2()` / `mapa_de_funcoes()` | Lista de módulos |

---

## ℹ️ Notas

- Análise prioriza o **município de residência** (`ID_MN_RESI`); taxas por 100
  mil habitantes usam população do IBGE.
- `CLASSI_FIN` adota a codificação vigente do SINAN (**10/11/12**) e a legada (1–4).
- O conjunto completo de CSVs tem **vários GB**; comece por um subconjunto de
  anos (`anos=[...]`) para validar o ambiente. Ajuste `chunk_size` se necessário.
- Suporte a Python **3.12 / 3.13 / 3.14** (degradação segura de libs opcionais).

---

**SIPREV v1.3** — Dengue · Campo Grande/MS · SINAN/DATASUS · 2015–2026 ·
*Pesquisa sobre tecnologia emergente*
