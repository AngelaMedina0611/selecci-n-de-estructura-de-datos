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
    
    # BUSCAR ENVÍO
    def buscar(self, codigo):
        actual = self.cabeza

        while actual:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente

        return None
    
    # ELIMINAR ENVÍO
    def eliminar(self, codigo):
        actual = self.cabeza

        while actual:
            if actual.codigo == codigo:

                # Caso: primer nodo
                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None

                else:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente:
                        actual.siguiente.anterior = actual.anterior

                print("Envío eliminado")
                return

            actual = actual.siguiente

        print("Envío no encontrado")

   # MOSTRAR NORMAL
    def mostrar(self):
        actual = self.cabeza

        if actual is None:
            print("Lista vacía")
            return

        while actual:
            print(f"Código: {actual.codigo} | Cliente: {actual.cliente} | Estado: {actual.estado}")
            actual = actual.siguiente
            
     # MOSTRAR INVERSO
    def mostrar_inverso(self):
        actual = self.cabeza

        if actual is None:
            print("Lista vacía")
            return

        # ir al final
        while actual.siguiente:
            actual = actual.siguiente

        # recorrer hacia atrás
        while actual:
            print(f"Código: {actual.codigo} | Cliente: {actual.cliente} | Estado: {actual.estado}")
            actual = actual.anterior
