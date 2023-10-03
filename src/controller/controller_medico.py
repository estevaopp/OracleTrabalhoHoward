from pydoc import cli
from model.medico import Medico
from model.paciente import Paciente
from controller.controller_paciente import Controller_Paciente
from model.fornecedores import Fornecedor
from controller.controller_fornecedor import Controller_Fornecedor
from conexion.oracle_queries import OracleQueries
from datetime import date

class Controller_Medico:
    def __init__(self):
        self.ctrl_paciente = Controller_Paciente()
        self.ctrl_fornecedor = Controller_Fornecedor()
        
    def inserir_medico(self) -> Medico:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        
        # Lista os pacientes existentes para inserir no medico
        self.listar_pacientes(oracle, need_connect=True)
        cpf = str(input("Digite o número do CPF do Paciente: "))
        paciente = self.valida_paciente(oracle, cpf)
        if paciente == None:
            return None

        # Lista os fornecedores existentes para inserir no medico
        self.listar_fornecedores(oracle, need_connect=True)
        cnpj = str(input("Digite o número do CNPJ do Fornecedor: "))
        fornecedor = self.valida_fornecedor(oracle, cnpj)
        if fornecedor == None:
            return None

        data_hoje = date.today()

        # Recupera o cursos para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(codigo=output_value, data_medico=data_hoje, cpf=paciente.get_CPF(), cnpj=fornecedor.get_CNPJ())
        # Executa o bloco PL/SQL anônimo para inserção do novo produto e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :codigo := MEDICOS_CODIGO_MEDICO_SEQ.NEXTVAL;
            insert into medicos values(:codigo, :data_medico, :cpf, :cnpj);
        end;
        """, data)
        # Recupera o código do novo produto
        codigo_medico = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_medico = oracle.sqlToDataFrame(f"select codigo_medico, data_medico from medicos where codigo_medico = {codigo_medico}")
        # Cria um novo objeto Produto
        novo_medico = Medico(df_medico.codigo_medico.values[0], df_medico.data_medico.values[0], paciente, fornecedor)
        # Exibe os atributos do novo produto
        print(novo_medico.to_string())
        # Retorna o objeto novo_medico para utilização posterior, caso necessário
        return novo_medico

    def atualizar_medico(self) -> Medico:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_medico = int(input("Código do Medico que irá alterar: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_medico(oracle, codigo_medico):

            # Lista os pacientes existentes para inserir no medico
            self.listar_pacientes(oracle)
            cpf = str(input("Digite o número do CPF do Paciente: "))
            paciente = self.valida_paciente(oracle, cpf)
            if paciente == None:
                return None

            # Lista os fornecedores existentes para inserir no medico
            self.listar_fornecedores(oracle)
            cnpj = str(input("Digite o número do CNPJ do Fornecedor: "))
            fornecedor = self.valida_fornecedor(oracle, cnpj)
            if fornecedor == None:
                return None

            data_hoje = date.today()

            # Atualiza a descrição do produto existente
            oracle.write(f"update medicos set cpf = '{paciente.get_CPF()}', cnpj = '{fornecedor.get_CNPJ()}', data_medico = to_date('{data_hoje}','yyyy-mm-dd') where codigo_medico = {codigo_medico}")
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_medico = oracle.sqlToDataFrame(f"select codigo_medico, data_medico from medicos where codigo_medico = {codigo_medico}")
            # Cria um novo objeto Produto
            medico_atualizado = Medico(df_medico.codigo_medico.values[0], df_medico.data_medico.values[0], paciente, fornecedor)
            # Exibe os atributos do novo produto
            print(medico_atualizado.to_string())
            # Retorna o objeto medico_atualizado para utilização posterior, caso necessário
            return medico_atualizado
        else:
            print(f"O código {codigo_medico} não existe.")
            return None

    def excluir_medico(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_medico = int(input("Código do Medico que irá excluir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_medico(oracle, codigo_medico):            
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_medico = oracle.sqlToDataFrame(f"select codigo_medico, data_medico, cpf, cnpj from medicos where codigo_medico = {codigo_medico}")
            paciente = self.valida_paciente(oracle, df_medico.cpf.values[0])
            fornecedor = self.valida_fornecedor(oracle, df_medico.cnpj.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir o medico {codigo_medico} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                print("Atenção, caso o medico possua itens, também serão excluídos!")
                opcao_excluir = input(f"Tem certeza que deseja excluir o medico {codigo_medico} [S ou N]: ")
                if opcao_excluir.lower() == "s":
                    # Revome o produto da tabela
                    oracle.write(f"delete from itens_medico where codigo_medico = {codigo_medico}")
                    print("Itens do medico removidos com sucesso!")
                    oracle.write(f"delete from medicos where codigo_medico = {codigo_medico}")
                    # Cria um novo objeto Produto para informar que foi removido
                    medico_excluido = Medico(df_medico.codigo_medico.values[0], df_medico.data_medico.values[0], paciente, fornecedor)
                    # Exibe os atributos do produto excluído
                    print("Medico Removido com Sucesso!")
                    print(medico_excluido.to_string())
        else:
            print(f"O código {codigo_medico} não existe.")

    def verifica_existencia_medico(self, oracle:OracleQueries, codigo:int=None) -> bool:
        # Recupera os dados do novo medico criado transformando em um DataFrame
        df_medico = oracle.sqlToDataFrame(f"select codigo_medico, data_medico from medicos where codigo_medico = {codigo}")
        return df_medico.empty

    def listar_pacientes(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select c.cpf
                    , c.nome 
                from pacientes c
                order by c.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def listar_fornecedores(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select f.cnpj
                    , f.razao_social
                    , f.nome_fantasia
                from fornecedores f
                order by f.nome_fantasia
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_paciente(self, oracle:OracleQueries, cpf:str=None) -> Paciente:
        if self.ctrl_paciente.verifica_existencia_paciente(oracle, cpf):
            print(f"O CPF {cpf} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo paciente criado transformando em um DataFrame
            df_paciente = oracle.sqlToDataFrame(f"select cpf, nome from pacientes where cpf = {cpf}")
            # Cria um novo objeto paciente
            paciente = Paciente(df_paciente.cpf.values[0], df_paciente.nome.values[0])
            return paciente

    def valida_fornecedor(self, oracle:OracleQueries, cnpj:str=None) -> Fornecedor:
        if self.ctrl_fornecedor.verifica_existencia_fornecedor(oracle, cnpj):
            print(f"O CNPJ {cnpj} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo fornecedor criado transformando em um DataFrame
            df_fornecedor = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from fornecedores where cnpj = {cnpj}")
            # Cria um novo objeto fornecedor
            fornecedor = Fornecedor(df_fornecedor.cnpj.values[0], df_fornecedor.razao_social.values[0], df_fornecedor.nome_fantasia.values[0])
            return fornecedor