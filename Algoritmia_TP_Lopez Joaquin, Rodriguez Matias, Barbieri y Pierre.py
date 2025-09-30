# Lista de usuarios (usuario, contraseña, rol)
usuarios = [
    {"usuario": "admin", "contraseña": "admin", "rol": "Admin"},
    {"usuario": "user", "contraseña": "1234", "rol": "User"}
]

def login():
    """
    Muestra un menú de login para el sistema.
    Opciones:
        1) Ingresar con usuario
        2) Entrar como invitado
        3) Registrar nuevo usuario
    Retorna:
        (rol, usuario) si login válido
        ("Guest", "Invitado") si guest
        (None, None) si error
    """
    print("=== Sistema de Login ===")
    print("1) Ingresar con usuario")
    print("2) Entrar como Guest")
    print("3) Registrar Usuario")

    # Validación de input con try/except
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
        return login()  # vuelve al login después de registrar

    # Opción 1: login normal
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    # Buscar usuario válido con next
    usuario_valido = next(
        (u for u in usuarios if u["usuario"] == usuario and u["contraseña"] == contraseña),
        None
    )

    if usuario_valido:
        print(f"Bienvenido {usuario_valido['usuario']} (rol: {usuario_valido['rol']})")
        return usuario_valido["rol"], usuario_valido["usuario"]
    else:
        print("Credenciales inválidas")
        return None, None

def registrarUsuario():
    print("=== Registrar Nuevo Usuario ===")

    # Validar que el nombre de usuario no exista
    nombre_valido = False
    while not nombre_valido:
        usuario = input("Nuevo usuario: ")
        if any(u["usuario"] == usuario for u in usuarios):
            print("Ese nombre de usuario ya existe. Elegí otro.")
        else:
            nombre_valido = True

    # Validar formato de contraseña
    print("La contraseña debe tener al menos 8 caracteres, una mayúscula y un número.")
    contraseña_valida = False
    while not contraseña_valida:
        contraseña = input("Contraseña: ")
        tiene_mayus = any(ch.isupper() for ch in contraseña)
        tiene_numero = any(ch.isdigit() for ch in contraseña)
        cumple_formato = (len(contraseña) >= 8 and tiene_mayus and tiene_numero)

        if cumple_formato:
            contraseña_valida = True
        else:
            print("La contraseña no cumple los requisitos.")

    # Rol por defecto: User
    usuarios.append({"usuario": usuario, "contraseña": contraseña, "rol": "User"})
    print("Usuario creado con éxito.")

# ------------------ FUNCIONES DE CINE ------------------ #

def mostrarCartelera(peliculas,fechas,horarios,precios):
    print("-------------------------------------------")
    for i in range(len(peliculas)):
        print(f"{i+1}) {peliculas[i]} - {fechas[i]} {horarios[i]} - ${precios[i]}")

def mostrarEstadoSala(listaAsientos):
    estados=[]
    for sala in listaAsientos:
        ocupados = sum(sala)
        if ocupados == len(sala):
            estados.append(1)  # lleno
        elif ocupados == 0:
            estados.append(0)  # vacío
        else:
            estados.append(2)  # mixto
    return estados

def prohibirSalaCompleta(estados):
    return [1 if estado == 1 else 0 for estado in estados]

def prohibirSalaVacia(estados):
    return [1 if estado == 0 else 0 for estado in estados]

def borrarRegistroAsiento(asientos):
    reingreso=1
    cantidadEliminados=0
    asientosElegidos=[]
    contOcupados=sum(asientos)

    while reingreso==1 and contOcupados>0:
        print(f"En esta sala hay {len(asientos)} asientos, {contOcupados} ocupados")
        asientoElegido=int(input("Seleccione asiento a liberar: ")) - 1

        if 0 <= asientoElegido < len(asientos) and asientos[asientoElegido] and asientoElegido not in asientosElegidos:
            print("Reserva eliminada correctamente")
            asientosElegidos.append(asientoElegido)
            contOcupados -= 1
            cantidadEliminados += 1
        else:
            print("Asiento inválido o ya libre")

        if contOcupados > 0:
            reingreso=int(input("Desea seleccionar otro asiento? 1)SI 2)NO: "))
        else:
            print("La sala está vacía")
            reingreso=2

    for asiento in asientosElegidos:
        asientos[asiento] = False

    return cantidadEliminados

