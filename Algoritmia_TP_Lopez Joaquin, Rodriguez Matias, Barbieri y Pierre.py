import time
import os
# ==================== DATOS INICIALES ==================== #
usuarios = [{"usuario": "admin", "contraseña": "admin", "rol": "Admin"}]
# Estructura base de películas
peliculas = []
archivoBase = os.path.dirname(__file__)
archivoUsuarios = os.path.join(archivoBase,"usuarios.txt")
archivoPeliculas = os.path.join(archivoBase,"peliculas.txt")

# ==================== ARCHIVO ==================== #
def cargar_Usarios_desde_archivo():
    try:
        archivo = open(archivoUsuarios, "r", encoding="utf-8")
        for linea in archivo:
            if linea != "\n":
                partes = linea.split(",")
                if len(partes) == 3:
                    usuario = partes[0]
                    contraseña = partes[1]
                    rol = partes[2].replace("\n", "")
                    usuarios.append({"usuario": usuario, "contraseña": contraseña, "rol": rol})
        archivo.close()
        print("Archivo 'usuarios.txt' leído correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará vacío.")
        archivo = open(archivoUsuarios, "a", encoding="utf-8")
        archivo.close()
    
def cargar_peliculas_desde_archivo():
    """
    Objetivo: cargar la lista peliculas utilizando la informacion almacenada en archivos
    """
    peliculas.clear()
    try:
        with open(archivoPeliculas, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")

                titulo = partes[0]
                fecha = partes[1]
                horario = partes[2]
                precio = int(partes[3])
                recaudacion = int(partes[4])

                asientosTexto = partes[5:]  # Los valores restantes

                asientos = []
                for a in asientosTexto:
                    if a == "False":
                        asientos.append(False)
                    else:
                        asientos.append(a)

                peliculas.append({
                    "titulo": titulo,
                    "fecha": fecha,
                    "horario": horario,
                    "precio": precio,
                    "recaudacion": recaudacion,
                    "asientos": asientos
                })

        print("\nPelículas cargadas correctamente.")

    except FileNotFoundError:
        print("\nNo se encontró el archivo peliculas.txt. Se creará al guardar nuevas películas.")
        
def guardar_peliculas_en_archivo():
    """
    Objetivo: Almacenar la informacion de la lista de peliculas en un archivo de texto
    """
    with open(archivoPeliculas, "w", encoding="utf-8") as archivo:
        for p in peliculas:
            linea = f"{p['titulo']},{p['fecha']},{p['horario']},{p['precio']},{p['recaudacion']}"
            for asiento in p["asientos"]:
                if asiento == False:
                    linea += ",False"
                else:
                    linea += f",{asiento}"

            archivo.write(linea + "\n")

    print("Películas (incluyendo asientos) guardadas correctamente en peliculas.txt")


# ==================== FUNCIONES DE USUARIOS ==================== #
def login():
    print("=== Sistema de Login ===")
    print("1) Ingresar con usuario")
    print("2) Entrar como Guest")
    print("3) Registrar Usuario")

    try:
        opcion = int(input("Seleccione opción: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return None, None

    while opcion not in [1, 2, 3]:
        try:
            opcion = int(input("Seleccione opción (1-3): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return None, None

    if opcion == 2:
        return "Guest", "Invitado"

    elif opcion == 3:
        registrarUsuario()
        return login()

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    usuario_valido = None
    for u in usuarios:
        if u["usuario"] == usuario and u["contraseña"] == contraseña:
            usuario_valido = u


    if usuario_valido:
        print(f"Bienvenido {usuario_valido['usuario']} (rol: {usuario_valido['rol']})")
        return usuario_valido["rol"], usuario_valido["usuario"]
    else:
        print("Credenciales inválidas")
        return None, None

def registrarUsuario():
    """
    Objetivo: La creacion de nuevos usuarios y su agregacion a la lista de usuarios
    """
    print("=== Registrar Nuevo Usuario ===")
    nombre_valido = False
    while not nombre_valido:
        usuario = input("Nuevo usuario: ").strip()
        existe = False
        for u in usuarios:
            if u["usuario"] == usuario:
                existe = True
        if existe:
            print("Ese nombre de usuario ya existe. Elegí otro.")
        elif usuario == "":
            print("El nombre de usuario no puede ser dejado en blanco")
        else:
            nombre_valido = True

    print("La contraseña debe tener al menos 8 caracteres, una mayúscula y un número.")
    contraseña_valida = False
    while not contraseña_valida:
        contraseña = input("Contraseña: ").strip()
        tiene_mayus = False
        for ch in contraseña:
            if ch.isupper():
                tiene_mayus = True
        tiene_numero = False
        for ch in contraseña:
            if ch.isdigit():
                tiene_numero = True
        cumple_formato = (len(contraseña) >= 8 and tiene_mayus and tiene_numero)

        if cumple_formato:
            verificacion = input("Ingrese la contraseña nuevamente: ")
            if verificacion == contraseña:
                contraseña_valida = True
            else:
                print("La contraseña debe ser la misma")
                print("Vuelva a ingresar la contraseña")
        else:
            print("La contraseña no cumple los requisitos.")
        
    usuarios.append({"usuario": usuario, "contraseña": contraseña, "rol": "User"})
    with open(archivoUsuarios, "a", encoding="utf-8") as archivo:
        archivo.write(f"{usuario},{contraseña},User\n")
    print("Usuario creado con éxito.")

# ------------------ FUNCIONES UTILITARIAS ------------------ #
def limpiarPantalla():
    """
    Objetivo: Simular la limpieza de la pantalla utilizando 100 saltos de linea
    """
    for i in range(100):
        print("\n")

def contar(n):
    """
    Entrada: la cantidad de tiempo a esperar
    Objetivo: Hacer un tiempo de espera para darle mas importancia al cierre de sesion y finalizacion del programa
    """
    if n<=0:
        limpiarPantalla()
        return
    print(n)
    time.sleep(1)
    contar(n-1)

# ------------------ FUNCIONES DE CINE ------------------ #
def mostrarCartelera(peliculas):
    """
    Entradas: la lista de las peliculas
    Objetivo: que el usuario pueda ver la cartelera de forma sencilla
    """
    print("-------------------------------------------")
    if len(peliculas) > 0:
        for i, peli in enumerate(peliculas, start=1):
            print(f"{i}) {peli['titulo']} - {peli['fecha']} {peli['horario']} - ${peli['precio']}")
    else:
        print("No hay peliculas disponibles")

def mostrarEstadoSala(peliculas):
    """
    Entradas: la lista de las peliculas
    Objetivo: analizar el estado de cada sala (lleno,vacio o mixto)
    Salida: la lista de estados
    """
    estados=[]
    for peli in peliculas:
        asientos= peli["asientos"]
        ocupados = sum(1 for asiento in asientos if asiento!=False)
        if ocupados == len(asientos):
            estados.append(1)  # lleno
        elif ocupados == 0:
            estados.append(0)  # vacio
        else:
            estados.append(2)  # mixto
    return estados

def prohibirSalaCompleta(estados):
    """
    Entrada: la lista de estados
    Objetivo: analizar si alguna sala esta completa
    Salida: una lista con 1 si la sala esta llena y 0 si no lo esta, utilizando todas las peliculas en cartelera
    """
    return [1 if estado == 1 else 0 for estado in estados]

def prohibirSalaVacia(estados):
    """
    Entrada: la lista de estados
    Objetivo: analizar si alguna sala esta vacia
    Salida: una lista con 1 si la sala esta vacia y 0 si no lo esta, utilizando todas las peliculas en cartelera
    """
    return [1 if estado == 0 else 0 for estado in estados]

def borrarRegistroAsiento(asientos,usuario):
    """
    Entrada: la lista de asientos (osea la sala) y el usuario actual (para que no pueda borrar reservas que no sean suyas)
    Objetivo: Eliminar las reservas de asientos en la sala elegida
    Salida: la lista de asientos modificada con menos reservas
    """
    reingreso=1
    cantidadEliminados=0
    asientosElegidos=[]
    contOcupados=sum(1 for asiento in asientos if asiento!= False)

    while reingreso==1 and contOcupados>0:
        print(f"En esta sala hay {len(asientos)} asientos, {contOcupados} ocupados")
        try:
            asientoElegido=int(input("Seleccione asiento a liberar: ")) - 1
            if (0 <= asientoElegido < len(asientos)) and (asientos[asientoElegido]!=False) and ((usuario=="admin") or (asientos[asientoElegido]==usuario)) and (asientoElegido not in asientosElegidos):
                print("Reserva eliminada correctamente")
                asientosElegidos.append(asientoElegido)
                contOcupados -= 1
                cantidadEliminados += 1
                
                asientos[asientoElegido] = False
                cantFilas = 3
                cantColumnas = int(len(asientos) / cantFilas)
                mostrarAsientos(asientos, cantFilas, cantColumnas)
                
            else:
                print("Asiento inválido, ya libre o reservado por otra persona")
        except ValueError:
            print("ingrese numeros, no caracteres")
         
        if contOcupados > 0:
            reingreso = 0
            while reingreso not in [1, 2]:
                try:
                    reingreso = int(input("Desea seleccionar otro asiento? 1)SI 2)NO: "))
                    if reingreso not in [1, 2]:
                        print("Ingrese un numero valido (1-2)")
                except ValueError:
                    print("No se permiten caracteres, solo numeros")
        else:
            print("La sala esta vacia")
            reingreso = 2

    for asiento in asientosElegidos:
        asientos[asiento] = False
    return cantidadEliminados

def seleccionarFuncion(peliculas,prohibir,palabra):
    """
    Entrada: la lista de peliculas, la lista que prohibe salas llenas o vacias (dependiendo de si se utilizara para reservar
    o borrar una reserva) y la palabra (agregar,borrar)
    Objetivo: Seleccionar una pelicula de la cartelera
    Salida: el numero de la pelicula seleccionada
    """
    mostrarCartelera(peliculas)
    valido=0
    while valido==0:
        try:
            peliculaElegida=int(input("Seleccione función: "))
        except ValueError:
            print("porfavor, no ingrese caracteres. Solo numeros")
        else:
            if 1 <= peliculaElegida <= len(peliculas):
                if prohibir[peliculaElegida-1]!=1:
                    valido=1
                else:
                    print(f"Lo sentimos, esta función esta {'llena' if palabra=='agregar' else 'vacía'}")
            else:
                print("Opción incorrecta")
    return peliculaElegida

def seleccionarAsiento(asientos,usuario):
    """
    Entrada: la lista de asientos de la sala y el nombre del usuario actual
    Objetivo: Reservar asientos
    Salida: la cantidad de asientos seleccionados (utilizado para la recaudacion)
    """
    reingreso=1
    cantidadReservados=0
    asientosElegidos=[]
    contDisponibles=asientos.count(False)

    while reingreso==1 and contDisponibles>0:
        print(f"Total asientos: {len(asientos)}, disponibles: {contDisponibles}")
        try:
            asientoElegido=int(input("Seleccione asiento: ")) - 1
        except ValueError:
            print("Porfavor ingrese solo numeros, no caracteres.")
        else:
            if 0 <= asientoElegido < len(asientos) and not asientos[asientoElegido] and asientoElegido not in asientosElegidos:
                print("Asiento reservado correctamente")
                asientosElegidos.append(asientoElegido)
                contDisponibles -= 1
                cantidadReservados += 1
                
                asientos[asientoElegido] = usuario
                cantFilas = 3
                cantColumnas = int(len(asientos)/cantFilas)
                mostrarAsientos(asientos, cantFilas, cantColumnas)

            else:
                print("Asiento inválido o ya seleccionado")

            if contDisponibles>0:
                reingreso=0
                while(reingreso not in [1,2]):
                    try:
                        reingreso=int(input("Desea seleccionar otro asiento? 1)SI 2)NO: "))
                        if (reingreso not in [1,2]):
                            print("Ingrese un numero entre (1-2)")
                    except ValueError:
                        print("Porfavor ingrese solo numeros, no caracteres.")
            else:
                print("La sala está completa")
                reingreso=2
                
    for asiento in asientosElegidos:
        asientos[asiento] = usuario
        
    return cantidadReservados

def mostrarAsientos(asientosFuncion,cantFilas,cantColumnas):
    """
    Entradas: la lista de asientos, la cantidad de filas y la cantidad de columnas (para saber como se mostrara)
    Objetivo: Mostrar con una forma de matriz los asientos ocupados y los libres de una sala
    """
    for j in range(cantFilas):
        for i in range(cantColumnas):
            print("X" if asientosFuncion[i+j*cantColumnas]!=False else "O", end=" ")
        print("")
    print("")

# ==================== FUNCIONES DE PELÍCULAS ==================== #
def agregarPelicula(peliculas,cantAsientos):
    """
    Entradas: la lista de peliculas y la cantidad de asientos (para generar la lista de asientos vacios)
    Objetivo: Agregar peliculas a la lista de peliculas
    Salida: la lista de peliculas modificada con mas peliculas
    """
    nombreValido = False
    while (nombreValido==False):
        nombre = input("Nombre de la película: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío")
        existe = False
        for p in peliculas:
            if p["titulo"].lower() == nombre.lower():
                existe = True

        if existe:
            print("Ya existe una película con ese nombre. Ingrese otro nombre.")

        else:
            nombreValido = True

    fecha=input("Fecha: ").strip()
    while(fecha==""):
        print("la fecha no puede estar vacia")
        fecha=input("Fecha: ").strip()
    horario=input("Horario: ").strip()
    while(horario==""):
        print("el horario no puede estar vacio")
        horario=input("Horario: ").strip()
        
    precioValido=False
    while (precioValido==False):
        try:
            precio=int(input("Precio de entrada: "))
            if (precio>=1500):
                precioValido=True
            else:
                print("El precio debe ser de al menos 1500")
        except ValueError:
            print("Ingrese numeros no caracteres")
    asientosFuncion=[False for i in range (cantAsientos)]
    peliculas.append({
        "titulo": nombre,
        "fecha": fecha,
        "horario": horario,
        "precio": precio,
        "recaudacion": 0,
        "asientos": asientosFuncion
    })
    guardar_peliculas_en_archivo()
    print(f'Película "{nombre}" agregada correctamente.')
    
def eliminarPelicula(peliculas):
    """
    Entradas: la lista de peliculas
    Objetivo: Eliminar peliculas de la lista de peliculas
    Salida: la lista de peliculas modificada con menos peliculas
    """
    if len(peliculas)==0:
        print("no hay peliculas para eliminar")
        return
    valido=False
    while (valido==False):
        try:
            opc=int(input("Ingrese la pelicula a eliminar: "))-1
            if 0 <= opc < len(peliculas):
                valido = True
            else:
                print(f"Ingrese un numero entre (1-{len(peliculas)})")
        except ValueError:
            print("Ingrese un numero, no caracteres")
        
    peliculas.pop(opc)
    guardar_peliculas_en_archivo()
    print("Pelicula eliminada correctamente")

# ==================== FUNCIONES DE REPORTES ==================== #
def reporte_peliculas():
    """
    Entrada: la lista de peliculas
    Objetivo: Mostrar las peliculas ordenadas por nombre
    """
    print("\n=== Reporte de Películas ===")
    if not peliculas:
        print("No hay películas para mostrar.")
        return

    # Uso de LAMBDA → ordenar por nombre de película
    peliculas_ordenadas = sorted(peliculas, key=lambda x: x["titulo"])

    print("\nPelículas ordenadas por nombre:")
    for p in peliculas_ordenadas:
        print(f"- {p['titulo']} ({p['fecha']} - {p['horario']})")

    print(f"\nTotal de películas: {len(peliculas_ordenadas)}")

def leerArchivos():
    """
    Objetivo: Centralizar la lectura de todos los archivos necesarios
    (usuarios, películas, etc.)
    """
    cargar_Usarios_desde_archivo()
    cargar_peliculas_desde_archivo()

# ------------------ MAIN ------------------ #

def main():
    leerArchivos()

    rol, usuario = login()
    while (rol == None):
        print("Usuario invalido")
        print("Volviendo a la pantalla de login")
        rol, usuario = login()

    print(f"Acceso concedido: {usuario} ({rol})")

    cantAsientos=30
    cantFilas=3
    cantColumnas=10
    
    if len(peliculas) == 0:
        peliculas.extend([
            {"titulo":"Hereditary","fecha":"30/7/2025","horario":"9:00","precio":1200,"recaudacion":0,"asientos":[False for i in range(cantAsientos)]},
            {"titulo":"Scott Pilgrim vs. The World","fecha":"31/7/2025","horario":"12:00","precio":1500,"recaudacion":0,"asientos":[False for i in range(cantAsientos)]},
            {"titulo":"The Truman Show","fecha":"1/8/2025","horario":"18:00","precio":1000,"recaudacion":0,"asientos":[False for i in range(cantAsientos)]}
        ])
    salir=0
    while salir!=2:
        print("-------------------------------------------")
        opcAdmin=opcUser=opcGuest=0

        if (rol=="Admin"):
            print("1) Mostrar Cartelera\n2) Reservar Asiento\n3) Mostrar Asientos Disponibles\n4) Borrar Reserva Asiento\n5) Ver Recaudación\n6) Eliminar Pelicula\n7) Agregar Pelicula\n8) Ordenar Peliculas\n9) Salir")
            opcValido=False
            while (opcValido==False):         
                try:
                    opcAdmin=int(input("Seleccione opción: "))
                    if (opcAdmin>0 and opcAdmin<10):
                        opcValido=True
                    else:
                        print("El numero debe estar entre (1-9)")
                except ValueError:
                    print("Ingrese un numero no caracteres")

        elif(rol=="User"):
            print("1) Mostrar Cartelera\n2) Reservar Asiento\n3) Mostrar Asientos Disponibles\n4) Borrar Reserva Asiento\n5) Salir")
            opcValido=False
            while (opcValido==False):         
                try:
                    opcUser=int(input("Seleccione opción: "))
                    if (opcUser>0 and opcUser<6):
                        opcValido=True
                    else:
                        print("El numero debe estar entre (1-5)")
                except ValueError:
                    print("Ingrese un numero no caracteres")

        else:  # Guest
            print("1) Mostrar Cartelera\n2) Mostrar Asientos Disponibles\n3) Salir")
            opcValido=False
            while (opcValido==False):         
                try:
                    opcGuest=int(input("Seleccione opción: "))
                    if (opcGuest>0 and opcGuest<4):
                        opcValido=True
                    else:
                        print("El numero debe estar entre (1-3)")
                except ValueError:
                    print("Ingrese un numero no caracteres")

        if (opcAdmin==1 or opcUser==1 or opcGuest==1):
            mostrarCartelera(peliculas)

        elif (opcAdmin==2 or opcUser==2):
            estados = mostrarEstadoSala(peliculas)
            prohibir = prohibirSalaCompleta(estados)
            todas_llenas = True
            for p in prohibir:
                if p != 1:
                    todas_llenas = False
            if todas_llenas:
                print("No hay funciones disponibles")
            else:
                peliculaElegida = seleccionarFuncion(peliculas,prohibir,"agregar")
                
                mostrarAsientos(
                    peliculas[peliculaElegida-1]["asientos"],
                    cantFilas,
                    cantColumnas
                )
                cantidad = seleccionarAsiento(peliculas[peliculaElegida-1]["asientos"],usuario)
                
                mostrarAsientos(
                    peliculas[peliculaElegida-1]["asientos"],
                    cantFilas,
                    cantColumnas
                )
                peliculas[peliculaElegida-1]["recaudacion"] += cantidad * peliculas[peliculaElegida-1]["precio"]
                guardar_peliculas_en_archivo()

        elif (opcAdmin==3 or opcUser==3 or opcGuest==2):
            mostrarCartelera(peliculas)
            peliculaValida=False
            while (peliculaValida==False):
                try:
                    peliculaElegida=int(input("Función para ver asientos: "))
                    if 1 <= peliculaElegida <= len(peliculas):
                        mostrarAsientos(peliculas[peliculaElegida-1]["asientos"],cantFilas,cantColumnas)
                        peliculaValida=True
                    else:
                        print("Opción incorrecta")
                except ValueError:
                    print("ingrese solo numeros, no caracteres.")

        elif (opcAdmin==4 or opcUser==4):
            estados = mostrarEstadoSala(peliculas)
            prohibir = prohibirSalaVacia(estados)
            if all(p==1 for p in prohibir):
                print("Todas las funciones están vacías")
            else:
                peliculaElegida = seleccionarFuncion(peliculas,prohibir,"borrar")
                mostrarAsientos(
                    peliculas[peliculaElegida-1]["asientos"],
                    cantFilas,
                    cantColumnas
                )
                cantidad = borrarRegistroAsiento(peliculas[peliculaElegida-1]["asientos"],usuario)
                mostrarAsientos(
                    peliculas[peliculaElegida-1]["asientos"],
                    cantFilas,
                    cantColumnas
                )
                peliculas[peliculaElegida-1]["recaudacion"] -= cantidad * peliculas[peliculaElegida-1]["precio"]
                guardar_peliculas_en_archivo()

        elif (opcAdmin==5):
            for peli in peliculas:
                print(f"{peli['titulo']}: ${peli['recaudacion']}")

        elif (opcAdmin==6):
            mostrarCartelera(peliculas)
            eliminarPelicula(peliculas)

        elif (opcAdmin==7):
            agregarPelicula(peliculas,cantAsientos)
        
        elif (opcAdmin==8):
            reporte_peliculas()

        elif (opcAdmin == 9 or opcUser == 5 or opcGuest == 3):
            print("¿Qué desea hacer?")
            print("1) Volver al menú de login")
            print("2) Salir del programa")
            sub = 0
            while sub not in [1, 2]:
                try:
                    sub = int(input("Seleccione opción (1-2): "))
                    if sub not in [1, 2]:
                        print("Ingrese un número válido (1-2)")
                except ValueError:
                    print("Ingrese un número válido (1-2)")

            if sub == 1:
                print("Volviendo al menú de login...")
                contar(3)
                rol, usuario = login()
                while (rol == None):
                    print("Usuario invalido")
                    print("Volviendo a la pantalla de login")
                    rol, usuario = login()
                print(f"Acceso concedido: {usuario} ({rol})")
            else:
                print("Saliendo del programa...")
                contar(3)
                salir = 2
    print("----------------------------------------------------\nPrograma finalizado\nGracias por utilizar nuestros servicios")
    
main()
