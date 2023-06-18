from Cuenta import Cuenta


class Cuenta_ahorro(Cuenta):
    def _init_(self, interes: float = 0, numero=None, nombrepropietario=None, saldo: float = 0):
        self._interes = interes
        super(Cuenta_ahorro, self)._init_(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

        @property
        def interes(self):
            return self._interes

        @interes.setter
        def interes(self, interes):
            self._interes = interes

        def pagar_interes(self):
            self._saldo = self._saldo + ((float(self._saldo) * int(self._interes)) / 100)
            return self._saldo


if _name_ == '_main_':
    Cuentas_ahorros = Cuenta_ahorro(3, '0925239139', 'jorge_luna', '123')

    Cuentas_ahorros.mostrar_saldo()
    Cuentas_ahorros.credito(2500)

    Cuentas_ahorros.mostrar_saldo()
    Cuentas_ahorros.debito(100)

    print(Cuentas_ahorros)
