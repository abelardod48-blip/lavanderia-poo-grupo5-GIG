# Proyecto Final POO - Lavandería
# Grupo 5 - Paralelo vespertino GIG-S-VE-3-5
# Integrantes:
# - Cedeño Rosero Hillary Mery
# - Delgado Bajaña Bolivar Abelardo



from lavado_estandar import LavadoEstandar
from lavado_seco import LavadoSeco
from planchado import Planchado
from cliente import Cliente
from pedido import Pedido

print("===== LAVANDERÍA =====")

# 1. Creamos los servicios
estandar = LavadoEstandar()
seco = LavadoSeco(delicado=True)
planchado = Planchado()

# 2. Polimorfismo: recorremos una lista con servicios de distintas subclases
print("\n--- Servicios disponibles ---")
servicios = [estandar, seco, planchado]
for s in servicios:
    print(s.mostrar_info())

print("\n--- Cotización de ejemplo (cantidad 6 en todos) ---")
for s in servicios:
    costo = s.calcular_costo(6)
    tiempo = s.calcular_tiempo(6)
    print(f"{s.nombre}: ${costo:.2f} - {tiempo:.1f} horas")

# 3. Creamos un cliente y su pedido
print("\n--- Pedido de un cliente ---")
cliente1 = Cliente("María Torres", "0991234567")
pedido1 = Pedido(cliente1)
pedido1.agregar_servicio(estandar, 8)
pedido1.agregar_servicio(seco, 2)
pedido1.agregar_servicio(planchado, 5)
pedido1.mostrar_resumen()

# 4. Segundo pedido, solo planchado de 1 prenda (aplica el costo mínimo)
print("\n--- Segundo pedido ---")
cliente2 = Cliente("Luis Pérez", "0987654321")
pedido2 = Pedido(cliente2)
pedido2.agregar_servicio(Planchado(), 1)
pedido2.mostrar_resumen()

# 5. Probamos la validación de los setters
print("\n--- Prueba de validaciones ---")
try:
    estandar.precio_base = -5
except ValueError as e:
    print("Error:", e)

try:
    cliente1.telefono = "123"
except ValueError as e:
    print("Error:", e)
