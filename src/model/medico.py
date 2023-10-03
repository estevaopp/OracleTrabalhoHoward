from datetime import date
from model.paciente import Paciente

class Medico:
    def __init__(self, 
                 codigo_medico:int=None,
                 data_medico:date=None,
                 paciente:Paciente= None
                 ):
        self.set_codigo_medico(codigo_medico)
        self.set_data_medico(data_medico)
        self.set_paciente(paciente)


    def set_codigo_medico(self, codigo_medico:int):
        self.codigo_medico = codigo_medico

    def set_data_medico(self, data_medico:date):
        self.data_medico = data_medico

    def set_paciente(self, paciente:Paciente):
        self.paciente = paciente

    def get_codigo_medico(self) -> int:
        return self.codigo_medico

    def get_data_medico(self) -> date:
        return self.data_medico

    def get_paciente(self) -> Paciente:
        return self.paciente

    def to_string(self) -> str:
        return f"Medico: {self.get_codigo_medico()} | Data: {self.get_data_medico()} | Paciente: {self.get_paciente().get_nome()} | Fornecedor: {self.get_fornecedor().get_nome_fantasia()}"