# Grupo 5 - Paralelo vespertino GIG-S-VE-3-5
# Integrantes:
# - Cedeño Rosero Hillary Mery
# - Delgado Bajaña Bolivar Abelardo


class Pedido:
    def __init__(self, cliente):
        self._cliente = cliente
        self._items = []  # lista de (servicio, cantidad)

    @property
    def cliente(self):
        return self._cliente

    @property
    def items(self):
        return self._items

    def agregar_servicio(self, servicio, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        self._items.append((servicio, cantidad))

    # aquí se usa el polimorfismo: cada servicio calcula a su manera
    def calcular_total(self):
        total = 0
        for servicio, cantidad in self._items:
            total += servicio.calcular_costo(cantidad)
        return total

    # el pedido está listo cuando termina el servicio que más demora
    def calcular_tiempo_entrega(self):
        tiempos = []
        for servicio, cantidad in self._items:
            tiempos.append(servicio.calcular_tiempo(cantidad))
        return max(tiempos)

    def mostrar_resumen(self):
        print(f"Cliente: {self._cliente.nombre} - Tel: {self._cliente.telefono}")
        for servicio, cantidad in self._items:
            costo = servicio.calcular_costo(cantidad)
            print(f"  {servicio.nombre}: {cantidad} {servicio.unidad()} -> ${costo:.2f}")
        print(f"Total a pagar: ${self.calcular_total():.2f}")
        print(f"Tiempo de entrega: {self.calcular_tiempo_entrega():.1f} horas")
if __name__ == "__main__":
    from cliente import Cliente
    from lavado_estandar import LavadoEstandar
    from lavado_seco import LavadoSeco
    from planchado import Planchado

    cliente = Cliente("María Torres", "0991234567")
    pedido = Pedido(cliente)

    pedido.agregar_servicio(LavadoEstandar(), 8)
    pedido.agregar_servicio(LavadoSeco(delicado=True), 2)
    pedido.agregar_servicio(Planchado(), 5)

    print("===== PEDIDO =====")
    pedido.mostrar_resumen()