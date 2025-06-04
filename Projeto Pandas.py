import pandas as pd

margem = " " * 4  # Define uma margem para a exibição da aplicação

############################################################################
# # Criando uma Series a partir de uma lista
# s = pd.Series([1, 2, 3, 4, 5])

# # Acesso à posição de índice 4
# print(s[4]) # Saída: 5

# dados = {
#     "Produto": ["A", "B", "C"],
#     "Preço": [100, 200, 300],
#     "Quantidade": [10, 20, 30],
# }
# # Criando um DataFrame a partir de um dicionário
# df = pd.DataFrame(dados)

############################################################################
# # Acesso à coluna Produto
# coluna = df['Produto']
# # Acesso à múltiplas colunas
# colunas = df[['Produto', 'Preço']]
# # Acesso à primeira linha pelo rótulo
# linha = df.loc[0]
# # Acesso à primeira linha pela posição
# linha = df.iloc[0]
# # Acesso a um intervalo de linhas pela posição
# df.iloc[0:2]
# # Acesso a um único valor pela coluna e linha
# a = df['Produto'][0]
# print(a) # Saída: 'A'
# # Acesso a um único valor pela linha e coluna
# b = df.iloc[0]['Produto']
# print(b) # Saída: 'A'

############################################################################
# # Filtragem de dados com base em uma condição
# produtos_caros = df[df["Preço"] > 150]
# # Filtragem com múltiplas condições
# produtos_caros_quantidade_alta = df[(df["Preço"] > 150) & (df["Quantidade"] > 20)]

############################################################################
# Mostrando os dois resultados
# print(f"{margem}######### TABELA #########\n")
# print(margem + df.to_string(index=False))  # tira os índices se quiser

# print(f"\n{margem}Produtos com preço > 150:\n")
# print(margem + produtos_caros.to_string(index=False))

# print(f"\n{margem}Produtos com preço > 150 e quantidade > 20:\n")
# print(margem + produtos_caros_quantidade_alta.to_string(index=False))

############################################################################
# # Agregação de dados - soma total
# total_vendas = df['Preço'].sum()
# print(total_vendas) # Saída: 600
# # Agregação de dados - média
# media_precos = df['Preço'].mean()
# print(media_precos) # Saída: 200
# # Agregação de dados por grupo – gera uma tabela sumarizada
# vendas_por_produto = df.groupby('Produto').sum()

############################################################################
# DataFrame de produtos com 'ProdutoID' como índice
# import pandas as pd

# # Tabela de produtos
# df_produtos = pd.DataFrame({
#     'ProdutoID': [1, 2, 3],
#     'Nome': ['Prod A', 'Prod B', 'Prod C']
# })

# # Tabela de vendas (note que há um ProdutoID que não está na de produtos)
# df_vendas = pd.DataFrame({
#     'ProdutoID': [2, 3, 4],
#     'Quantidade': [5, 10, 8]
# })

# # INNER JOIN: só mantém o que tem em ambos
# print("INNER JOIN")
# print(pd.merge(df_vendas, df_produtos, on='ProdutoID', how='inner'))

# # LEFT JOIN: mantém tudo de df_vendas (esquerda)
# print("\nLEFT JOIN")
# print(pd.merge(df_vendas, df_produtos, on='ProdutoID', how='left'))

# # RIGHT JOIN: mantém tudo de df_produtos (direita)
# print("\nRIGHT JOIN")
# print(pd.merge(df_vendas, df_produtos, on='ProdutoID', how='right'))

# # OUTER JOIN: mantém tudo de ambos
# print("\nOUTER JOIN")
# print(pd.merge(df_vendas, df_produtos, on='ProdutoID', how='outer'))

############################################################################
# Escrevendo um DataFrame para um arquivo CSV
df.to_csv('dados.csv', sep=';', index=False)

# Lendo o arquivo CSV criado, para um novo DataFrame
df2 = pd.read_csv('dados.csv', sep=';')