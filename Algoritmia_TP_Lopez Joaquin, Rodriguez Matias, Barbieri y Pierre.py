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

        while not valido:
            asientoElegido=int(input("Seleccione que registro quiere eliminar: ")) - 1
            if 0 <= asientoElegido < len(asientos) and asientos[asientoElegido] and asientoElegido not in asientosElegidos:
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

        while not valido:
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

def main():
    cantAsientos=30
    cantFilas=3
    cantColumnas=10

    peliculas=["Hereditary","Scott Pilgrim vs. The World","The Truman Show"]
    fechas=["30/7/2025","31/7/2025","1/8/2025"]
    horarios=["9:00","12:00","18:00"]
    precios = [1200,1500,1000]
    recaudaciones = [0]*len(peliculas)

    asientosFuncion1=[False for i in range (cantAsientos)]
    asientosFuncion2=[False for i in range (cantAsientos)]
    asientosFuncion3=[False for i in range (cantAsientos)]
    asientosDisponibles1=[i for i in range (cantAsientos)]
    asientosDisponibles2=[i for i in range (cantAsientos)]
    asientosDisponibles3=[i for i in range (cantAsientos)]

    listaAsientos=[]
    listaAsientos.append(asientosFuncion1)
    listaAsientos.append(asientosFuncion2)
    listaAsientos.append(asientosFuncion3)

    # Lista de asientos disponibles
    listaDisponibles=[]
    listaDisponibles.append(asientosDisponibles1)
    listaDisponibles.append(asientosDisponibles2)
    listaDisponibles.append(asientosDisponibles3)

    salir=0
    while salir!=2:
        print("-------------------------------------------")
        print("1) Mostrar Cartelera\n2) Reservar Asiento\n3) Mostrar Asientos Disponibles\n4) Borrar Reserva Asiento\n5) Ver Recaudación por Función\n6) Salir del Menu")
        opc=int(input("Seleccione La opcion: "))
        while opc<1 or opc>6:
            opc=int(input("Opción incorrecta. Seleccione La opcion: "))

        if opc==1:
            mostrarCartelera(peliculas,fechas,horarios,precios)

        elif opc==2:
            estados = mostrarEstadoSala(listaAsientos)
            prohibir = prohibirSalaCompleta(estados)
            if all(p==1 for p in prohibir):
                print("Lo sentimos no hay funciones disponibles")
            else:
                peliculaElegida = seleccionarFuncion(peliculas,fechas,horarios,prohibir,"agregar",precios)
                cantidad = seleccionarAsiento(listaAsientos[peliculaElegida-1], listaDisponibles[peliculaElegida-1])
                recaudaciones[peliculaElegida-1] += cantidad * precios[peliculaElegida-1]

        elif opc==3:
            mostrarCartelera(peliculas,fechas,horarios,precios)
            reingreso=1
            while reingreso==1:
                peliculaElegida=int(input("De qué función desea ver la disponibilidad de los asientos: "))
                if 1 <= peliculaElegida <= len(peliculas):
                    mostrarAsientos(listaAsientos[peliculaElegida-1],cantFilas,cantColumnas)
                else:
                    print("Opción incorrecta")
                reingreso=int(input("Desea ver otras opciones? 1)SI 2)NO: "))

        elif opc==4:
            estados = mostrarEstadoSala(listaAsientos)
            prohibir = prohibirSalaVacia(estados)
            if all(p==1 for p in prohibir):
                print("Todas las funciones están vacías")
            else:
                peliculaElegida = seleccionarFuncion(peliculas,fechas,horarios,prohibir,"borrar",precios)
                cantidad = borrarRegistroAsiento(listaAsientos[peliculaElegida-1], listaDisponibles[peliculaElegida-1])
                recaudaciones[peliculaElegida-1] -= cantidad * precios[peliculaElegida-1]

        elif opc==5:
            for i in range(len(peliculas)):
                print(f"{peliculas[i]}: ${recaudaciones[i]}")

        elif opc==6:
            salir=2

        if salir!=2:
            salir=int(input("Desea volver al menú? 1)SI 2)NO: "))

    print("----------------------------------------------------\nPrograma finalizado\nGracias por utilizar nuestros servicios")

main()
