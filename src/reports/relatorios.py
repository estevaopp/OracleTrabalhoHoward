from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_agendamentos.sql") as f:
            self.query_relatorio_agendamentos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_agendamentos_por_fornecedor.sql") as f:
            self.query_relatorio_agendamentos_por_fornecedor = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_clientes.sql") as f:
            self.query_relatorio_clientes = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_fornecedores.sql") as f:
            self.query_relatorio_fornecedores = f.read()

    def get_relatorio_agendamentos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_agendamentos))
        input("Pressione Enter para Sair do Relatório de Agendamentos")

    def get_relatorio_agendamentos_por_fornecedor(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_agendamentos_por_fornecedor))
        input("Pressione Enter para Sair do Relatório de Fornecedores")

    def get_relatorio_clientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        input("Pressione Enter para Sair do Relatório de Clientes")

    def get_relatorio_fornecedores(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_fornecedores))
        input("Pressione Enter para Sair do Relatório de Fornecedores")