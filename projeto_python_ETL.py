import pandas as pd                  # Importa a biblioteca pandas para ler e manipular arquivos CSV
import oracledb                      # Importa a biblioteca oracledb para conectar ao banco Oracle

conn = oracledb.connect(             # Estabelece a conexão com o banco Oracle
    user="RM558359",                # Usuário do banco
    password="210396",             # Senha do banco
    dsn="oracle.fiap.com.br:1521/ORCL"  # Endereço e serviço do banco
)

df = pd.read_csv("novos_funcionarios.csv")  # Lê o arquivo CSV e armazena em um DataFrame (tabela em memória)

cursor = conn.cursor()             # Cria um cursor para executar comandos SQL no banco

sql_insert = """
INSERT INTO funcionarios (id, nome, idade, cidade, salario, setor)
VALUES (:1, :2, :3, :4, :5, :6)
"""

data = [tuple(x) for x in df.to_numpy()]  # Converte o DataFrame em uma lista de tuplas para inserção

cursor.executemany(sql_insert, data)  # Executa o comando SQL várias vezes (uma vez por linha do CSV)
conn.commit()                         # Confirma (salva) as alterações no banco
cursor.close()                        # Fecha o cursor
conn.close()                          # Fecha a conexão com o banco