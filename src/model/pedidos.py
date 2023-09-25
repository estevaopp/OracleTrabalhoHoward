from datetime import date
from model.clientes import Cliente

class Pedido:
    def __init__(self, 
                 codigo_pedido:int=None,
                 data_pedido:date=None,
                 cliente:Cliente= None
                 ):
        self.set_codigo_pedido(codigo_pedido)
        self.set_data_pedido(data_pedido)
        self.set_cliente(cliente)


    def set_codigo_pedido(self, codigo_pedido:int):
        self.codigo_pedido = codigo_pedido

    def set_data_pedido(self, data_pedido:date):
        self.data_pedido = data_pedido

    def set_cliente(self, cliente:Cliente):
        self.cliente = cliente

    def get_codigo_pedido(self) -> int:
        return self.codigo_pedido

    def get_data_pedido(self) -> date:
        return self.data_pedido

    def get_cliente(self) -> Cliente:
        return self.cliente

    def to_string(self) -> str:
        return f"Pedido: {self.get_codigo_pedido()} | Data: {self.get_data_pedido()} | Cliente: {self.get_cliente().get_nome()} | Fornecedor: {self.get_fornecedor().get_nome_fantasia()}"