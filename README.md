# 📊 Inteligência de Dados: Previsão de Risco de Crédito (Machine Learning)
### 🏦 Projeto de Portfólio | Análise de Inadimplência & Scoring

![Banner](https://img.shields.io/badge/Status-Finalizado-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Looker](https://img.shields.io/badge/Looker_Studio-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)

---

## 🔹 1. Dissertação sobre o Problema

### 🎯 O Desafio
A inadimplência é um dos maiores gargalos das instituições financeiras. O desafio deste projeto foi construir um motor de decisão capaz de prever se um solicitante de crédito irá atrasar o pagamento, minimizando o prejuízo do banco.

### 📈 Relevância Financeira
Prever o risco de inadimplência permite que instituições ofereçam taxas mais justas para bons pagadores e protejam seu capital contra perfis de alto risco. Este projeto simula um cenário real de **Credit Scoring**.

### 💡 A Solução via Dados
Utilizando **Machine Learning (Random Forest)**, processamos dados socioeconômicos para identificar padrões de comportamento. O modelo não apenas classifica o risco, mas quantifica a probabilidade de inadimplência por perfil de cliente.

---

## 🔹 2. Fontes de Dados
| Fonte | Tipo | Descrição |
| :--- | :--- | :--- |
| **Kaggle** | CSV | Dataset contendo 32k+ registros de clientes bancários |
| **Python Script** | XLSX | Dados limpos e processados com previsões do modelo |
| **Model Features** | XLSX | Ranking de importância das variáveis gerado pelo ML |

---

## 🔹 3. Pipeline de Dados (ETL & ML)

Utilizamos **Python** para construir um fluxo ponta a ponta:
* ✅ **Tratamento de Outliers:** Identificação e limpeza de dados bizarros (como idades acima de 120 anos).
* ✅ **Engenharia de Atributos:** Criação de métricas de comprometimento de renda e encoders para variáveis categóricas.
* ✅ **Modelagem:** Implementação do algoritmo **Random Forest** para prever o risco com alta precisão.
* ✅ **Exportação Automática:** Geração de arquivos prontos para consumo em ferramentas de BI.

---

## 🔹 4. 🧠 Relatório de Insights
> **Insight Principal:** O **Comprometimento da Renda** (Percentual da renda usado para o empréstimo) é o fator #1 na previsão de risco, superando até mesmo o histórico de crédito.

* 📍 **Perfil de Risco:** Clientes com renda comprometida acima de 30% apresentam taxas de default drasticamente maiores.
* 📍 **Nota de Crédito:** O modelo identificou que as grades de crédito (A, B, C...) estão bem calibradas, mas há oportunidades de otimização na Grade C.
* 📍 **Eficácia:** O modelo atingiu uma taxa de previsão alinhada com os dados reais da carteira (21.5%).

---

## 🔹 5. Visualização (Dashboard Interativo)

O Dashboard foi construído no **Looker Studio**, utilizando a identidade visual do **Kaggle** para proporcionar uma experiência executiva e técnica simultaneamente.

🚀 **[CLIQUE AQUI PARA ACESSAR O DASHBOARD INTERATIVO](https://lookerstudio.google.com/reporting/1531fc16-f459-4f33-90fc-f0e5469eb261)**

<img width="900" alt="image" src="https://github.com/user-attachments/assets/946983b6-0369-4481-9105-bea20cec1c21" />


---

## 🔹 6. Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Bibliotecas:** Pandas, Scikit-Learn, OpenPyXL
* **BI:** Google Looker Studio
* **Dataset Original:** Credit Risk Dataset (Kaggle)

---

## 📩 Contato
- **Nome:** Diego Santos
- **LinkedIn:** [https://www.linkedin.com/in/dados-disantos/](https://www.linkedin.com/in/dados-disantos/)
- **Email:** d.96leandro@gmail.com
