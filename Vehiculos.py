# =============================================
#  CLASE BASE: Vehiculo
# =============================================

class Vehiculo:
    def __init__(self, marca: str, anio: int):
        self.__marca = marca
        self.__anio  = anio

    def consultar_marca(self) -> str:
        return self.__marca

    def consultar_anio(self) -> int:
        return self.__anio

    def __str__(self) -> str:
        return f"Marca: {self.__marca} | Año: {self.__anio}"


# =============================================
#  CLASE HIJA: Coche
# =============================================

class Coche(Vehiculo):
    def __init__(self, marca: str, anio: int, modelo: str):
        super().__init__(marca, anio)   # Reutiliza __init__ de Vehiculo
        self.__modelo = modelo

    def consultar_modelo(self) -> str:
        return self.__modelo

    def imprimir_modelo(self):
        print(f"  Modelo del coche: {self.__modelo}")

    def __str__(self) -> str:
        return super().__str__() + f" | Modelo: {self.__modelo}"


# =============================================
#  CREAR INSTANCIAS Y PROBAR
# =============================================

print("=" * 50)
print("         SISTEMA DE VEHICULOS")
print("=" * 50)

# --- Vehiculo ---
print("\n[ Objeto: Vehiculo ]")
v = Vehiculo("Toyota", 2018)
print(v)
print(f"  Marca: {v.consultar_marca()}")
print(f"  Año:   {v.consultar_anio()}")

# --- Coche ---
print("\n[ Objeto: Coche ]")
c = Coche("Honda", 2022, "Civic")
print(c)
print(f"  Marca:  {c.consultar_marca()}")    
print(f"  Año:    {c.consultar_anio()}")     
c.imprimir_modelo()                          

# --- Confirmar herencia ---
print("\n[ Confirmacion de herencia ]")
print(f"  ¿c es instancia de Coche?    {isinstance(c, Coche)}")
print(f"  ¿c es instancia de Vehiculo? {isinstance(c, Vehiculo)}")

print("\n" + "=" * 50)
