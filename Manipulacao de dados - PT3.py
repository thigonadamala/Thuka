# 🧪 Desafio prático:
# Filtre todos os funcionários do Financeiro que ganham mais de 6000
# Salve esse resultado num novo DataFrame chamado financeiro_acima_6k
# Exiba esse novo DataFrame com print()

import pandas as pd

df = pd.read_csv("funcionarios.csv")

# Filtrar funcionários do setor de Tecnologia
filtro_tecnologia = df[df['setor'] == 'Tecnologia']
print("Setor Tecnologia:")
print(filtro_tecnologia)

# Filtrar funcionários com salário acima de 6000
filtro_salario = df[df['salario'] > 6000]
print("\nSalário acima de 6000:")
print(filtro_salario)

# Filtrar quem trabalha no Marketing e ganha mais de 5000
filtro_composto = df[(df['setor'] == 'Marketing') & (df['salario'] > 5000)]
print("\nMarketing com salário > 5000:")
print(filtro_composto)

# !Filtrar quem trabalha no Financeiro e ganha mais de 6000 e salve esse resultado num novo DataFrame chamado financeiro_acima_6k

financeiro_acima_6k = df[(df['setor'] == 'Financeiro') & (df['salario'] > 6000)]
print("\Financeiro com salário > 6000:")
print(financeiro_acima_6k)


