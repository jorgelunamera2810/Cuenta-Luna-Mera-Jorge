class Cuenta:

    def _init_(self, numero=None, nombrepropietario=None, saldo: float = 0):
        self._numero = numero
        self._nombrepropietario = nombrepropietario
        self._saldo = saldo

    def _str_(self):
        return f' Cuenta: {self._dict.str_()}'

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def nombrepropietario(self):
        return self._nombrepropietario

    @nombrepropietario.setter
    def nombrepropietario(self, nombrepropietario):
        self._nombrepropietario = nombrepropietario

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def credito(self, valor: float = 0):
        self._saldo = float(self._saldo) + float(valor)
        return self._saldo

    def debito(self, valor: float = 0):
        self._saldo = float(self._saldo) - float(valor)
        return self._saldo

    def mostrar_saldo(self):
        print(self._saldo)