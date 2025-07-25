# 🔧 Desafio 1:
# Agrupar os funcionários por setor e mostrar a média salarial de cada setor.
# 🧠 Dica:
# Use .groupby('setor')['salario'].mean()

import pandas as pd

df = pd.read_csv("funcionarios.csv")

# Agrupar por setor e calcular a média salarial
media_salarial_por_setor = df.groupby('setor')['salario'].mean()

# Para remover a última linha (informativo adicional da series)
media_df = media_salarial_por_setor.reset_index()
#print(media_df)

# Agrupar por setor e contar quantos funcionários existem em cada um.
contagem_por_setor = df.groupby('setor').size().reset_index(name='quantidade')

# adicionei um titulo 'quantidade' para parar de entrar no .size
contagem_df = contagem_por_setor.reset_index()
#print(contagem_df)

# forma otimizada
# contagem_por_setor = df['setor'].value_counts()
# print(contagem_por_setor)


# Agrupar por setor e calcular a soma total dos salários por setor.
soma_salario_por_setor = df.groupby('setor')['salario'].sum()

# deixar em formato de DataFrame com uma coluna nomeada
salario_df = soma_salario_por_setor.reset_index(name='salário')
#print(salario_df)


# Agrupar por setor e exibir múltiplas estatísticas (como média, soma e contagem) para o salário.
agrupamento_por_setor = df.groupby('setor')['salario'].agg(['mean', 'sum', 'count'])
df_agrupamento = agrupamento_por_setor.reset_index()
df_agrupamento.columns = ['setor', 'media', 'soma', 'quantidade']
print (df_agrupamento)
