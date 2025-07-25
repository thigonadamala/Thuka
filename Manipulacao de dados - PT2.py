# Desafio:
# Crie uma nova coluna chamada salario_liquido com 85% do salário original.
# Depois, remova a coluna salario_bonus.

import pandas as pd

# Carregar o CSV
df = pd.read_csv("funcionarios.csv")

# Ver as colunas
#print(df.columns)

# Criar nova coluna "salario_bonus" com 10% de bônus
df['salario_bonus'] = df['salario'] * 1.10

# Renomear a coluna 'setor' para 'departamento'
df.rename(columns={'setor': 'departamento'}, inplace=True)

# Remover a coluna 'idade'
df.drop(columns=['idade'], inplace=True)

# !Criar nova coluna "salario_liquido" com 85% do salário original
df['salario_liquido'] = df['salario'] * 0.85

# !Remover a coluna 'salário bonus'
df.drop(columns=['salario_bonus'], inplace=True)

print(df.head(3))