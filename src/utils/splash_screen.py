from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_pacientes = config.QUERY_COUNT.format(tabela="pacientes")
        self.qry_total_medicos = config.QUERY_COUNT.format(tabela="medicos")
        self.qry_total_agendamentos = config.QUERY_COUNT.format(tabela="agendamentos")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Estêvão Paulo Pereira, Dyana Luiz Oliveira, João Guilherme Pigatto da Silva, José Henrique Bessi Wolkers, Matheus Barros Barreto e Karolini Prando de Mattos"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_pacientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_pacientes)["total_pacientes"].values[0]

    def get_total_medicos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_medicos)["total_medicos"].values[0]

    def get_total_agendamentos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_agendamentos)["total_agendamentos"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PACIENTES:         {str(self.get_total_pacientes()).rjust(5)}
        #      2 - MEDICOS:     {str(self.get_total_medicos()).rjust(5)}
        #      3 - AGENDAMENTOS:          {str(self.get_total_agendamentos()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """