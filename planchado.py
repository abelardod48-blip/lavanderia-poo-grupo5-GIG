# Grupo 5 - Paralelo vespertino GIG-S-VE-3-5
# Integrantes:
# - Cedeño Rosero Hillary Mery
# - Delgado Bajaña Bolivar Abelardo


from servicio import Servicio


class Planchado(Servicio):
    def __init__(self, precio_por_prenda=0.75):
        super().__init__("Planchado", precio_por_prenda, 1)
        self._costo_minimo = 2.00

    @property
    def costo_minimo(self):
        return self._costo_minimo

    def unidad(self):
        return "prendas"

    # por prenda, pero el servicio tiene un costo mínimo de $2.00
    def calcular_costo(self, cantidad):
        total = self._precio_base * cantidad
        if total < self._costo_minimo:
            total = self._costo_minimo
        return total

    # 1 hora más 6 minutos por prenda
    def calcular_tiempo(self, cantidad):
        return self._tiempo_base + cantidad * 0.1
if __name__ == "__main__":
    planchado = Planchado()
    cantidad = 5

    print("===== PLANCHADO =====")
    print(planchado.mostrar_info())
    print("Cantidad:", cantidad, "prendas")
    print(f"Costo: ${planchado.calcular_costo(cantidad):.2f}")
    print("Tiempo:", planchado.calcular_tiempo(cantidad), "horas")