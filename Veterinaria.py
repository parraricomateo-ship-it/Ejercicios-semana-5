# =============================================
#  CLASE BASE: Animal
# =============================================

class Animal:
    def __init__(self, nombre: str, especie: str):
        self.__nombre  = nombre
        self.__especie = especie

    def consultar_nombre(self) -> str:
        return self.__nombre

    def consultar_especie(self) -> str:
        return self.__especie

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} | Especie: {self.__especie}"


# =============================================
#  CLASE HIJA: Perro
# =============================================

class Perro(Animal):
    def __init__(self, nombre: str, especie: str, raza: str):
        super().__init__(nombre, especie)  # Reutiliza __init__ de Animal
        self.__raza = raza

    def consultar_raza(self) -> str:
        return self.__raza

    def imprimir_raza(self):
        print(f"  Raza del perro: {self.__raza}")

    def __str__(self) -> str:
        # Reutiliza el __str__ de Animal y agrega la raza
        return super().__str__() + f" | Raza: {self.__raza}"


# =============================================
#  CREAR INSTANCIAS Y PROBAR
# =============================================

print("=" * 50)
print("        CLINICA VETERINARIA")
print("=" * 50)

# --- Animal ---
print("\n[ Objeto: Animal ]")
a = Animal("Michi", "Gato")
print(a)
print(f"  Nombre:  {a.consultar_nombre()}")
print(f"  Especie: {a.consultar_especie()}")

# --- Perro ---
print("\n[ Objeto: Perro ]")
p = Perro("Max", "Perro", "Labrador")
print(p)
print(f"  Nombre:  {p.consultar_nombre()}")    # Heredado de Animal
print(f"  Especie: {p.consultar_especie()}")   # Heredado de Animal
p.imprimir_raza()                              # Propio de Perro

# --- Confirmar herencia ---
print("\n[ Confirmacion de herencia ]")
print(f"  ¿p es instancia de Perro?   {isinstance(p, Perro)}")
print(f"  ¿p es instancia de Animal?  {isinstance(p, Animal)}")

print("\n" + "=" * 50)
