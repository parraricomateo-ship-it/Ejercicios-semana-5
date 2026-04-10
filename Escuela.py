# =============================================
#  CLASE BASE: Persona
# =============================================

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad   = edad

    def consultar_nombre(self) -> str:
        return self.__nombre

    def consultar_edad(self) -> int:
        return self.__edad

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} | Edad: {self.__edad}"


# =============================================
#  CLASE HIJA: Estudiante
# =============================================

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, grado: str):
        super().__init__(nombre, edad)   # Reutiliza el __init__ de Persona
        self.__grado = grado

    def consultar_grado(self) -> str:
        return self.__grado

    def imprimir_grado(self):
        print(f"  Grado del estudiante: {self.__grado}")

    def __str__(self) -> str:
        # super().__str__() reutiliza el texto de Persona y le agrega el grado
        return super().__str__() + f" | Grado: {self.__grado}"


# =============================================
#  CREAR INSTANCIAS Y PROBAR
# =============================================

print("=" * 48)
print("         SISTEMA ESCOLAR")
print("=" * 48)

# --- Persona ---
print("\n[ Objeto: Persona ]")
p = Persona("Laura Torres", 35)
print(p)                            # Llama a __str__ de Persona
print(f"  Nombre: {p.consultar_nombre()}")
print(f"  Edad:   {p.consultar_edad()}")

# --- Estudiante ---
print("\n[ Objeto: Estudiante ]")
e = Estudiante("Carlos Ruiz", 14, "9no grado")
print(e)                            # Llama a __str__ de Estudiante
print(f"  Nombre: {e.consultar_nombre()}")   # Heredado de Persona
print(f"  Edad:   {e.consultar_edad()}")     # Heredado de Persona
e.imprimir_grado()                           # Propio de Estudiante

# --- Confirmar herencia ---
print("\n[ Confirmacion de herencia ]")
print(f"  ¿e es instancia de Estudiante? {isinstance(e, Estudiante)}")
print(f"  ¿e es instancia de Persona?    {isinstance(e, Persona)}")

print("\n" + "=" * 48)
