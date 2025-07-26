import pandas as pd
import oracledb

conn = oracledb.connect(
     user="system",
     password="oracle123",
     dsn="localhost:1521/FREE"
)
cursor = conn.cursor()

df = pd.read_csv("novos_funcionarios_docker.csv")

colunas_obrigatorias = ["id", "nome", "idade", "cidade", "salario", "setor"]
df = df.dropna(subset=colunas_obrigatorias)

data = [tuple(x) for x in df.to_numpy()]

print(df)