# Grupo 5 - Paralelo vespertino GIG-S-VE-3-5
# Integrantes:
# - Cedeño Rosero Hillary Mery
# - Delgado Bajaña Bolivar Abelardo


from servicio import Servicio


class LavadoEstandar(Servicio):
    def __init__(self, precio_por_kilo=1.25):
        super().__init__("Lavado estándar", precio_por_kilo, 3)
        self._kilos_minimo = 2

    @property
    def kilos_minimo(self):
        return self._kilos_minimo

    def unidad(self):
        return "kg"

    # se cobra por kilo, con un mínimo de 2 kg
    def calcular_costo(self, cantidad):
        if cantidad < self._kilos_minimo:
            cantidad = self._kilos_minimo
        return self._precio_base * cantidad

    # 3 horas y 1 hora más por cada 10 kg
    def calcular_tiempo(self, cantidad):
        return self._tiempo_base + (cantidad // 10)
if __name__ == "__main__":
    lavado = LavadoEstandar()
    cantidad = 6

    print("===== LAVADO ESTÁNDAR =====")
    print(lavado.mostrar_info())
    print("Cantidad:", cantidad, "kg")
    print(f"Costo: ${lavado.calcular_costo(cantidad):.2f}")
    print("Tiempo:", lavado.calcular_tiempo(cantidad), "horas")