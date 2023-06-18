

from Cuenta import Cuenta_corriente

class Cuenta_corriente (Cuenta_corriente):

    def _init_(self, numero= None, nombrepropietario= None, saldo:float= 0, tiene_cheque=bool):
        self._tiene_cheque= tiene_cheque
        super(Cuenta_corriente, self)._init_(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

    @property
    def tiene_cheque(self):
        return self._tiene_cheque

    @tiene_cheque.setter
    def tiene_cheque(self, tiene_cheque):
        self._tiene_cheque = tiene_cheque
        return self._saldo

    def pagar_cheque(self):
        self._saldo = self._saldo + ((float (self._saldo) - int (self._pagar_cheque)))
        return self._saldo

if _name_=='main_':
    Cuentas_corrientes = Cuenta_corriente('0925239139', 'jorge_luna', '123', bool)

    Cuentas_corrientes.mostrar_saldo()
    Cuentas_corrientes.credito(2500)

    Cuentas_corrientes.mostrar_saldo()
    Cuentas_corrientes.debito(100)

    print(Cuentas_corrientes)