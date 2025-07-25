import pandas as pd
import oracledb

conn = oracledb.connect(
     user="system",
     password="oracle123",
     dsn="localhost:1521/FREE"
)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM funcionarios")
print(cursor.fetchone())