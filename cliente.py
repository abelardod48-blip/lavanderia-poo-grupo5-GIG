# Grupo 5 - Paralelo vespertino GIG-S-VE-3-5
# Integrantes:
# - Cedeño Rosero Hillary Mery
# - Delgado Bajaña Bolivar Abelardo


class Cliente:
    def __init__(self, nombre, telefono):
        self._nombre = nombre
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not valor.isdigit() or len(valor) != 10:
            raise ValueError("El teléfono debe tener 10 dígitos")
        self._telefono = valor
if __name__ == "__main__":
    cliente = Cliente("María Torres", "0991234567")

    print("===== CLIENTE =====")
    print("Nombre:", cliente.nombre)
    print("Teléfono:", cliente.telefono)