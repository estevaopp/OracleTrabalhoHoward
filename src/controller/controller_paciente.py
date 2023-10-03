from model.paciente import Paciente
from conexion.oracle_queries import OracleQueries

class Controller_paciente:
    def __init__(self):
        pass
        
    def inserir_paciente(self) -> Paciente:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo CPF
        cpf = input("CPF (Novo): ")

        if self.verifica_existencia_paciente(oracle, cpf):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            # Insere e persiste o novo paciente
            oracle.write(f"insert into pacientes values ('{cpf}', '{nome}')")
            # Recupera os dados do novo paciente criado transformando em um DataFrame
            df_paciente = oracle.sqlToDataFrame(f"select cpf, nome from pacientes where cpf = '{cpf}'")
            # Cria um novo objeto paciente
            novo_paciente = Paciente(df_paciente.cpf.values[0], df_paciente.nome.values[0])
            # Exibe os atributos do novo paciente
            print(novo_paciente.to_string())
            # Retorna o objeto novo_paciente para utilização posterior, caso necessário
            return novo_paciente
        else:
            print(f"O CPF {cpf} já está cadastrado.")
            return None

    def atualizar_paciente(self) -> Paciente:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do paciente a ser alterado
        cpf = int(input("CPF do paciente que deseja alterar o nome: "))

        # Verifica se o paciente existe na base de dados
        if not self.verifica_existencia_paciente(oracle, cpf):
            # Solicita a nova descrição do paciente
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do paciente existente
            oracle.write(f"update pacientes set nome = '{novo_nome}' where cpf = {cpf}")
            # Recupera os dados do novo paciente criado transformando em um DataFrame
            df_paciente = oracle.sqlToDataFrame(f"select cpf, nome from pacientes where cpf = {cpf}")
            # Cria um novo objeto paciente
            paciente_atualizado = paciente(df_paciente.cpf.values[0], df_paciente.nome.values[0])
            # Exibe os atributos do novo paciente
            print(paciente_atualizado.to_string())
            # Retorna o objeto paciente_atualizado para utilização posterior, caso necessário
            return paciente_atualizado
        else:
            print(f"O CPF {cpf} não existe.")
            return None

    def excluir_paciente(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o CPF do paciente a ser alterado
        cpf = int(input("CPF do paciente que irá excluir: "))        

        # Verifica se o paciente existe na base de dados
        if not self.verifica_existencia_paciente(oracle, cpf):            
            # Recupera os dados do novo paciente criado transformando em um DataFrame
            df_paciente = oracle.sqlToDataFrame(f"select cpf, nome from pacientes where cpf = {cpf}")
            # Revome o paciente da tabela
            oracle.write(f"delete from pacientes where cpf = {cpf}")            
            # Cria um novo objeto paciente para informar que foi removido
            paciente_excluido = paciente(df_paciente.cpf.values[0], df_paciente.nome.values[0])
            # Exibe os atributos do paciente excluído
            print("paciente Removido com Sucesso!")
            print(paciente_excluido.to_string())
        else:
            print(f"O CPF {cpf} não existe.")

    def verifica_existencia_paciente(self, oracle:OracleQueries, cpf:str=None) -> bool:
        # Recupera os dados do novo paciente criado transformando em um DataFrame
        df_paciente = oracle.sqlToDataFrame(f"select cpf, nome from pacientes where cpf = {cpf}")
        return df_paciente.empty