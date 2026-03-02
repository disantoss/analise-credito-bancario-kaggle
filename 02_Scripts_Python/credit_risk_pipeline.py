import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# ==========================================
# 1. CARREGAMENTO E TRADUÇÃO
# ==========================================
print("Iniciando processamento...")
df = pd.read_csv('credit_risk_dataset.csv')

traducao = {
    'person_age': 'idade',
    'person_income': 'renda_anual',
    'person_home_ownership': 'tipo_moradia',
    'person_emp_length': 'tempo_trabalho',
    'loan_intent': 'objetivo_emprestimo',
    'loan_grade': 'pontuacao_emprestimo',
    'loan_amnt': 'valor_emprestimo',
    'loan_int_rate': 'taxa_juros',
    'loan_status': 'status_inadimplencia',
    'loan_percent_income': 'percentual_renda_emprestimo',
    'cb_person_default_on_file': 'historico_inadimplencia',
    'cb_person_cred_hist_length': 'tempo_historico_credito'
}
df.rename(columns=traducao, inplace=True)

# ==========================================
# 2. LIMPEZA DE DADOS (DATA CLEANING)
# ==========================================
# Removendo inconsistências
df = df[df['idade'] <= 100]
df = df[df['tempo_trabalho'] <= 60]

# Tratando nulos com a mediana (estratégia sólida)
df['tempo_trabalho'] = df['tempo_trabalho'].fillna(df['tempo_trabalho'].median())
df['taxa_juros'] = df.groupby('pontuacao_emprestimo')['taxa_juros'].transform(lambda x: x.fillna(x.median()))

# ==========================================
# 3. FEATURE ENGINEERING & MODELAGEM
# ==========================================
# Criamos uma cópia para o modelo (o modelo precisa de números, o BI de texto)
df_model = df.copy()
colunas_categoricas = ['tipo_moradia', 'objetivo_emprestimo', 'pontuacao_emprestimo', 'historico_inadimplencia']

# Transformando texto em números para o modelo
le = LabelEncoder()
for col in colunas_categoricas:
    df_model[col] = le.fit_transform(df_model[col].astype(str))

# Definindo X (features) e y (target)
X = df_model.drop('status_inadimplencia', axis=1)
y = df_model['status_inadimplencia']

# Dividindo Treino e Teste (Stratify mantém a proporção de inadimplentes)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Treinando o Random Forest
modelo = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
modelo.fit(X_train, y_train)

# ==========================================
# 4. EXTRAÇÃO DE INSIGHTS (IMPORTÂNCIA)
# ==========================================
importancias = pd.DataFrame({
    'Variavel': X.columns,
    'Importancia': modelo.feature_importances_
}).sort_values(by='Importancia', ascending=False)

print("\n--- Top Variáveis que influenciam o Risco ---")
print(importancias)

# ==========================================
# 5. PREPARAÇÃO FINAL E EXPORTAÇÃO
# ==========================================
# Adicionando predições ao DataFrame original (que ainda tem os textos para o BI)
df['previsao_modelo'] = modelo.predict(X)
df['probabilidade_default_perc'] = (modelo.predict_proba(X)[:, 1] * 100).round(2)

# Exportando o arquivo principal para o Looker Studio
df.to_excel('dados_credito_looker.xlsx', index=False)

# Exportando as importâncias para um gráfico de barras no Looker
importancias.to_excel('importancia_variaveis.xlsx', index=False)

print("\nConcluído! Arquivos 'dados_credito_looker.xlsx' e 'importancia_variaveis.xlsx' gerados.")