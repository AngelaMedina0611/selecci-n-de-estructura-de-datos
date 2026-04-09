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
    # AGREGAR ENVÍO
    def agregar(self, codigo, cliente, estado):
        nuevo = Nodo(codigo, cliente, estado)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo
        nuevo.anterior = actual
