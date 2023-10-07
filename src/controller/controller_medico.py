from model.medicos import Medico
from conexion.oracle_queries import OracleQueries

class Controller_Medico:
    def __init__(self):
        pass
        
    def inserir_medico(self) -> Medico:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo CNPJ
        cnpj = input("CNPJ (Novo): ")

        if self.verifica_existencia_medico(oracle, cnpj):
            # Solicita ao usuario a nova razão social
            razao_social = input("Razão Social (Novo): ")
            # Solicita ao usuario o novo nome fantasia
            nome_fantasia = input("Nome Fantasia (Novo): ")
            # Insere e persiste o novo medico
            oracle.write(f"insert into medicos values ('{cnpj}', '{razao_social}', '{nome_fantasia}')")
            # Recupera os dados do novo medico criado transformando em um DataFrame
            df_medico = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from medicos where cnpj = '{cnpj}'")
            # Cria um novo objeto medico
            novo_medico = Medico(df_medico.cnpj.values[0], df_medico.razao_social.values[0], df_medico.nome_fantasia.values[0])
            # Exibe os atributos do novo medico
            print(novo_medico.to_string())
            # Retorna o objeto novo_medico para utilização posterior, caso necessário
            return novo_medico
        else:
            print(f"O CNPJ {cnpj} já está cadastrado.")
            return None

    def atualizar_medico(self) -> Medico:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do medico a ser alterado
        cnpj = int(input("CNPJ do medico que deseja atualizar: "))

        # Verifica se o medico existe na base de dados
        if not self.verifica_existencia_medico(oracle, cnpj):
            # Solicita ao usuario a nova razão social
            razao_social = input("Razão Social (Novo): ")
            # Solicita ao usuario o novo nome fantasia
            nome_fantasia = input("Nome Fantasia (Novo): ")            
            # Atualiza o nome do medico existente
            oracle.write(f"update medicos set razao_social = '{razao_social}', nome_fantasia = '{nome_fantasia}'  where cnpj = {cnpj}")
            # Recupera os dados do novo medico criado transformando em um DataFrame
            df_medico = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from medicos where cnpj = {cnpj}")
            # Cria um novo objeto medico
            medico_atualizado = Medico(df_medico.cnpj.values[0], df_medico.razao_social.values[0], df_medico.nome_fantasia.values[0])
            # Exibe os atributos do novo medico
            print(medico_atualizado.to_string())
            # Retorna o objeto medico_atualizado para utilização posterior, caso necessário
            return medico_atualizado
        else:
            print(f"O CNPJ {cnpj} não existe.")
            return None

    def excluir_medico(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o CPF do medico a ser alterado
        cnpj = int(input("CNPJ do medico que irá excluir: "))        

        # Verifica se o medico existe na base de dados
        if not self.verifica_existencia_medico(oracle, cnpj):            
            # Recupera os dados do novo medico criado transformando em um DataFrame
            df_medico = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from medicos where cnpj = {cnpj}")
            # Revome o medico da tabela
            oracle.write(f"delete from medicos where cnpj = {cnpj}")            
            # Cria um novo objeto medico para informar que foi removido
            medico_excluido = Medico(df_medico.cnpj.values[0], df_medico.razao_social.values[0], df_medico.nome_fantasia.values[0])
            # Exibe os atributos do medico excluído
            print("medico Removido com Sucesso!")
            print(medico_excluido.to_string())
        else:
            print(f"O CNPJ {cnpj} não existe.")

    def verifica_existencia_medico(self, oracle:OracleQueries, cnpj:str=None) -> bool:
        # Recupera os dados do novo medico criado transformando em um DataFrame
        df_medico = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from medicos where cnpj = {cnpj}")
        return df_medico.empty