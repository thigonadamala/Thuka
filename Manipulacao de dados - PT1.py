#AQUI EU GEREI UM CSV COM NOMES IDADES E SALÁRIO
import pandas as pd

df = pd.read_csv("clientes.csv")

filtro = df[df['idade'] > 30]

print("Clientes que possuem mais de 30 anos:")
print(filtro.head(5))

media = filtro['salario'].mean()
print(f"Média dos salários de quem tem mais de 30 anos: {media}")

# Salvar como CSV (padrão) ".csv"
filtro.to_csv('clientes_maiores_30.csv', index=False)