def seleccionarFuncion(peliculas,fechas,horarios,prohibir,palabra,precios):
    mostrarCartelera(peliculas,fechas,horarios,precios)
    valido=0
    while valido==0:
        peliculaElegida=int(input("Seleccione función: "))
        if 1 <= peliculaElegida <= len(peliculas):
            if prohibir[peliculaElegida-1]!=1:
                valido=1
            else:
                print(f"Lo sentimos, esta función está {'llena' if palabra=='agregar' else 'vacía'}")
        else:
            print("Opción incorrecta")
    return peliculaElegida

def seleccionarAsiento(asientos):
    reingreso=1
    cantidadReservados=0
    asientosElegidos=[]
    contDisponibles=asientos.count(False)

    while reingreso==1 and contDisponibles>0:
        print(f"Total asientos: {len(asientos)}, disponibles: {contDisponibles}")
        asientoElegido=int(input("Seleccione asiento: ")) - 1

        if 0 <= asientoElegido < len(asientos) and not asientos[asientoElegido] and asientoElegido not in asientosElegidos:
            print("Asiento reservado correctamente")
            asientosElegidos.append(asientoElegido)
            contDisponibles -= 1
            cantidadReservados += 1
        else:
            print("Asiento inválido o ya seleccionado")

        if contDisponibles>0:
            reingreso=int(input("Desea seleccionar otro asiento? 1)SI 2)NO: "))
        else:
            print("La sala está completa")
            reingreso=2

    for asiento in asientosElegidos:
        asientos[asiento] = True

    return cantidadReservados

def mostrarAsientos(asientosFuncion,cantFilas,cantColumnas):
    for j in range(cantFilas):
        for i in range(cantColumnas):
            print("X" if asientosFuncion[i+j*cantColumnas] else "O", end=" ")
        print("")
    print("")

def eliminarPelicula(peliculas,fechas,horarios,precios,listaAsientos,recaudaciones):
    opc=int(input("Ingrese la pelicula a eliminar: "))-1
    while (opc <0 or opc >= len(listaAsientos)):
        opc=int(input("Número inválido. Ingrese película a eliminar: "))-1
    peliculas.pop(opc)
    fechas.pop(opc)
    precios.pop(opc)
    horarios.pop(opc)
    listaAsientos.pop(opc)
    recaudaciones.pop(opc)
    print("Pelicula eliminada correctamente")

def agregarPelicula(peliculas,fechas,horarios,precios,listaAsientos,recaudaciones,cantAsientos):
    nombre=input("Nombre de la pelicula: ")
    fecha=input("Fecha: ")
    horario=input("Horario: ")
    precio=int(input("Precio de entrada: "))
    asientosFuncion=[False for _ in range (cantAsientos)]
    peliculas.append(nombre)
    fechas.append(fecha)
    horarios.append(horario)
    precios.append(precio)
    listaAsientos.append(asientosFuncion)
    recaudaciones.append(0)

# ------------------ MAIN ------------------ #

