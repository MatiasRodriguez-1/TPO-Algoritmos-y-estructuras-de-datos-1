# Lista de usuarios (usuario, contraseña, rol)
usuarios = [
    {"usuario": "admin", "contraseña": "admin", "rol": "Admin"},
    {"usuario": "user", "contraseña": "1234", "rol": "User"}
]


     """
    Muestra un menú de login para el sistema.
    Permite:
        1) Ingresar con usuario registrado
        2) Entrar como invitado
        3) Registrar un nuevo usuario
    
    Retorna:
        tuple: (rol, usuario) si el login es válido
               ("Guest", "Invitado") si entra como guest
               (None, None) si no se pudo autenticar
    """

    print("=== Sistema de Login ===")
    print("1) Ingresar con usuario")
    print("2) Entrar como Guest")
    print("3) Registrar Usuario")

    # Validación con try/except
    try:
        opcion = int(input("Seleccione opción: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return None, None

    # Validación con lambda
    es_valida = lambda op: op in [1, 2, 3]
    while not es_valida(opcion):
        print("La opción debe estar entre 1 y 3")
        try:
            opcion = int(input("Seleccione opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return None, None

    if opcion == 2:
        return "Guest", "Invitado"

    elif opcion == 3:
        registrarUsuario()
        return login()  # vuelve a pedir login luego de registrar

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    # Buscar usuario válido con next + lambda
    usuario_valido = next(
        (u for u in usuarios if u["usuario"] == usuario and u["contraseña"] == contraseña),
        None
    )

    if usuario_valido:
        print("Bienvenido", usuario_valido["usuario"], "rol:", usuario_valido["rol"])
        return usuario_valido["rol"], usuario_valido["usuario"]
    else:
        print("Credenciales inválidas")
        return None, None

def registrarUsuario():
    print("=== Registrar Nuevo Usuario ===")
    usuario = input("Nuevo usuario: ")
    contraseña = input("Contraseña: ")
    rol = "User"
    usuarios.append({"usuario": usuario, "contraseña": contraseña, "rol": rol})
    print("Usuario creado con éxito.")

def mostrarCartelera(peliculas,fechas,horarios,precios):
    print("-------------------------------------------")
    #Se muestran todas las peliculas con sus fechas y horarios
    for i in range(len(peliculas)):
        print(peliculas[i],fechas[i],horarios[i], "$",precios[i])

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

def borrarRegistroAsiento(asientos,asientosDisponibles):
    reingreso=1
    cantidadEliminados=0
    asientosElegidos=[]
    contOcupados=sum(asientos)

    while reingreso==1 and contOcupados>0:
        valido = 0
        print("En esta sala hay ",len(asientos)," asientos ",contOcupados," ocupados")
        asientoElegido=int(input("Seleccione que registro quiere eliminar: ")) - 1

        if 0 <= asientoElegido and asientoElegido < len(asientos) and asientos[asientoElegido] == True and asientoElegido not in asientosElegidos:
            valido=1
        else:
            print("Asiento inválido o ya libre")

        while valido==0:
            asientoElegido=int(input("Seleccione que registro quiere eliminar: ")) - 1
            if 0 <= asientoElegido and asientoElegido < len(asientos) and asientos[asientoElegido] == True and asientoElegido not in asientosElegidos:
                valido=1
            else:
                print("Asiento inválido o ya libre")

        print("reserva eliminada correctamente")
        asientosElegidos.append(asientoElegido)
        contOcupados -= 1
        cantidadEliminados += 1

        if contOcupados > 0:
            reingreso=int(input("Desea seleccionar otro asiento? 1)SI 2)NO: "))
        else:
            print("La sala está vacía")
            reingreso=2

    for asiento in asientosElegidos:
        asientos[asiento] = False

    return cantidadEliminados

def seleccionarFuncion(peliculas,fechas,horarios,prohibir,palabra,precios):
    print("-------------------------------------------")
    mostrarCartelera(peliculas,fechas,horarios,precios)
    valido=0
    while valido==0:
        peliculaElegida=int(input("Seleccione su opcion: "))
        if 1 <= peliculaElegida <= len(peliculas):
            if prohibir[peliculaElegida-1]!=1:
                valido=1
            else:
                print(f"Lo sentimos, esta función está {'llena' if palabra=='agregar' else 'vacía'}")
        else:
            print("Opcion incorrecta")
    print("Función elegida correctamente")
    return peliculaElegida

def seleccionarAsiento(asientos,asientosDisponibles):
    reingreso=1
    cantidadReservados=0
    asientosElegidos=[]
    contDisponibles=asientos.count(False)

    while reingreso==1 and contDisponibles>0:
        valido=0
        print(f"Total asientos: {len(asientos)}, disponibles: {contDisponibles}")
        asientoElegido=int(input("Seleccione asiento: ")) - 1

        if 0 <= asientoElegido < len(asientos) and not asientos[asientoElegido] and asientoElegido not in asientosElegidos:
            valido=1
        else:
            print("Asiento inválido o ya seleccionado")

        while valido==0:
            asientoElegido=int(input("Seleccione asiento: ")) - 1
            if 0 <= asientoElegido < len(asientos) and not asientos[asientoElegido] and asientoElegido not in asientosElegidos:
                valido=1
            else:
                print("Asiento inválido o ya seleccionado")

        print("Asiento reservado correctamente")
        asientosElegidos.append(asientoElegido)
        contDisponibles -= 1
        cantidadReservados += 1

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
    while (opc <0 or opc >len(listaAsientos)):
        print("Ingrese un numero de pelicula valida")
        opc=int(input("Ingrese la pelicula a eliminar :"))-1
    peliculas.pop(opc)
    fechas.pop(opc)
    precios.pop(opc)
    horarios.pop(opc)
    listaAsientos.pop(opc)
    recaudaciones.pop(opc)
    print("Pelicula eliminada correctamente")

def agregarPelicula(peliculas,fechas,horarios,precios,listaAsientos,recaudaciones,cantAsientos):
    nombre=input("Ingrese el nombre de la pelicula: ")
    fecha=input("Ingrese la fecha de la pelicula: ")
    horario=input("Ingrese el horario de la pelicula: ")
    precio=int(input("Ingrese el costo de la entrada: "))
    asientosFuncion=[False for i in range (cantAsientos)]
    peliculas.append(nombre)
    fechas.append(fecha)
    horarios.append(horario)
    precios.append(precio)
    listaAsientos.append(asientosFuncion)
    recaudaciones.append(0)

def main():
    #login
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

    asientosFuncion1=[False for i in range (cantAsientos)]
    asientosFuncion2=[False for i in range (cantAsientos)]
    asientosFuncion3=[False for i in range (cantAsientos)]
    asientosDisponibles1=[i for i in range (cantAsientos)]
    asientosDisponibles2=[i for i in range (cantAsientos)]
    asientosDisponibles3=[i for i in range (cantAsientos)]

    listaAsientos=[asientosFuncion1,asientosFuncion2,asientosFuncion3]
    listaDisponibles=[asientosDisponibles1,asientosDisponibles2,asientosDisponibles3]

    salir=0
    while salir!=2:
        print("-------------------------------------------")
        opcAdmin=0
        opcUser=0
        opcGuest=0
        if (rol=="Admin"):
            print("1) Mostrar Cartelera\n2) Reservar Asiento\n3) Mostrar Asientos Disponibles\n4) Borrar Reserva Asiento\n5) Ver Recaudación por Función\n6) Eliminar Pelicula \n7) Agregar Pelicula \n8) Salir del Menu")
            opcAdmin=int(input("Seleccione La opcion: "))
            while opcAdmin<1 or opcAdmin>8:
                opcAdmin=int(input("Opción incorrecta. Seleccione La opcion: "))
                 
        elif(rol=="User"):
            print("1) Mostrar Cartelera\n2) Reservar Asiento\n3) Mostrar Asientos Disponibles\n4) Borrar Reserva Asiento\n5) Salir del Menu")
            opcUser=int(input("Seleccione La opcion: "))
            while opcUser<1 or opcAdmin>5:
                opcUser=int(input("Opción incorrecta. Seleccione La opcion: "))
        
        else:
            print("1) Mostrar Cartelera\n2) Mostrar Asientos Disponibles\n3) Salir del Menu")
            opcGuest=int(input("Seleccione La opcion: "))
            while opcGuest<1 or opcGuest>3:
                opcGuest=int(input("Opción incorrecta. Seleccione La opcion: "))

        if (opcAdmin==1 or opcUser==1 or opcGuest==1):
            mostrarCartelera(peliculas,fechas,horarios,precios)

        elif (opcAdmin==2 or opcUser==2):
            estados = mostrarEstadoSala(listaAsientos)
            prohibir = prohibirSalaCompleta(estados)
            if all(p==1 for p in prohibir):
                print("Lo sentimos no hay funciones disponibles")
            else:
                peliculaElegida = seleccionarFuncion(peliculas,fechas,horarios,prohibir,"agregar",precios)
                cantidad = seleccionarAsiento(listaAsientos[peliculaElegida-1], listaDisponibles[peliculaElegida-1])
                recaudaciones[peliculaElegida-1] += cantidad * precios[peliculaElegida-1]

        elif (opcAdmin==3 or opcUser==3 or opcGuest==2):
            mostrarCartelera(peliculas,fechas,horarios,precios)
            reingreso=1
            while reingreso==1:
                peliculaElegida=int(input("De qué función desea ver la disponibilidad de los asientos: "))
                if 1 <= peliculaElegida <= len(peliculas):
                    mostrarAsientos(listaAsientos[peliculaElegida-1],cantFilas,cantColumnas)
                else:
                    print("Opción incorrecta")
                reingreso=int(input("Desea ver otras opciones? 1)SI 2)NO: "))

        elif (opcAdmin==4 or opcUser==4):
            estados = mostrarEstadoSala(listaAsientos)
            prohibir = prohibirSalaVacia(estados)
            if all(p==1 for p in prohibir):
                print("Todas las funciones están vacías")
            else:
                peliculaElegida = seleccionarFuncion(peliculas,fechas,horarios,prohibir,"borrar",precios)
                cantidad = borrarRegistroAsiento(listaAsientos[peliculaElegida-1], listaDisponibles[peliculaElegida-1])
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
            salir=int(input("Desea volver al menú? 1)SI 2)NO: "))

    print("----------------------------------------------------\nPrograma finalizado\nGracias por utilizar nuestros servicios")


main()
