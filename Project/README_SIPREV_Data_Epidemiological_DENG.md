# 🦟 SIPREV — Sistema Inteligente de Previsão Epidemiológica de Dengue

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Status](https://img.shields.io/badge/Status-Experimental%20Acad%C3%AAmico-yellow)
![Dados](https://img.shields.io/badge/Dados-SINAN%2FDATASUS-green)
![Área](https://img.shields.io/badge/%C3%81rea-Ci%C3%AAncia%20dos%20Dados-purple)

## 📌 Visão geral

O **SIPREV — Sistema Inteligente de Previsão Epidemiológica de Dengue** é um pipeline analítico desenvolvido em Python/Jupyter para apoiar a análise, visualização, modelagem e previsão de dados epidemiológicos de dengue no Brasil, com foco especial em **Campo Grande/MS** e no estado de **Mato Grosso do Sul**.

O programa utiliza microdados públicos do **SINAN/DATASUS** no padrão `DENGBR15.csv` a `DENGBR26.csv`, correspondentes ao período de **2015 a 2026**, e executa um fluxo completo de Ciência dos Dados: carregamento em chunks, limpeza, enriquecimento, indicadores epidemiológicos, análise exploratória, visualizações, mapas, dashboards, modelos de Machine Learning, Deep Learning, séries temporais, interpretabilidade, relatórios acadêmicos e exportação final dos resultados.

> ⚠️ **Observação:** o arquivo enviado está no formato `.ipynb`, porém sua estrutura contém o programa completo em Python, podendo ser convertido para `.py` com `jupyter nbconvert --to script`.

---

## 🎯 Objetivo do projeto

Analisar a recorrência, incidência, gravidade, sazonalidade e tendência de casos de dengue em Campo Grande/MS, Mato Grosso do Sul e Brasil, utilizando técnicas de análise de dados, estatística, aprendizado de máquina e redes neurais para produzir relatórios, indicadores e artefatos visuais úteis ao acompanhamento epidemiológico.

### Objetivos específicos

- 📥 Carregar automaticamente os microdados de dengue do SINAN/DATASUS.
- 🧹 Realizar limpeza, padronização e enriquecimento dos dados.
- 📊 Calcular indicadores epidemiológicos anuais, mensais e semanais.
- 🗺️ Gerar mapas interativos para análise espacial.
- 📈 Produzir gráficos e dashboards em HTML.
- 🤖 Treinar modelos de Machine Learning para classificação, regressão, clusterização e detecção de anomalias.
- 🧠 Aplicar modelos de Deep Learning, incluindo LSTM, GRU, MLP, Autoencoder, TCN e Transformer temporal.
- 🔍 Aplicar interpretabilidade com SHAP.
- ⏳ Realizar previsão por séries temporais com ARIMA, Prophet, Holt-Winters e ensemble.
- 📝 Gerar relatórios técnicos, acadêmicos e arquivos consolidados para auditoria e reprodutibilidade.

---

## 🧾 Contexto acadêmico

| Item | Descrição |
|---|---|
| 🎓 Curso | Ciência dos Dados |
| 📚 Disciplina | Análise Organizacional e Soluções Tecnológicas |
| 🗓️ Semestre | 2026.1 |
| 📄 Módulo | Módulo 3 — Relatório Parcial da Ação de Extensão |
| 🦟 Tema | Dados epidemiológicos: recorrência/incidência de dengue em Campo Grande/MS |
| 🏥 Fonte | SINAN/DATASUS |
| 🌎 Recorte | Campo Grande/MS, Mato Grosso do Sul e Brasil |
| 📅 Período | 2015–2026 |

---

## 🗂️ Estrutura esperada do repositório

```text
.
├── SIPREV_Data_Epidemiological_DENG_v1_0.ipynb
├── SIPREV_Data_Epidemiological_DENG.py          # opcional, se convertido
├── README.md
├── input/
│   └── csv_archive/
│       ├── DENGBR15.csv
│       ├── DENGBR16.csv
│       ├── DENGBR17.csv
│       ├── DENGBR18.csv
│       ├── DENGBR19.csv
│       ├── DENGBR20.csv
│       ├── DENGBR21.csv
│       ├── DENGBR22.csv
│       ├── DENGBR23.csv
│       ├── DENGBR24.csv
│       ├── DENGBR25.csv
│       └── DENGBR26.csv
└── output/
    ├── graficos/
    ├── mapas/
    ├── dashboards/
    ├── relatorios/
    ├── modelos/
    └── dados/
```

O diretório `input/csv_archive/` armazena os arquivos CSV de entrada. O diretório `output/` é criado automaticamente pelo programa e concentra todos os resultados gerados.

---

## 🧬 Fonte dos dados

O sistema trabalha com os microdados públicos de dengue do **SINAN/DATASUS**, organizados por ano no padrão:

```text
DENGBR15.csv
DENGBR16.csv
DENGBR17.csv
...
DENGBR26.csv
```

O notebook também contém rotina para baixar os CSVs automaticamente a partir do repositório de dados:

```text
https://media.githubusercontent.com/media/OpenScienceTechnology/SINAN_DATASUS-DENG_ZIKA/refs/heads/main/Dataset/Dengue/csv_archive/
```

### Variáveis principais utilizadas

| Variável | Descrição |
|---|---|
| `TP_NOT` | Tipo de notificação |
| `ID_AGRAVO` | Agravo notificado, como dengue CID A90/A91 |
| `DT_NOTIFIC` | Data de notificação |
| `SEM_NOT` | Semana epidemiológica da notificação |
| `NU_ANO` | Ano da notificação |
| `SG_UF_NOT` | UF de notificação |
| `ID_MUNICIP` | Município de notificação |
| `DT_SIN_PRI` | Data dos primeiros sintomas |
| `SEM_PRI` | Semana epidemiológica dos primeiros sintomas |
| `NU_IDADE_N` | Idade codificada no padrão SINAN |
| `CS_SEXO` | Sexo do paciente |
| `CS_GESTANT` | Situação gestacional |
| `CS_RACA` | Raça/cor |
| `CS_ESCOL_N` | Escolaridade |
| `SG_UF` | UF de residência |
| `ID_MN_RESI` | Município de residência |
| `CLASSI_FIN` | Classificação final do caso |
| `CRITERIO` | Critério de confirmação |
| `EVOLUCAO` | Evolução do caso |
| `HOSPITALIZ` | Hospitalização |
| `SOROTIPO` | Sorotipo identificado |
| `DT_OBITO` | Data do óbito |
| `DT_ENCERRA` | Data de encerramento |

---

## 🧮 Indicadores calculados

O SIPREV calcula automaticamente indicadores epidemiológicos e estatísticos, como:

| Indicador | Fórmula/Descrição |
|---|---|
| 📈 Taxa de incidência | `(casos / população) × 100.000` |
| ⚰️ Taxa de letalidade | `(óbitos / casos confirmados) × 100` |
| 🏥 Taxa de mortalidade | `(óbitos / população) × 100.000` |
| 📊 Crescimento anual | `(valor atual - valor anterior) / valor anterior × 100` |
| 🧪 Casos confirmados | Classificação final 1, 2 ou 3 |
| 🚨 Casos graves | Dengue com sinais de alarme ou dengue grave |
| 🧭 Ranking municipal | Classificação dos municípios de MS por casos e taxas |
| 🌎 Ranking nacional | Comparação por UF brasileira |
| 🔁 Rt estimado | Razão aproximada entre janelas móveis de casos |
| 📉 Tendência temporal | Mann-Kendall, Sen's slope, ADF, ACF/PACF |

---

## 🧠 Técnicas implementadas

### 📊 Análise e estatística

- Análise exploratória de dados.
- Qualidade dos dados.
- Distribuições por ano, mês, semana epidemiológica, sexo, faixa etária, raça/cor, escolaridade e evolução.
- Análise de sazonalidade.
- Testes estatísticos, incluindo Qui-Quadrado e Mann-Kendall.
- Regressão de Poisson e Binomial Negativa.
- Análise de outliers por Z-score e IQR.
- Autocorrelação, ACF, PACF e teste ADF.

### 🤖 Machine Learning

- Random Forest.
- XGBoost.
- LightGBM.
- CatBoost.
- Decision Tree.
- Gradient Boosting.
- AdaBoost.
- Extra Trees.
- SVM/SVR.
- KNN.
- Naive Bayes.
- Regressão Linear, Ridge, Lasso e Logistic Regression.
- K-Means.
- DBSCAN.
- Cluster hierárquico.
- Isolation Forest.
- PCA e t-SNE.

### 🧠 Deep Learning e redes neurais

- LSTM.
- GRU.
- MLP.
- Autoencoder para anomalias.
- TCN — Temporal Convolutional Network.
- Transformer temporal com Multi-Head Attention.

### ⏳ Séries temporais

- ARIMA.
- Auto-ARIMA.
- SARIMAX.
- Holt-Winters.
- Prophet.
- NeuralProphet.
- Ensemble de previsão ponderado por erro.

### 🔍 Interpretabilidade

- SHAP com Random Forest.
- SHAP com XGBoost.
- SHAP com LightGBM.
- Análise de importância de variáveis.

---

## 🛠️ Tecnologias e bibliotecas

| Categoria | Bibliotecas |
|---|---|
| 🧮 Dados | `pandas`, `numpy`, `scipy` |
| 📊 Visualização | `matplotlib`, `seaborn`, `plotly` |
| 🗺️ Mapas | `folium`, `HeatMap`, `MarkerCluster` |
| 🤖 Machine Learning | `scikit-learn`, `xgboost`, `lightgbm`, `catboost` |
| 🧠 Deep Learning | `tensorflow`, `keras` |
| ⏳ Séries temporais | `statsmodels`, `pmdarima`, `prophet`, `neuralprophet` |
| 🔍 Interpretabilidade | `shap` |
| 📄 Relatórios | `fpdf2`, `texttable`, `openpyxl`, `xlsxwriter` |
| 💾 Dados otimizados | `pyarrow`, `fastparquet` |

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

### 2️⃣ Criar ambiente virtual

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
```

#### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3️⃣ Instalar dependências

```bash
pip install texttable folium plotly kaleido \
    xgboost lightgbm catboost shap \
    statsmodels pmdarima scikit-learn \
    fpdf2 openpyxl xlsxwriter \
    tensorflow keras prophet neuralprophet \
    pyarrow fastparquet pandas numpy scipy \
    matplotlib seaborn
```

Também é possível criar um `requirements.txt`:

```txt
pandas
numpy
scipy
matplotlib
seaborn
plotly
kaleido
folium
scikit-learn
xgboost
lightgbm
catboost
shap
statsmodels
pmdarima
prophet
neuralprophet
tensorflow
keras
texttable
fpdf2
openpyxl
xlsxwriter
pyarrow
fastparquet
```

E instalar com:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como executar

### ✅ Execução no Jupyter Notebook

Abra o notebook:

```bash
jupyter notebook SIPREV_Data_Epidemiological_DENG_v1_0.ipynb
```

Execute as células em ordem:

1. Instalação de dependências.
2. Configuração do ambiente.
3. Definição das funções e constantes.
4. Execução final com `main_max()`.

### ✅ Execução no Google Colab

1. Faça upload do notebook no Google Colab.
2. Ative GPU se for executar modelos de Deep Learning.
3. Execute todas as células em sequência.
4. O programa baixará automaticamente os CSVs, quando necessário.
5. Ao final, baixe o arquivo compactado `EpiAnalysis_DENG_*.zip`.

### ✅ Execução como script `.py`

Converta o notebook para script:

```bash
jupyter nbconvert --to script SIPREV_Data_Epidemiological_DENG_v1_0.ipynb
```

Depois execute:

```bash
python SIPREV_Data_Epidemiological_DENG_v1_0.py
```

### ✅ Execução modular

O programa permite chamar módulos específicos:

```python
from SIPREV_Data_Epidemiological_DENG import *

df = carregar_dados_ms()
df = preprocessar(df)
ind_cg = calcular_indicadores_cg(df)
graficos_cg(ind_cg, df[df["IS_CG"] == 1])
```

Listar módulos disponíveis:

```python
listar_modulos()
```

Executar um módulo específico:

```python
executar_modulo("mann_kendall", df)
executar_modulo("ensemble", df, horizonte=12)
executar_modulo("shap_rf", df)
```

---

## 🏗️ Fluxo do pipeline

```text
📥 Coleta/Download dos CSVs
        ↓
🧹 Limpeza e padronização
        ↓
🧬 Enriquecimento epidemiológico
        ↓
📊 Indicadores Campo Grande/MS
        ↓
🗺️ Rankings municipais e nacionais
        ↓
📈 Visualizações e mapas
        ↓
🤖 Machine Learning
        ↓
🧠 Deep Learning e redes neurais
        ↓
⏳ Séries temporais e previsão
        ↓
🔍 Interpretabilidade e validação
        ↓
📝 Relatórios, dashboards e ZIP final
```

---

## 📦 Principais funções

| Função | Finalidade |
|---|---|
| `main()` | Executa o pipeline básico |
| `main_completo()` | Executa pipeline expandido |
| `main_max()` | Executa o pipeline máximo com todos os módulos |
| `carregar_dados_ms()` | Carrega dados do SINAN/DATASUS filtrando MS |
| `preprocessar()` | Limpa, padroniza e enriquece os dados |
| `calcular_indicadores_cg()` | Calcula indicadores para Campo Grande/MS |
| `calcular_indicadores_ms()` | Calcula ranking municipal de MS |
| `calcular_indicadores_nacionais()` | Calcula indicadores por UF brasileira |
| `graficos_cg()` | Gera gráficos de Campo Grande/MS |
| `mapa_calor_cg()` | Gera mapa de calor de Campo Grande/MS |
| `modelos_classificacao()` | Treina modelos de classificação |
| `modelo_regressao_incidencia()` | Treina modelos de regressão de incidência |
| `modelo_lstm()` | Treina rede neural LSTM |
| `modelo_gru()` | Treina rede neural GRU |
| `modelo_transformer_temporal()` | Treina modelo Transformer temporal |
| `modelo_arima()` | Executa previsão ARIMA/Auto-ARIMA |
| `modelo_prophet()` | Executa previsão com Prophet |
| `ensemble_previsao()` | Combina previsões em ensemble |
| `shap_random_forest()` | Gera interpretabilidade SHAP para Random Forest |
| `exportar_dados_processados()` | Exporta CSV, Parquet e XLSX |
| `exportar_zip()` | Compacta todos os resultados |
| `validar_programa()` | Audita ambiente, arquivos e dependências |

---

## 📁 Saídas geradas

Ao final da execução, o sistema cria automaticamente a pasta `output/` com múltiplos artefatos.

```text
output/
├── graficos/
│   ├── cg_casos_anuais.png
│   ├── cg_heatmap_sazonal.png
│   ├── cg_piramide_etaria_geral.png
│   ├── cg_curva_epidemica_semanal.png
│   ├── cg_rt_efetivo.png
│   ├── cg_ensemble_previsao.png
│   ├── shap_rf_beeswarm.png
│   ├── shap_xgb_barras.png
│   ├── pca_epidemiologico.png
│   └── ...
├── mapas/
│   ├── mapa_calor_campo_grande.html
│   ├── mapa_municipios_ms_interativo.html
│   ├── mapa_estados_brasil_interativo.html
│   └── mapa_bairros_campo_grande.html
├── dashboards/
│   ├── dashboard_principal.html
│   ├── dashboard_curva_epidemica.html
│   ├── dashboard_perfil_demografico.html
│   ├── dashboard_cg_temporal.html
│   ├── dashboard_cg_perfil.html
│   ├── dashboard_ms_municipal.html
│   └── dashboard_nacional.html
├── relatorios/
│   ├── execucao_YYYYMMDD_HHMMSS.log
│   ├── relatorio_final_YYYYMMDD_HHMMSS.txt
│   ├── relatorio_final_YYYYMMDD_HHMMSS.pdf
│   ├── relatorio_saude_publica_narrativo.txt
│   ├── relatorio_academico_modulo3.txt
│   └── relatorio_dengue_YYYYMMDD_HHMMSS.xlsx
├── dados/
│   ├── campo_grande_tratado.csv
│   ├── campo_grande_tratado.parquet
│   ├── ms_completo_tratado.csv
│   ├── ranking_municipal_ms.csv
│   ├── ranking_nacional_estados.csv
│   ├── cg_indicadores_anuais.csv
│   ├── SIPREV_Dados_Consolidados.xlsx
│   └── metadados_YYYYMMDD_HHMMSS.json
└── modelos/
```

Também é gerado um arquivo compactado:

```text
EpiAnalysis_DENG_YYYYMMDD_HHMMSS.zip
```

---

## 🗺️ Recorte geográfico

| Localidade | Código |
|---|---:|
| Campo Grande/MS | `500270` no padrão SINAN de 6 dígitos |
| Campo Grande/MS | `5002704` no padrão IBGE de 7 dígitos |
| Mato Grosso do Sul | UF `50` |

O programa prioriza o campo `ID_MN_RESI`, isto é, o **município de residência**, para calcular taxas e rankings epidemiológicos.

---

## 🧪 Classificação epidemiológica

O sistema considera como casos confirmados as classificações finais:

| Código | Classificação |
|---:|---|
| 1 | Dengue |
| 2 | Dengue com sinais de alarme |
| 3 | Dengue grave |

Casos descartados ou inconclusivos são tratados separadamente em análises de qualidade, encerramento e critério de confirmação.

---

## 🚨 Sistema de alerta epidemiológico

O SIPREV implementa classificação de alerta por percentis históricos e por taxa de incidência:

| Nível | Interpretação |
|---|---|
| 🟢 Verde | Atividade mínima/baixa |
| 🟡 Amarelo | Atenção ou atividade moderada |
| 🟠 Laranja | Risco elevado ou aumento incomum |
| 🔴 Vermelho | Situação crítica/surto potencial |

Além disso, utiliza parâmetros epidemiológicos configuráveis, como janela de média móvel, limiares de incidência, Rt estimado e thresholds de risco.

---

## 🔐 Ética, privacidade e limitações

Este projeto utiliza dados públicos, agregáveis e de interesse epidemiológico. Mesmo assim, recomenda-se:

- Não divulgar dados individualizados sensíveis.
- Trabalhar preferencialmente com dados agregados por ano, município, faixa etária ou semana epidemiológica.
- Utilizar os resultados como apoio analítico, e não como diagnóstico clínico.
- Validar conclusões com especialistas em epidemiologia, vigilância em saúde e políticas públicas.
- Considerar que dados de anos recentes, especialmente 2026, podem estar incompletos ou sujeitos a atualização.

> 🏥 O sistema não substitui análises oficiais de vigilância epidemiológica nem decisões técnicas das autoridades de saúde.

---

## ⚠️ Limitações técnicas

- O último ano disponível pode conter dados parciais.
- A qualidade das previsões depende da completude dos arquivos SINAN/DATASUS.
- Algumas análises ambientais são simuladas quando não há integração direta com bases climáticas.
- Modelos de Deep Learning podem exigir GPU para melhor desempenho.
- Arquivos grandes podem demandar mais memória RAM; o programa usa leitura em chunks para reduzir esse problema.
- Determinadas bibliotecas, como `prophet`, `tensorflow` e `neuralprophet`, podem ter instalação mais demorada em ambientes novos.

---

## 🧰 Recomendações para grandes volumes de dados

Para bases muito grandes, recomenda-se:

- Usar ambiente com pelo menos 16 GB de RAM.
- Aumentar ou reduzir `chunk_size` conforme memória disponível.
- Exportar dados processados em Parquet.
- Usar Google Colab Pro, Vertex AI Workbench, GitHub Codespaces ou ambiente local com SSD.
- Evitar abrir CSVs grandes diretamente em editores de planilha.
- Usar `DuckDB`, `Polars` ou `PySpark` em versões futuras do pipeline.

---

## 🧾 Metadados do projeto

| Campo | Valor |
|---|---|
| Nome | SIPREV — Sistema Inteligente de Previsão Epidemiológica de Dengue |
| Versão | 1.0.0 |
| Linguagem | Python |
| Ambiente | Jupyter Notebook, Google Colab, Google Cloud Shell, ambiente local |
| Fonte | SINAN/DATASUS |
| Período | 2015–2026 |
| Área | Ciência dos Dados aplicada à Saúde Pública |
| Foco | Campo Grande/MS, Mato Grosso do Sul e Brasil |

---

## 📚 Glossário rápido

| Termo | Significado |
|---|---|
| SINAN | Sistema de Informação de Agravos de Notificação |
| DATASUS | Departamento de Informática do Sistema Único de Saúde |
| Dengue A90/A91 | Códigos CID associados à dengue |
| SE | Semana epidemiológica |
| Rt | Número de reprodução efetivo |
| ACF/PACF | Funções de autocorrelação |
| ARIMA | Modelo autoregressivo integrado de médias móveis |
| Prophet | Biblioteca de previsão de séries temporais |
| SHAP | Técnica de explicação de modelos baseada em valores de Shapley |
| LSTM/GRU | Redes neurais recorrentes para sequências temporais |
| TCN | Rede convolucional temporal |
| PCA | Análise de Componentes Principais |
| t-SNE | Técnica de redução de dimensionalidade para visualização |

---

## 🤝 Como contribuir

Contribuições são bem-vindas! Algumas possibilidades:

1. Abrir uma issue descrevendo erro, melhoria ou nova funcionalidade.
2. Criar uma branch para a alteração.
3. Testar o notebook/script com dados reais.
4. Submeter um pull request com descrição clara.

Sugestões de melhorias futuras:

- Integração com dados climáticos reais do INMET.
- Integração com LIRAa, CNES e indicadores socioeconômicos.
- Uso de DuckDB/Polars para maior desempenho.
- Deploy de dashboard web com Streamlit ou Dash.
- Automatização do pipeline com GitHub Actions.
- Monitoramento contínuo de atualizações do DATASUS.

---

## 📜 Licença

Este projeto pode ser distribuído sob a licença **MIT**, desde que mantidos os devidos créditos aos autores, fontes de dados e instituições relacionadas.

> Caso o repositório utilize outra licença, substitua esta seção pelo arquivo `LICENSE` correspondente.

---

## 👨‍💻 Autor/Responsável

**Projeto acadêmico:** SIPREV — Sistema Inteligente de Previsão Epidemiológica de Dengue  
**Área:** Ciência dos Dados aplicada à Saúde Pública  
**Fonte de dados:** SINAN/DATASUS  
**Recorte:** Campo Grande/MS — Mato Grosso do Sul — Brasil  

---

## ⭐ Citação sugerida

```text
SIPREV — Sistema Inteligente de Previsão Epidemiológica de Dengue. Pipeline em Python/Jupyter para análise, visualização e previsão de dados epidemiológicos de dengue com base em microdados SINAN/DATASUS, 2015–2026. Campo Grande/MS: Ciência dos Dados, 2026.
```

Em formato ABNT simplificado:

```text
SIPREV. Sistema Inteligente de Previsão Epidemiológica de Dengue: análise de dados SINAN/DATASUS 2015–2026. Campo Grande/MS, 2026. Disponível em: repositório GitHub do projeto. Acesso em: dia mês ano.
```

---

## ✅ Status do projeto

🚧 **Status:** versão acadêmica funcional, com pipeline completo em notebook.  
📌 **Versão:** `v1.0.0`  
🧪 **Uso recomendado:** pesquisa acadêmica, análise exploratória, apoio didático e prototipação em Ciência dos Dados aplicada à saúde pública.

