from pydoc import cli
from model.agendamentos import Agendamento
from model.clientes import Cliente
from controller.controller_cliente import Controller_Cliente
from model.fornecedores import Fornecedor
from controller.controller_fornecedor import Controller_Fornecedor
from conexion.oracle_queries import OracleQueries
from datetime import date

class Controller_Agendamento:
    def __init__(self):
        self.ctrl_cliente = Controller_Cliente()
        self.ctrl_fornecedor = Controller_Fornecedor()
        
    def inserir_agendamento(self) -> Agendamento:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        
        # Lista os clientes existentes para inserir no agendamento
        self.listar_clientes(oracle, need_connect=True)
        cpf = str(input("Digite o número do CPF do Cliente: "))
        cliente = self.valida_cliente(oracle, cpf)
        if cliente == None:
            return None

        # Lista os fornecedores existentes para inserir no agendamento
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
        data = dict(codigo=output_value, data_agendamento=data_hoje, cpf=cliente.get_CPF(), cnpj=fornecedor.get_CNPJ())
        # Executa o bloco PL/SQL anônimo para inserção do novo produto e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :codigo := AGENDAMENTOS_CODIGO_AGENDAMENTO_SEQ.NEXTVAL;
            insert into agendamentos values(:codigo, :data_agendamento, :cpf, :cnpj);
        end;
        """, data)
        # Recupera o código do novo produto
        codigo_agendamento = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_agendamento = oracle.sqlToDataFrame(f"select codigo_agendamento, data_agendamento from agendamentos where codigo_agendamento = {codigo_agendamento}")
        # Cria um novo objeto Produto
        novo_agendamento = Agendamento(df_agendamento.codigo_agendamento.values[0], df_agendamento.data_agendamento.values[0], cliente, fornecedor)
        # Exibe os atributos do novo produto
        print(novo_agendamento.to_string())
        # Retorna o objeto novo_agendamento para utilização posterior, caso necessário
        return novo_agendamento

    def atualizar_agendamento(self) -> Agendamento:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_agendamento = int(input("Código do Agendamento que irá alterar: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_agendamento(oracle, codigo_agendamento):

            # Lista os clientes existentes para inserir no agendamento
            self.listar_clientes(oracle)
            cpf = str(input("Digite o número do CPF do Cliente: "))
            cliente = self.valida_cliente(oracle, cpf)
            if cliente == None:
                return None

            # Lista os fornecedores existentes para inserir no agendamento
            self.listar_fornecedores(oracle)
            cnpj = str(input("Digite o número do CNPJ do Fornecedor: "))
            fornecedor = self.valida_fornecedor(oracle, cnpj)
            if fornecedor == None:
                return None

            data_hoje = date.today()

            # Atualiza a descrição do produto existente
            oracle.write(f"update agendamentos set cpf = '{cliente.get_CPF()}', cnpj = '{fornecedor.get_CNPJ()}', data_agendamento = to_date('{data_hoje}','yyyy-mm-dd') where codigo_agendamento = {codigo_agendamento}")
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_agendamento = oracle.sqlToDataFrame(f"select codigo_agendamento, data_agendamento from agendamentos where codigo_agendamento = {codigo_agendamento}")
            # Cria um novo objeto Produto
            agendamento_atualizado = Agendamento(df_agendamento.codigo_agendamento.values[0], df_agendamento.data_agendamento.values[0], cliente, fornecedor)
            # Exibe os atributos do novo produto
            print(agendamento_atualizado.to_string())
            # Retorna o objeto agendamento_atualizado para utilização posterior, caso necessário
            return agendamento_atualizado
        else:
            print(f"O código {codigo_agendamento} não existe.")
            return None

    def excluir_agendamento(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_agendamento = int(input("Código do Agendamento que irá excluir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_agendamento(oracle, codigo_agendamento):            
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_agendamento = oracle.sqlToDataFrame(f"select codigo_agendamento, data_agendamento, cpf, cnpj from agendamentos where codigo_agendamento = {codigo_agendamento}")
            cliente = self.valida_cliente(oracle, df_agendamento.cpf.values[0])
            fornecedor = self.valida_fornecedor(oracle, df_agendamento.cnpj.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir o agendamento {codigo_agendamento} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                print("Atenção, caso o agendamento possua itens, também serão excluídos!")
                opcao_excluir = input(f"Tem certeza que deseja excluir o agendamento {codigo_agendamento} [S ou N]: ")
                if opcao_excluir.lower() == "s":
                    # Revome o produto da tabela
                    oracle.write(f"delete from itens_agendamento where codigo_agendamento = {codigo_agendamento}")
                    print("Itens do agendamento removidos com sucesso!")
                    oracle.write(f"delete from agendamentos where codigo_agendamento = {codigo_agendamento}")
                    # Cria um novo objeto Produto para informar que foi removido
                    agendamento_excluido = Agendamento(df_agendamento.codigo_agendamento.values[0], df_agendamento.data_agendamento.values[0], cliente, fornecedor)
                    # Exibe os atributos do produto excluído
                    print("Agendamento Removido com Sucesso!")
                    print(agendamento_excluido.to_string())
        else:
            print(f"O código {codigo_agendamento} não existe.")

    def verifica_existencia_agendamento(self, oracle:OracleQueries, codigo:int=None) -> bool:
        # Recupera os dados do novo agendamento criado transformando em um DataFrame
        df_agendamento = oracle.sqlToDataFrame(f"select codigo_agendamento, data_agendamento from agendamentos where codigo_agendamento = {codigo}")
        return df_agendamento.empty

    def listar_clientes(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select c.cpf
                    , c.nome 
                from clientes c
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

    def valida_cliente(self, oracle:OracleQueries, cpf:str=None) -> Cliente:
        if self.ctrl_cliente.verifica_existencia_cliente(oracle, cpf):
            print(f"O CPF {cpf} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = {cpf}")
            # Cria um novo objeto cliente
            cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0])
            return cliente

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