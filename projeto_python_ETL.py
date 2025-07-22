import pandas as pd                  # Biblioteca para ler e manipular dados (como arquivos CSV)
import oracledb                      # Biblioteca para conectar e interagir com o banco Oracle

df = pd.read_csv("novos_funcionarios.csv")  # Lê o arquivo CSV e armazena em um DataFrame

# VALIDAÇÃO – Remove linhas com dados obrigatórios ausentes
colunas_obrigatorias = ["id", "nome", "salario", "setor"]  # Define as colunas obrigatórias
df = df.dropna(subset=colunas_obrigatorias)                # Remove linhas com dados ausentes nessas colunas

# Converte o ID para inteiro (garante que seja número e remove espaços)
df["id"] = df["id"].astype(str).str.strip().astype(int)

# TRANSFORMAÇÃO – Tratamento dos dados
df["nome"] = df["nome"].str.strip().str.title()    # Remove espaços e capitaliza os nomes (ex: maria silva → Maria Silva)

df["setor"] = df["setor"].str.upper()              # Converte o setor para caixa alta (ex: rh → RH)
df["setor"] = df["setor"].replace({                # Padroniza nomes diferentes para o mesmo setor
    "RECURSOS HUMANOS": "RH",
    "R.H.": "RH"
})

#df = df[df["salario"] >= 4000]                     # Filtra apenas quem ganha R$4000 ou mais

#print("\nMédia de salário e idade por setor:")
#print(df.groupby("setor")[["salario", "idade"]].mean().round(2))

# CONEXÃO COM O BANCO ORACLE
conn = oracledb.connect(                           # Estabelece a conexão com o banco
    user="RM558359",
    password="210396",
    dsn="oracle.fiap.com.br:1521/ORCL"
)

# BUSCA IDs JÁ EXISTENTES NO BANCO
cursor = conn.cursor()                             # Cria o cursor para executar comandos
cursor.execute("SELECT id FROM funcionarios")      # Busca todos os IDs da tabela funcionarios
ids_existentes = set(row[0] for row in cursor.fetchall())  # Cria um set com os IDs já existentes
cursor.close()                                     # Fecha o cursor

# FILTRA DADOS NOVOS (IDs que ainda não existem)
df_novos = df[~df["id"].isin(ids_existentes)]      # Mantém apenas os registros com ID novo

if df_novos.empty:                                 # Se não há registros novos
    print("Nenhum novo funcionário para inserir.")
    #print(df)                                      # Mostra o DataFrame já filtrado
else:
    cursor = conn.cursor()                         # Reabre o cursor para inserção
    sql_insert = """
    INSERT INTO funcionarios (id, nome, idade, cidade, salario, setor)
    VALUES (:1, :2, :3, :4, :5, :6)
    """
    data = [tuple(x) for x in df_novos.to_numpy()]  # Converte o DataFrame para lista de tuplas
    cursor.executemany(sql_insert, data)            # Executa os inserts em lote
    conn.commit()                                   # Confirma a transação no banco
    cursor.close()                                  # Fecha o cursor após inserir
    print(f"{len(df_novos)} novos funcionários inseridos.")
    #print(df)                                       # Exibe o DataFrame final

# EXPORTA OS DADOS PROCESSADOS PARA UM NOVO CSV
df.to_csv("funcionarios_processados.csv", index=False)
print("Arquivo 'funcionarios_processados.csv' gerado com sucesso.")

conn.close()                                        # Encerra a conexão com o banco