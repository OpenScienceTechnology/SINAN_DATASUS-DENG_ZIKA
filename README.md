# 🦟 SINAN DATASUS — Dengue & Zika Dataset (2015–2026)

## Microdados Epidemiológicos do DATASUS/SINAN em CSV e CSV.GZ

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Dataset](https://img.shields.io/badge/Dataset-Epidemiologia-green)
![DATASUS](https://img.shields.io/badge/DATASUS-SINAN-success)
![BigData](https://img.shields.io/badge/Big%20Data-ready-orange)
![CSV](https://img.shields.io/badge/Format-CSV-informational)
![GZIP](https://img.shields.io/badge/Compression-GZIP-purple)
![License](https://img.shields.io/badge/license-Open%20Data-lightgrey)

---

# 📌 Sobre o Repositório

Este repositório disponibiliza datasets epidemiológicos públicos do **SINAN/DATASUS** relacionados aos agravos:

* 🦟 Dengue
* 🧬 Zika Vírus

Os arquivos foram:

✅ Baixados diretamente do DATASUS
✅ Convertidos de `.dbc` → `.csv`
✅ Compactados em `.csv.gz`
✅ Organizados para uso em:

* 📊 Ciência de Dados
* 🤖 Machine Learning
* 🧠 Deep Learning
* ☁️ Big Data
* 📈 Business Intelligence
* 🌎 Geoprocessamento
* 🏥 Epidemiologia Computacional

---

# 🌐 Repositório Oficial

## 🔗 GitHub

https://github.com/OpenScienceTechnology/SINAN_DATASUS-DENG_ZIKA

---

# 🏛 Fonte Oficial dos Dados

Os dados são provenientes do:

## 🇧🇷 DATASUS — Ministério da Saúde

### 🔗 FTP Oficial

```text id="lwh4l7"
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/
```

---

# 📂 Estrutura do Repositório

```text id="5v30eh"
Dataset/
├── Dengue/
│   ├── csv_archive/
│   ├── gz_archive/
│   └── log_datasus_sinan_dengue_csv_gz.txt/
│
├── Zika/
│   ├── csv_archive/
│   ├── gz_archive/
│   └── log_datasus_sinan_zika_csv_gz.txt/
├── log_datasus_sinan_dengue_zika_csv_gz/
│
└── README.md
```

---

# 📁 Estrutura dos Arquivos

## 🦟 Dengue

### 📄 CSV

```text id="c8y13v"
Dataset/Dengue/csv_archive/
```

Arquivos:

```text id="hbrv51"
DENGBR15.csv
DENGBR16.csv
DENGBR17.csv
...
DENGBR26.csv
```

---

### 🗜 CSV.GZ

```text id="o1kj9m"
Dataset/Dengue/gz_archive/
```

Arquivos compactados para:

* ☁️ Cloud
* 📊 Pandas
* 🧠 ML
* 💾 Economia de armazenamento

---

## 🧬 Zika Vírus

### 📄 CSV

```text id="92o9tx"
Dataset/Zika/csv_archive/
```

Arquivos:

```text id="6h7jq0"
ZIKABR16.csv
ZIKABR17.csv
ZIKABR18.csv
...
ZIKABR26.csv
```

---

### 🗜 CSV.GZ

```text id="4h4hpy"
Dataset/Zika/gz_archive/
```

---

# 📅 Cobertura Temporal

| Dataset | Período     |
| ------- | ----------- |
| Dengue  | 2015 → 2026 |
| Zika    | 2016 → 2026 |

# 🇧🇷 Abrangência Nacional — Estados e Códigos IBGE

Este banco possui abrangência nacional, podendo conter registros relacionados às 27 Unidades Federativas do Brasil.

| Código IBGE | UF | Estado |
|---:|:---:|---|
| 11 | RO | Rondônia |
| 12 | AC | Acre |
| 13 | AM | Amazonas |
| 14 | RR | Roraima |
| 15 | PA | Pará |
| 16 | AP | Amapá |
| 17 | TO | Tocantins |
| 21 | MA | Maranhão |
| 22 | PI | Piauí |
| 23 | CE | Ceará |
| 24 | RN | Rio Grande do Norte |
| 25 | PB | Paraíba |
| 26 | PE | Pernambuco |
| 27 | AL | Alagoas |
| 28 | SE | Sergipe |
| 29 | BA | Bahia |
| 31 | MG | Minas Gerais |
| 32 | ES | Espírito Santo |
| 33 | RJ | Rio de Janeiro |
| 35 | SP | São Paulo |
| 41 | PR | Paraná |
| 42 | SC | Santa Catarina |
| 43 | RS | Rio Grande do Sul |
| 50 | MS | Mato Grosso do Sul |
| 51 | MT | Mato Grosso |
| 52 | GO | Goiás |
| 53 | DF | Distrito Federal |

⚠️ Os anos mais recentes (`2025` e `2026`) pertencem à categoria:

```text id="nyryph"
PRELIM
```

Ou seja:

* Dados preliminares
* Podem sofrer atualizações futuras
* Ainda sujeitos à consolidação oficial

---

# 🔗 URLs Oficiais — DENGUE

```text id="jmsmvv"
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR15.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR16.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR17.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR18.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR19.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR20.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR21.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR22.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR23.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/DENGBR24.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/PRELIM/DENGBR25.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/PRELIM/DENGBR26.dbc
```

---

# 🔗 URLs Oficiais — ZIKA

```text id="7qyzkm"
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR16.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR17.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR18.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR19.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR20.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR21.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR22.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR23.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS/ZIKABR24.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/PRELIM/ZIKABR25.dbc
ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/PRELIM/ZIKABR26.dbc
```

---

# 📦 Formatos Disponíveis

| Formato   | Descrição                        |
| --------- | -------------------------------- |
| `.csv`    | Texto plano compatível com Excel |
| `.csv.gz` | CSV compactado em GZIP           |

---

# 🚀 Vantagens do CSV.GZ

Os arquivos `.csv.gz` oferecem:

✅ Menor uso de disco
✅ Menor tráfego de rede
✅ Melhor performance em cloud
✅ Ideal para Big Data
✅ Compatível com Pandas/Spark

---

# 📊 Como Ler os Arquivos

## 📄 CSV

```python id="p5o4o4"
import pandas as pd

df = pd.read_csv(
    "Dataset/Dengue/csv_archive/DENGBR23.csv",
    encoding="utf-8-sig"
)

print(df.head())
```

---

## 🗜 CSV.GZ

```python id="h6v8we"
import pandas as pd

df = pd.read_csv(
    "Dataset/Zika/gz_archive/ZIKABR23.csv.gz",
    compression="gzip",
    encoding="utf-8-sig"
)

print(df.shape)
```

---

# ⚡ Leitura em Chunks (Big Data)

Ideal para datasets gigantes.

```python id="u6hh6i"
chunks = pd.read_csv(
    "Dataset/Dengue/gz_archive/DENGBR23.csv.gz",
    compression="gzip",
    chunksize=100_000
)

for chunk in chunks:
    print(chunk.shape)
```

---

# 🤖 Aplicações em Ciência de Dados

Este dataset pode ser utilizado em:

---

## 📊 Análise Exploratória

* Distribuição espacial
* Sazonalidade
* Séries temporais
* Correlação epidemiológica

---

## 🤖 Machine Learning

* Random Forest
* XGBoost
* CatBoost
* Árvores de decisão
* Regressão

---

## 🧠 Deep Learning

* Redes neurais
* LSTM
* Transformers
* Forecasting temporal

---

## 🌎 Geoprocessamento

* Heatmaps
* GIS
* GeoPandas
* Mapas epidemiológicos

---

## ☁️ Big Data

Compatível com:

* Apache Spark
* Dask
* Ray
* Polars
* DuckDB

---

# 🧪 Exemplo — Machine Learning

```python id="drrv7g"
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X = df.drop(columns=["CLASSI_FIN"])
y = df["CLASSI_FIN"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)
```

---

# 📈 Possíveis Pesquisas

* 🦟 Predição de surtos
* 🌎 Mapeamento epidemiológico
* 🧠 IA aplicada à saúde pública
* 📊 Estudos temporais
* 🏥 Vigilância epidemiológica
* 📈 Modelagem preditiva
* 📉 Análise de sazonalidade

---

# ⚠️ Observações Importantes

## 📌 Dados Públicos

Os dados são públicos e disponibilizados oficialmente pelo DATASUS.

---

## 📌 Dados Preliminares

Arquivos:

```text id="o04kek"
DENGBR25
DENGBR26
ZIKABR25
ZIKABR26
```

Podem sofrer:

* Atualizações
* Correções
* Consolidação posterior

---

## 📌 Volume de Dados

Os datasets podem ocupar vários GB de armazenamento.

Recomenda-se:

* SSD
* Ambientes cloud
* Leitura em chunks

---

# 🖥 Compatibilidade

✅ Windows
✅ Linux
✅ macOS
✅ WSL
✅ Google Colab
✅ Jupyter Notebook

---

# 📚 Bibliotecas Recomendadas

| Biblioteca   | Uso                  |
| ------------ | -------------------- |
| pandas       | Manipulação de dados |
| polars       | DataFrames rápidos   |
| dask         | Paralelismo          |
| pyarrow      | Apache Arrow         |
| geopandas    | Geoespacial          |
| scikit-learn | Machine Learning     |
| tensorflow   | Deep Learning        |
| xgboost      | Modelos preditivos   |

---

# 📜 Licença

Este repositório utiliza dados públicos do DATASUS.

Uso recomendado para:

✅ Pesquisa científica
✅ Estudos acadêmicos
✅ Ciência de Dados
✅ Saúde Pública
✅ Machine Learning

---

# ❤️ Agradecimentos

* 🇧🇷 Ministério da Saúde
* 🏛 DATASUS
* 📊 Comunidade Python
* 🧠 Comunidade Open Source

---

# ⭐ Contribua

Contribuições são bem-vindas:

* 🐛 Correções
* 🚀 Melhorias
* 📊 Novas análises
* ☁️ Integrações
* 🤖 IA aplicada

---

# ⭐ Se este projeto foi útil...

Deixe uma estrela no repositório ⭐
