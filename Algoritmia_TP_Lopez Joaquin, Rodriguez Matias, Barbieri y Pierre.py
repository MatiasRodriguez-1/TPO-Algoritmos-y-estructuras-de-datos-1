import time

# ==================== DATOS INICIALES ==================== #
usuarios = [
    {"usuario": "admin", "clave": "1234", "rol": "admin"},
    {"usuario": "juan", "clave": "abcd", "rol": "cliente"}
]

# Estructura base de películas
peliculas = []

# ==================== ARCHIVO ==================== #
def cargar_peliculas_desde_archivo():
    """Carga las películas desde peliculas.txt si existe."""
    try:
        with open("peliculas.txt", "r") as archivo:
            for linea in archivo:
                nombre, genero, duracion = linea.strip().split(",")
                peliculas.append({
                    "nombre": nombre,
                    "genero": genero,
                    "duracion": int(duracion)
                })
        print("\nPelículas cargadas correctamente desde peliculas.txt")
    except FileNotFoundError:
        print("\nNo se encontró el archivo peliculas.txt. Se creará al guardar nuevas películas.")

def guardar_peliculas_en_archivo():
    """Guarda las películas en peliculas.txt."""
    with open("peliculas.txt", "w") as archivo:
        for p in peliculas:
            archivo.write(f"{p['nombre']},{p['genero']},{p['duracion']}\n")
    print("\nPelículas guardadas correctamente en peliculas.txt")

# ==================== FUNCIONES DE USUARIOS ==================== #
def login():
    print("\n=== Inicio de sesión ===")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    for u in usuarios:
        if u["usuario"] == usuario and u["clave"] == clave:
            print(f"\nBienvenido {usuario} ({u['rol']})")
            return u["rol"]
    print("\nUsuario o clave incorrectos.")
    return None

# ==================== FUNCIONES DE PELÍCULAS ==================== #
def agregar_pelicula():
    print("\n=== Agregar Película ===")
    nombre = input("Nombre: ")
    genero = input("Género: ")
    duracion = int(input("Duración (min): "))

    peliculas.append({
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion
    })
    guardar_peliculas_en_archivo()
    print(f"\nPelícula '{nombre}' agregada correctamente.")

def mostrar_peliculas():
    print("\n=== Cartelera de Películas ===")
    if not peliculas:
        print("No hay películas cargadas.")
        return
    for i, p in enumerate(peliculas, start=1):
        print(f"{i}. {p['nombre']} ({p['genero']}, {p['duracion']} min)")

# ==================== FUNCIONES DE REPORTES ==================== #
def reporte_peliculas():
    print("\n=== Reporte de Películas ===")
    if not peliculas:
        print("No hay películas para mostrar.")
        return

    # Uso de LAMBDA → ordenar por nombre de película
    peliculas_ordenadas = sorted(peliculas, key=lambda x: x["nombre"])

    print("\nPelículas ordenadas por nombre:")
    for p in peliculas_ordenadas:
        print(f"- {p['nombre']} ({p['genero']} - {p['duracion']} min)")

    print(f"\nTotal de películas: {len(peliculas_ordenadas)}")

# ==================== CONJUNTOS ==================== #
def demo_conjuntos():
    print("\n=== Ejemplo de uso de conjuntos ===")

    roles_existentes = {u["rol"] for u in usuarios}
    print("Roles existentes en el sistema:", roles_existentes)

    nombres_usuarios = {u["usuario"] for u in usuarios}
    nombres_usuarios.add("admin")

    print("Usuarios registrados (sin duplicados gracias al conjunto):", nombres_usuarios)
    print("Cantidad total de usuarios:", len(nombres_usuarios))
    print("Cantidad total de roles:", len(roles_existentes))

# ==================== MENÚ PRINCIPAL ==================== #
def menu_admin():
    while True:
        print("""
=== Menú Administrador ===
1. Agregar película
2. Mostrar cartelera
3. Reporte de películas
4. Demo de conjuntos
5. Salir
""")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_pelicula()
        elif opcion == "2":
            mostrar_peliculas()
        elif opcion == "3":
            reporte_peliculas()
        elif opcion == "4":
            demo_conjuntos()
        elif opcion == "5":
            print("\nCerrando sesión...")
            time.sleep(1)
            break
        else:
            print("Opción no válida.")

def menu_cliente():
    while True:
        print("""
=== Menú Cliente ===
1. Ver cartelera
2. Salir
""")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            mostrar_peliculas()
        elif opcion == "2":
            print("\nCerrando sesión...")
            time.sleep(1)
            break
        else:
            print("Opción no válida.")

# ==================== FUNCIÓN PRINCIPAL ==================== #
def main():
    cargar_peliculas_desde_archivo()
    while True:
        rol = login()
        if rol == "admin":
            menu_admin()
        elif rol == "cliente":
            menu_cliente()
        else:
            print("Intentá de nuevo.")
        continuar = input("\n¿Desea iniciar sesión nuevamente? (s/n): ")
        if continuar.lower() != "s":
            print("\nSaliendo del sistema...")
            break

# ==================== EJECUCIÓN ==================== #
if __name__ == "__main__":
    main()
