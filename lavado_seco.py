# Grupo 5 - Paralelo vespertino GIG-S-VE-3-5
# Integrantes:
# - Cedeño Rosero Hillary Mery
# - Delgado Bajaña Bolivar Abelardo

from servicio import Servicio


class LavadoSeco(Servicio):
    def __init__(self, precio_por_prenda=4.50, delicado=False):
        super().__init__("Lavado en seco", precio_por_prenda, 48)
        self._delicado = delicado

    @property
    def delicado(self):
        return self._delicado

    @delicado.setter
    def delicado(self, valor):
        self._delicado = valor

    def unidad(self):
        return "prendas"

    # se cobra por prenda, si es delicada tiene 20% de recargo
    def calcular_costo(self, cantidad):
        total = self._precio_base * cantidad
        if self._delicado:
            total = total * 1.20
        return total

    # normalmente 48 horas, las delicadas tardan 72
    def calcular_tiempo(self, cantidad):
        if self._delicado:
            return 72
        return self._tiempo_base
if __name__ == "__main__":
    lavado = LavadoSeco(delicado=True)
    cantidad = 6

    print("===== LAVADO EN SECO =====")
    print(lavado.mostrar_info())
    print("Cantidad:", cantidad, "prendas")
    print(f"Costo: ${lavado.calcular_costo(cantidad):.2f}")
    print("Tiempo:", lavado.calcular_tiempo(cantidad), "horas")