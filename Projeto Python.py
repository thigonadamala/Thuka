# Importação dos módulos
import os
import oracledb
import pandas as pd

# Try para tentativa de Conexão com o Banco de Dados
try:
    # Efetua a conexão com o Usuário no servidor
    conn = oracledb.connect(
        user="RM558359", password="210396", dsn="oracle.fiap.com.br:1521/ORCL"
    )
    # Cria as instruções para cada módulo
    inst_cadastro = conn.cursor()  # insert
    inst_consulta = conn.cursor()  # select
    inst_alteracao = conn.cursor()  # updade
    inst_exclusao = conn.cursor()  # delete
except Exception as e:
    # Informa o erro
    print("Erro: ", e)
    # Flag para não executar a Aplicação
    conexao = False
else:
    # Flag para executar a Aplicação
    conexao = True

margem = " " * 4  # Define uma margem para a exibição da aplicação

# Enquanto o flag conexao estiver apontado com True
while conexao:
    os.system("cls")  # Limpa a tela no início do loop

    # Apresenta o menu
    print("------- CRUD - PETSHOP -------")
    print(
        """
    1 - Cadastrar Pet
    2 - Listar Pets
    3 - Alterar Pet
    4 - Excluir Pet
    5 - EXCLUIR TODOS OS PETS
    6 - SAIR
    """
    )

    # Captura a escolha do usuário
    escolha = input(margem + "Escolha -> ")

    # Verifica se o número digitado é um valor numérico
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        print("Você deve digitar um número de 1 a 6.\nReiniciando a Aplicação!")
        input("\nPressione ENTER para continuar...")

    # VERIFICA QUAL A ESCOLHA DO USUÁRIO
    match escolha:

        # CADASTRAR UM PET
        case 1:
            try:
                print("----- CADASTRAR PET -----\n")
                tipo = input(margem + "Digite o tipo....: ")
                nome = input(margem + "Digite o nome....: ")
                idade = int(input(margem + "Digite a idade...: "))

                # Instrução SQL segura
                cadastro = "INSERT INTO petshop (tipo_pet, nome_pet, idade) VALUES (:1, :2, :3)"
                inst_cadastro.execute(cadastro, (tipo, nome, idade))
                conn.commit()

            except ValueError:
                print("Digite um número na idade!")

            except Exception as e:
                print("Erro na transação do BD:", e)

            else:
                print("\n##### Dados GRAVADOS #####")
                input("\nPressione ENTER para continuar...")

        # LISTAR OS PETS
        case 2:
            print("----- LISTAR PETs -----\n")

            # Usando pandas diretamente para fazer a consulta SQL e ordenando por ID
            dados_df = pd.read_sql("SELECT * FROM petshop ORDER BY id", conn)

            # Verifica se não há dados
            if dados_df.empty:
                print("Não há Pets cadastrados!")
            else:
                print(dados_df)  # Exibe os dados do DataFrame

            print("\nLISTADOS!")
            input("\nPressione ENTER para continuar...")

        # ALTERANDO UM REGISTRO
        case 3:
            try:
                print("----- ALTERAR DADOS DO PET -----\n")

                lista_dados = []  # Lista para captura de dados da tabela

                # Permite o usuário escolher um Pet pelo id
                pet_id = int(input(margem + "Escolha um ID: "))

                # Constrói a instrução de consulta para verificar a existência do ID
                consulta = "SELECT * FROM petshop WHERE id = :1"
                inst_consulta.execute(consulta, (pet_id,))
                data = (
                    inst_consulta.fetchone()
                )  # Usando fetchone para um único resultado (menos uso de memória)

                # Se o pet não for encontrado, avisa o usuário
                if data is None:
                    print(f"Não há um pet cadastrado com o ID = {pet_id}")
                    input("\nPressione ENTER para continuar...")
                else:
                    # Captura os novos dados
                    novo_tipo = input(margem + "Digite um novo tipo: ")
                    novo_nome = input(margem + "Digite um novo nome: ")
                    nova_idade = input(margem + "Digite uma nova idade: ")

                    # Constrói a instrução de edição do registro com os novos dados
                    alteracao = """
                        UPDATE petshop
                        SET tipo_pet = :1, nome_pet = :2, idade = :3
                        WHERE id = :4
                    """

                    try:
                        # Executa a atualização no banco de dados
                        inst_alteracao.execute(
                            alteracao, (novo_tipo, novo_nome, nova_idade, pet_id)
                        )
                        conn.commit()  # Confirma a transação no banco
                        print("\n##### Dados ATUALIZADOS! #####")
                    except oracledb.DatabaseError as db_error:
                        print(
                            "Erro de banco de dados ao tentar atualizar o pet:",
                            db_error,
                        )
                    except Exception as e:
                        print(f"Erro inesperado ao tentar atualizar o pet: {e}")

            except ValueError:
                print("ID ou idade inválidos. Por favor, insira um valor numérico.")
            except Exception as e:
                print(f"Erro ao tentar processar a alteração: {e}")

        # EXCLUIR UM REGISTRO
        case 4:
            print("----- EXCLUIR PET -----\n")
            try:
                pet_id = input(margem + "Escolha um ID: ")

                if not pet_id.isdigit():
                    print("O ID deve ser numérico.")
                    input("\nPressione ENTER para continuar...")
                    break

                pet_id = int(pet_id)

                # Consulta se o ID existe
                consulta = "SELECT * FROM petshop WHERE id = :1"
                inst_consulta.execute(consulta, (pet_id,))
                data = inst_consulta.fetchone()

                if data is None:
                    print(f"Não há um pet cadastrado com o ID = {pet_id}")
                    input("\nPressione ENTER para continuar...")
                else:
                    # Executa exclusão com segurança
                    exclusao = "DELETE FROM petshop WHERE id = :1"
                    try:
                        inst_exclusao.execute(exclusao, (pet_id,))
                        conn.commit()
                        print("\n##### Pet APAGADO! #####")
                    except oracledb.DatabaseError as db_error:
                        print("Erro ao excluir o pet:", db_error)
                    except Exception as e:
                        print(f"Erro inesperado na exclusão: {e}")

            except Exception as e:
                print(f"Erro ao processar a exclusão: {e}")

        # EXCLUIR TODOS OS REGISTROS
        case 5:
            print("\n!!!!! EXCLUIR TODOS OS DADOS DA TABELA !!!!!\n")
            confirma = input(
                margem + "CONFIRMA A EXCLUSÃO DE TODOS OS PETS? [S]im ou [N]ão: "
            )

            if confirma.strip().upper() == "S":
                try:
                    # Apaga todos os registros da tabela
                    exclusao = "DELETE FROM petshop"
                    inst_exclusao.execute(exclusao)
                    conn.commit()

                    # Reseta o contador de ID
                    reset_id = "ALTER TABLE petshop MODIFY(ID GENERATED AS IDENTITY (START WITH 1))"
                    inst_exclusao.execute(reset_id)
                    conn.commit()

                    print("##### Todos os registros foram excluídos! #####")

                except oracledb.DatabaseError as db_error:
                    print("Erro ao excluir os registros do banco de dados:", db_error)
                except Exception as e:
                    print(f"Erro inesperado ao excluir todos os registros: {e}")
            else:
                print(margem + "Operação cancelada pelo usuário.")
                input("\nPressione ENTER para continuar...")

        # SAI DA APLICAÇÃO
        case 6:
            print(margem + "Você desconectou!")
            conexao = False

        # CASO O NUMERO DIGITADO NÃO SEJA UM DO MENU
        case _:
            print(
                margem
                + "Erro! Você digitou um número inválido. Digite um número entre 1 e 6."
            )

            # Pausa o fluxo da aplicação para a leitura das informações
            input("\nPressione ENTER para continuar...")
# Encerra aplicação
else:
    print("Obrigado por utilizar a nossa aplicação!")