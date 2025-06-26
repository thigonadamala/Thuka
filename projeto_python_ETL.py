import pandas as pd                  # Importa a biblioteca pandas para ler e manipular arquivos CSV
import oracledb                      # Importa a biblioteca oracledb para conectar ao banco Oracle

df = pd.read_csv("novos_funcionarios.csv")  # Lê o arquivo CSV e armazena em um DataFrame (tabela em memória)

# TRANSFORMAÇÃO
# Remover espaços extras e capitalizar nomes (ex: "  maria silva  " → "Maria Silva")
df["nome"] = df["nome"].str.strip().str.title()

# Padronizar setor para caixa alta e renomear algumas variações para "RH"
df["setor"] = df["setor"].str.upper()
df["setor"] = df["setor"].replace({
    "RECURSOS HUMANOS": "RH",
    "R.H.": "RH"
})

# Filtrar somente quem ganha a partir de R$4000
df = df[df["salario"] >= 4000]

# CONEXÃO COM O BANCO
conn = oracledb.connect(
    user="RM558359",
    password="210396",
    dsn="oracle.fiap.com.br:1521/ORCL"
)

# BUSCA IDs JÁ EXISTENTES NO BANCO
cursor = conn.cursor()
cursor.execute("SELECT id FROM funcionarios")
ids_existentes = set(row[0] for row in cursor.fetchall())
cursor.close()

# FILTRA DADOS NOVOS (IDs que ainda não existem)
df_novos = df[~df["id"].isin(ids_existentes)]

if df_novos.empty:
    print("Nenhum novo funcionário para inserir.")
    print(df)
else:
    cursor = conn.cursor()
    sql_insert = """
    INSERT INTO funcionarios (id, nome, idade, cidade, salario, setor)
    VALUES (:1, :2, :3, :4, :5, :6)
    """
    data = [tuple(x) for x in df_novos.to_numpy()]
    cursor.executemany(sql_insert, data)
    conn.commit()
    cursor.close()
    print(f"{len(df_novos)} novos funcionários inseridos.")
    print(df)

conn.close()