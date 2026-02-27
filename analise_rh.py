"""
Análise de Salários e Profissões (RH Analytics)

"""

# 1. Importação das Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os # Biblioteca para gerenciar pastas/arquivos

# Configuração para melhorar a visualização dos gráficos no Spyder
sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# 2. Criação de um Banco de Dados Simulado
# Simulando uma tabela com observações (linhas) e variáveis (colunas)
# ---------------------------------------------------------
dados = {
    'ID': range(1, 21),
    'Idade': [25, 30, 22, 35, 45, 23, 33, 50, 27, 29, 
              40, 55, 21, 24, 34, 42, 31, 28, 48, 38],
    'Profissao': ['Analista', 'Gerente', 'Estagiário', 'Analista', 'Diretor', 
                  'Estagiário', 'Analista', 'Diretor', 'Analista', 'Analista',
                  'Gerente', 'Diretor', 'Estagiário', 'Estagiário', 'Analista',
                  'Gerente', 'Analista', 'Analista', 'Diretor', 'Gerente'],
    'Renda_Mensal': [3500, 8000, 1500, 4200, 15000, 1600, 4100, 18000, 3800, 3900,
                     8500, 20000, 1400, 1550, 4000, 8200, 3700, 3600, 16000, 7800],
    'Regiao': ['Sudeste', 'Sul', 'Sudeste', 'Nordeste', 'Sudeste', 
               'Sul', 'Sudeste', 'Sudeste', 'Nordeste', 'Centro-Oeste',
               'Sul', 'Sudeste', 'Nordeste', 'Sudeste', 'Sul',
               'Sudeste', 'Centro-Oeste', 'Nordeste', 'Sudeste', 'Sul']
}

# Criando o DataFrame (Tabela)
df = pd.DataFrame(dados)

print("--- Visualizando as primeiras linhas da base ---")
print(df.head())
print("\n")

# ---------------------------------------------------------
# 3. Análise de Variáveis Qualitativas / Categóricas
# Exemplo: Variável 'Regiao'
# ---------------------------------------------------------
print("--- Análise Descritiva: Variável Qualitativa (Região) ---")

# Frequência Absoluta (Contagem)
freq_absoluta = df['Regiao'].value_counts()
print("Frequência Absoluta:\n", freq_absoluta)

# Frequência Relativa (Porcentagem)
freq_relativa = df['Regiao'].value_counts(normalize=True) * 100
print("\nFrequência Relativa (%):\n", freq_relativa)

# Gráfico de Barras (Visualização)
plt.figure(figsize=(8, 5))
# Adicionei hue e legend=False para evitar warnings recentes do Seaborn
sns.countplot(x='Regiao', data=df, hue='Regiao', palette='viridis', legend=False)
plt.title('Distribuição dos Clientes por Região')
plt.ylabel('Contagem')
plt.savefig('images/distribuicao_regiao.png') # Salva a imagem
plt.show()

# ---------------------------------------------------------
# 4. Análise de Variáveis Quantitativas / Métricas
# Exemplo: Variável 'Renda_Mensal'
# ---------------------------------------------------------
print("\n--- Análise Descritiva: Variável Quantitativa (Renda Mensal) ---")

# Medidas de Posição
media = df['Renda_Mensal'].mean()
mediana = df['Renda_Mensal'].median()
primeiro_quartil = df['Renda_Mensal'].quantile(0.25)
terceiro_quartil = df['Renda_Mensal'].quantile(0.75)

print(f"Média: R$ {media:.2f}")
print(f"Mediana (2º Quartil): R$ {mediana:.2f}")
print(f"1º Quartil (25%): R$ {primeiro_quartil:.2f}")
print(f"3º Quartil (75%): R$ {terceiro_quartil:.2f}")

# Medidas de Dispersão
variancia = df['Renda_Mensal'].var()
desvio_padrao = df['Renda_Mensal'].std()

print(f"Variância: {variancia:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")

# Gráfico Histograma (Distribuição da Renda)
plt.figure(figsize=(8, 5))
sns.histplot(df['Renda_Mensal'], kde=True, color='blue')
plt.title('Histograma da Renda Mensal')
plt.xlabel('Renda (R$)')
plt.savefig('images/histograma_renda.png') # Salva a imagem
plt.show()

# Gráfico Boxplot (Para ver quartis e outliers)
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Renda_Mensal'], color='orange')
plt.title('Boxplot da Renda Mensal')
plt.xlabel('Renda (R$)')
plt.savefig('images/boxplot_renda.png') # Salva a imagem
plt.show()

# ---------------------------------------------------------
# 5. Correlação (Relação entre Idade e Renda)
# ---------------------------------------------------------
print("\n--- Matriz de Correlação ---")
print(df[['Idade', 'Renda_Mensal']].corr())

plt.figure(figsize=(8, 5))
sns.scatterplot(x='Idade', y='Renda_Mensal', data=df, hue='Profissao')
plt.title('Relação Idade vs Renda Mensal')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # Legenda para fora
plt.tight_layout() # Ajusta para não cortar a legenda
plt.savefig('images/scatter_idade_renda.png') # Salva a imagem
plt.show()


print("\n--- Processo Finalizado! As imagens foram salvas na pasta 'images' ---")
