from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_medicos.sql") as f:
            self.query_relatorio_medicos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_medicos_por_fornecedor.sql") as f:
            self.query_relatorio_medicos_por_fornecedor = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_pacientes.sql") as f:
            self.query_relatorio_pacientes = f.read()

    def get_relatorio_medicos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_medicos))
        input("Pressione Enter para Sair do Relatório de Medicos")

    def get_relatorio_medicos_por_fornecedor(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_medicos_por_fornecedor))
        input("Pressione Enter para Sair do Relatório de Fornecedores")

    def get_relatorio_pacientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_pacientes))
        input("Pressione Enter para Sair do Relatório de Pacientes")
