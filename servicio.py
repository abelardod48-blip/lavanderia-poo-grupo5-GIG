
# Clase base de la jerarquía. Todos los servicios de la lavandería
# heredan de aquí.
# Grupo 5 - Paralelo vespertino GIG-S-VE-3-5
# Integrantes:
# - Cedeño Rosero Hillary Mery
# - Delgado Bajaña Bolivar Abelardo


class Servicio:
    def __init__(self, nombre, precio_base, tiempo_base):
        self._nombre = nombre
        self._precio_base = precio_base
        self._tiempo_base = tiempo_base  # en horas

    # getters y setters con @property
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self._precio_base = valor

    @property
    def tiempo_base(self):
        return self._tiempo_base

    @tiempo_base.setter
    def tiempo_base(self, valor):
        if valor <= 0:
            raise ValueError("El tiempo debe ser mayor a 0")
        self._tiempo_base = valor

    # métodos que las subclases van a sobrescribir
    def unidad(self):
        return "unidades"

    def calcular_costo(self, cantidad):
        return self._precio_base * cantidad

    def calcular_tiempo(self, cantidad):
        return self._tiempo_base

    def mostrar_info(self):
        return f"{self._nombre} (precio base: ${self._precio_base:.2f}, se mide en {self.unidad()})"

if __name__ == "__main__":
    servicio = Servicio("Lavado básico", 2.00, 3)

    print("===== SERVICIO =====")
    print(servicio.mostrar_info())
    print("Costo: $", servicio.calcular_costo(5))
    print("Tiempo:", servicio.calcular_tiempo(5), "horas")