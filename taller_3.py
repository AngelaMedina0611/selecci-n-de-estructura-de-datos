class Nodo:
    def _init_(self, codigo, cliente, estado):
        self.codigo = codigo
        self.cliente = cliente
        self.estado = estado
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def _init_(self):
        self.cabeza = None