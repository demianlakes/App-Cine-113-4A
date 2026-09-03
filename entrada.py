class Entrada:

    def __init__(self, numero, asiento):
        self.__numero = numero
        self.__asiento = asiento

    def mostrar_datos(self):
        print(f"Numero: {self.__numero} asiento: {self.__asiento}")

    def es_asiento_valido(self):
        pass