def main():
    # login
    rol, usuario = login()
    while (rol == None):
        rol, usuario = login()

    print(f"Acceso concedido: {usuario} ({rol})")

    cantAsientos=30
    cantFilas=3
    cantColumnas=10

    peliculas=["Hereditary","Scott Pilgrim vs. The World","The Truman Show"]
    fechas=["30/7/2025","31/7/2025","1/8/2025"]
    horarios=["9:00","12:00","18:00"]
    precios = [1200,1500,1000]
    recaudaciones = [0,0,0]

    listaAsientos=[[False for _ in range (cantAsientos)] for _ in peliculas]

    salir=0
    while salir!=2:
        print("-------------------------------------------")
        opcAdmin=opcUser=opcGuest=0

        if (rol=="Admin"):
            print("1) Mostrar Cartelera\n2) Reservar Asiento\n3) Mostrar Asientos Disponibles\n4) Borrar Reserva Asiento\n5) Ver Recaudación\n6) Eliminar Pelicula\n7) Agregar Pelicula\n8) Salir")
            opcAdmin=int(input("Seleccione opción: "))
            while opcAdmin<1 or opcAdmin>8:
                opcAdmin=int(input("Opción incorrecta. Seleccione opción: "))

        elif(rol=="User"):
            print("1) Mostrar Cartelera\n2) Reservar Asiento\n3) Mostrar Asientos Disponibles\n4) Borrar Reserva Asiento\n5) Salir")
            opcUser=int(input("Seleccione opción: "))
            while opcUser<1 or opcUser>5:
                opcUser=int(input("Opción incorrecta. Seleccione opción: "))

        else:  # Guest
            print("1) Mostrar Cartelera\n2) Mostrar Asientos Disponibles\n3) Salir")
            opcGuest=int(input("Seleccione opción: "))
            while opcGuest<1 or opcGuest>3:
                opcGuest=int(input("Opción incorrecta. Seleccione opción: "))

        if (opcAdmin==1 or opcUser==1 or opcGuest==1):
            mostrarCartelera(peliculas,fechas,horarios,precios)

        elif (opcAdmin==2 or opcUser==2):
            estados = mostrarEstadoSala(listaAsientos)
            prohibir = prohibirSalaCompleta(estados)
            if all(p==1 for p in prohibir):
                print("No hay funciones disponibles")
            else:
                peliculaElegida = seleccionarFuncion(peliculas,fechas,horarios,prohibir,"agregar",precios)
                cantidad = seleccionarAsiento(listaAsientos[peliculaElegida-1])
                recaudaciones[peliculaElegida-1] += cantidad * precios[peliculaElegida-1]

        elif (opcAdmin==3 or opcUser==3 or opcGuest==2):
            mostrarCartelera(peliculas,fechas,horarios,precios)
            peliculaElegida=int(input("Función para ver asientos: "))
            if 1 <= peliculaElegida <= len(peliculas):
                mostrarAsientos(listaAsientos[peliculaElegida-1],cantFilas,cantColumnas)
            else:
                print("Opción incorrecta")

        elif (opcAdmin==4 or opcUser==4):
            estados = mostrarEstadoSala(listaAsientos)
            prohibir = prohibirSalaVacia(estados)
            if all(p==1 for p in prohibir):
                print("Todas las funciones están vacías")
            else:
                peliculaElegida = seleccionarFuncion(peliculas,fechas,horarios,prohibir,"borrar",precios)
                cantidad = borrarRegistroAsiento(listaAsientos[peliculaElegida-1])
                recaudaciones[peliculaElegida-1] -= cantidad * precios[peliculaElegida-1]

        elif (opcAdmin==5):
            for i in range(len(peliculas)):
                print(f"{peliculas[i]}: ${recaudaciones[i]}")

        elif (opcAdmin==6):
            mostrarCartelera(peliculas,fechas,horarios,precios)
            eliminarPelicula(peliculas,fechas,horarios,precios,listaAsientos,recaudaciones)

        elif (opcAdmin==7):
            agregarPelicula(peliculas,fechas,horarios,precios,listaAsientos,recaudaciones,cantAsientos)

        elif (opcAdmin==8 or opcUser==5 or opcGuest==3):
            salir=2

        if salir!=2:
            salir=int(input("¿Desea volver al menú? 1)SI 2)NO: "))

    print("----------------------------------------------------\nPrograma finalizado\nGracias por utilizar nuestros servicios")

main()

