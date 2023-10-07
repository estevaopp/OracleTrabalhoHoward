from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_agendamentos.sql") as f:
            self.query_relatorio_agendamentos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_agendamentos_por_medico.sql") as f:
            self.query_relatorio_agendamentos_por_medico = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_pacientes.sql") as f:
            self.query_relatorio_pacientes = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_medicos.sql") as f:
            self.query_relatorio_medicos = f.read()

    def get_relatorio_agendamentos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_agendamentos))
        input("Pressione Enter para Sair do Relatório de Agendamentos")

    def get_relatorio_agendamentos_por_medico(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_agendamentos_por_medico))
        input("Pressione Enter para Sair do Relatório de Medicos")

    def get_relatorio_pacientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_pacientes))
        input("Pressione Enter para Sair do Relatório de Pacientes")

    def get_relatorio_medicos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_medicos))
        input("Pressione Enter para Sair do Relatório de Medicos")