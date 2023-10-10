class Medico:
    def __init__(self, 
                 CRM:str=None,
                 nome:str=None
                 ):
        self.set_CRM(CRM)
        self.set_nome(nome)

    def set_CRM(self, CRM:str):
        self.CRM = CRM

    def set_nome(self, nome:str):
        self.nome = nome

    def get_CRM(self) -> str:
        return self.CRM

    def get_nome(self) -> str:
        return self.nome

    def to_string(self) -> str:
        return f"CRM: {self.get_CRM()} | Nome: {self.get_nome()}"