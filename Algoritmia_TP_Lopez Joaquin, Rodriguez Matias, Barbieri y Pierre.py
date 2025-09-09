def mostrarCartelera(peliculas,fechas,horarios,precios):
    print("-------------------------------------------")
    #Se muestran todas las peliculas con sus fechas y horarios
    for i in range(len(peliculas)):
        print(peliculas[i],fechas[i],horarios[i], "$",precios[i])

def mostrarEstadoSala(asientos,asientos2,asientos3):
    #Cantidad de asientos ocupados en cada sala
    cont1=0
    cont2=0
    cont3=0
    #Lista con los estados de cada sala
    estados=[]
    #Si el asiento esta ocupado, el contador aumenta su valor en 1
    for i in range (len(asientos)):
        if (asientos[i]==True):
            cont1=cont1+1
    
    for i in range (len(asientos2)):
        if (asientos2[i]==True):
            cont2=cont2+1
            
    for i in range (len(asientos3)):
        if (asientos3[i]==True):
            cont3=cont3+1
    #Dependiendo la relacion de asientos ocupados con los asientos totales
    if (cont1==len(asientos)):
        #lleno, la sala no puede ser elegida para reservar mas asientos
        estado1=1
    elif(cont1==0):
        #vacio, la sala no puede ser elegida para eliminar reservas
        estado1=0
    else:
        #mixto, la sala puede ser elegida para reservar como para eliminar
        estado1=2
        
    if (cont2==len(asientos2)):
        estado2=1
    elif(cont2==0):
        estado2=0
    else:
        estado2=2
        
    if (cont3==len(asientos3)):
        estado3=1
    elif(cont3==0):
        estado3=0
    else:
        estado3=2
    
    #se agregan los estados la lista de estados
    estados.append(estado1)
    estados.append(estado2)
    estados.append(estado3)
    return estados

def prohibirSalaCompleta(estados):
    #lista que devuelve si las salas estan completas o no
    prohibir = []
    for i in range(len(estados)):
        #Si el estado igual a 1, entonces ese index de la lista lo marcara con 1 
        if estados[i] == 1:
            prohibir.append(1)
        #Si es desigual a 1, entonces lo marcara con 0
        else:
            prohibir.append(0)
    #Devuelve la lista
    return prohibir

def prohibirSalaVacia(estados):
    #lista que devuelve si las salas estan vacias o no
    prohibir = []
    for i in range(len(estados)):
        #Si el estado igual a 0, entonces ese index de la lista lo marcara con 1
        if estados[i] == 0:
            prohibir.append(1)
        #Si es desigual a 0, entonces lo marcara con 0
        else:
            prohibir.append(0)
    #Devuelve la lista
    return prohibir

def borrarRegistroAsiento(asientos,asientosDisponibles):
    #Variable usada para que el usuario pueda borrar un asiento extra
    reingreso=1
    #Variable que cuenta los asientos eliminados
    cantidadEliminados=0
    #Cuenta cuantos asientos se encuentran ocupados
    contOcupados=0
    #Lista que almacena los asientos elegidos por el usuario
    asientosElegidos=[]
    for i in range (len(asientos)):
        #se cuentan los asientos ocupados
        if (asientos[i]==True):
            contOcupados=contOcupados+1
    #bucle
    while (reingreso==1):
        #variable que confirma si el asiento elegido esta ocupado
        valido = 0
        print("En esta sala hay un total de : ",len(asientos),"asientos")
        print("En esta sala hay un total de: ", contOcupados,"asientos ocupados")
        #ingreso del usuario para seleccionar un asiento
        asientoElegido=int(input("Seleccione que registro quiere eliminar: "))
        #haciendo mas facil el emparejamiento con las listas, ya que las listas arrancan en 0
        asientoElegido=asientoElegido-1
        #Verificando que el asiento este ocupado
        for i in range(len(asientos)):
            if (asientoElegido==i and asientos[i] == True):
                valido=1
            elif (asientoElegido==i and asientos[i] == False):
                print("El asiento elegido ya esta libre.")
        #en caso de que la reserva este ocupada se notifica de la eliminacion de la misma
        for i in range(len(asientosElegidos)):
            if(asientoElegido==asientosElegidos[i]):
                valido=0
                print("La reserva ya ha sido borrada")
                
        while (asientoElegido<0 or asientoElegido>len(asientos) or valido==0):
            print("Opcion incorrecta, vuelva a ingresar.")
            asientoElegido=int(input("Seleccione que registro quiere eliminar: "))
            asientoElegido=asientoElegido-1
                
            for i in range(len(asientos)):
                if (asientoElegido==i and asientos[i] == True):
                    valido=1
                elif (asientoElegido==i and asientos[i] == False):
                    print("El asiento elegido ya esta libre.")
            for i in range(len(asientosElegidos)):
                if(asientoElegido==asientosElegidos[i]):
                    valido=0
                    print("la reserva ya ha sido borrada")
        print("reserva eliminada correctamente")
        #disminuye la cantidad de asientos ocupados
        contOcupados=contOcupados-1
        #Se incrementa la variable
        cantidadEliminados=cantidadEliminados+1
        #cuando el asiento elegido es valido, se agrega a la lista de asientos elegidos
        asientosElegidos.append(asientoElegido)
        if (contOcupados!=0): 
            #ingreso del usuario para volver (o no) a ingresar a otro asiento
            reingreso=int(input("Desea seleccionar otro asiento? 1)SI.2)NO"))
            while (reingreso<1 or reingreso>2):
                print("ingreso incorrecto, vuelva a ingresar")
                reingreso=int(input("Desea seleccionar otro asiento? 1)SI.2)NO"))
        else:
            print("La sala esta vacia")
            reingreso=2
    #al finalizar el ingreso de todos los datos, se lleva a cabo la eliminacion de todas las reservas elegidas
    for j in range(len(asientosElegidos)):
        for i in range(len(asientosDisponibles)):
            if asientosElegidos[j]==asientosDisponibles[i]:
                #Cambia el valor del asiento de Ocupado a Vacio
                asientos[i]=False
    return cantidadEliminados

def seleccionarFuncion(peliculas,fechas,horarios,prohibir,palabra,precios):
    print("-------------------------------------------")
    #Variable que confirma si la funcion es elegible
    valido=0
    #Se muestran las opciones de peliculas, con sus fechas y horarios
    print("Las opciones son:")
    mostrarCartelera(peliculas,fechas,horarios,precios)
    for i in range(len(peliculas)):
        print("Ingrese ",i+1,")"," para:",peliculas[i])
    #se pide al usuario que ingrese la funcion que desea ver
    peliculaElegida=int(input("Seleccione su opcion: "))
    #se evalua si esa sala esta completa
    if (peliculaElegida==1 and prohibir[0]!=1):
        #en caso de que no, valido se convierte en 1
        valido=1
    elif (peliculaElegida==1 and prohibir[0]==1):
        if (palabra=="agregar"):
            print("Lo sentimos esta funcion esta llena")
        else:
            print("La funcion ya esta vacia")
    elif (peliculaElegida==2 and prohibir[1]!=1):
        valido=1
    elif (peliculaElegida==2 and prohibir[1]==1):
        if (palabra=="agregar"):
            print("Lo sentimos esta funcion esta llena")
        else:
            print("La funcion ya esta vacia")
    elif (peliculaElegida==3 and prohibir[2]!=1):
        valido=1
    elif (peliculaElegida==3 and prohibir[2]==1):
        if (palabra=="agregar"):
            print("Lo sentimos esta funcion esta llena")
        else:
            print("La funcion ya esta vacia")
        
    while (valido==0):
        print("Opcion incorrecta, vuelva a ingresar.")
        peliculaElegida=int(input("Seleccione su opcion: "))
        if (peliculaElegida==1 and prohibir[0]!=1):
            valido=1
        elif (peliculaElegida==1 and prohibir[0]==1):
            if (palabra=="agregar"):
                print("Lo sentimos esta funcion esta llena")
            else:
                print("La funcion ya esta vacia")
        elif (peliculaElegida==2 and prohibir[1]!=1):
            valido=1
        elif (peliculaElegida==2 and prohibir[1]==1):
            if (palabra=="agregar"):
                print("Lo sentimos esta funcion esta llena")
            else:
                print("La funcion ya esta vacia")
        elif (peliculaElegida==3 and prohibir[2]!=1):
            valido=1
        elif (peliculaElegida==3 and prohibir[2]==1):
            if (palabra=="agregar"):
                print("Lo sentimos esta funcion esta llena")
            else:
                print("La funcion ya esta vacia")
                
    print("Funcion elegida correctamente")
    #Se Devuelve el numero de la pelicula elegida
    return peliculaElegida

def seleccionarAsiento(asientos,asientosDisponibles):
    #Variable usada para que el usuario pueda ingresar un asiento extra
    reingreso=1
    #Cantidad de asientos disponibles
    contDisponibles=0
    #Lista que almacena los asientos elegidos por el usuario
    asientosElegidos=[]
    #Variable para contar cuantos se reservaron
    cantidadReservados = 0
    for i in range (len(asientos)):
        #se cuentan los asientos disponibles
        if (asientos[i]==False):
            contDisponibles=contDisponibles+1
    #bucle
    while (reingreso==1):
        #variable que confirma si el asiento elegido esta libre
        valido = 0
        
        print("En esta sala hay un total de : ",len(asientos),"asientos")
        print("En esta sala hay un total de: ", contDisponibles,"asientos disponibles")
        #ingreso del usuario para seleccionar un asiento
        asientoElegido=int(input("Seleccione que asiento quiere reservar: "))
        #haciendo mas facil el emparejamiento con las listas, ya que las listas arrancan en 0
        asientoElegido=asientoElegido-1
        #Verificando que el asiento este libre
        for i in range(len(asientos)):
            if (asientoElegido==i and asientos[i] == False):
                #El asiento es elegible
                valido=1
            elif (asientoElegido==i and asientos[i] == True):
                print("El asiento elegido ya esta ocupado.")
                
        for i in range(len(asientosElegidos)):
            if(asientoElegido==asientosElegidos[i]):
                valido=0
                print("El Asiento ya ha sido seleccionado")
                
        while (asientoElegido<0 or asientoElegido>=len(asientos) or valido==0):
            print("Opcion incorrecta, vuelva a ingresar.")
            asientoElegido=int(input("Seleccione que Asiento quiere reservar: "))
            asientoElegido=asientoElegido-1
                
            for i in range(len(asientos)):
                if (asientoElegido==i and asientos[i] == False):
                    valido=1
                elif (asientoElegido==i and asientos[i] == True):
                    print("El asiento elegido ya esta ocupado.")
            for i in range(len(asientosElegidos)):
                if(asientoElegido==asientosElegidos[i]):
                    valido=0
                    print("El Asiento ya ha sido seleccionado")
        print("Asiento reservado correctamente")
        contDisponibles=contDisponibles-1
        # la cantidad de reservados aumenta en 1 
        cantidadReservados += 1
        #cuando el asiento elegido es valido, se agrega a la lista de asientos elegidos
        asientosElegidos.append(asientoElegido)
        if (contDisponibles!=0):
            #ingreso del usuario para volver (o no) a ingresar a otro asiento
            reingreso=int(input("Desea seleccionar otro asiento? 1)SI.2)NO:"))
            while (reingreso<1 or reingreso>2):
                print("ingreso incorrecto, vuelva a ingresar")
                reingreso=int(input("Desea seleccionar otro asiento? 1)SI.2)NO:"))
        else:
            print("La sala esta completa")
            reingreso=2
    for j in range(len(asientosElegidos)):
        for i in range(len(asientosDisponibles)):
            #busca en la lista los asientos seleccionados por el usuario
            if asientosElegidos[j]==asientosDisponibles[i]:
                #Cambia el valor del asiento de Vacio a Ocupado
                asientos[i]=True
    #Devuelve la cantidad reservada para usarla en el calculo de recaudación
    return cantidadReservados

def mostrarAsientos(asientosFuncion,cantFilas,cantColumnas):
    #Se muestran los Asientos: X para los ocupados y O para los Libres
    for j in range (cantFilas):
        print("")
        for i in range(cantColumnas):
            if (asientosFuncion[i+(j*cantColumnas)]==True):
                print("X",end=" ")
            else:
                print("O",end=" ")
    print("")

def main():
    #Los asientos que tendran todas las funciones
    cantAsientos=30
    #Variable utilizado para salir del bucle en el menu
    salir=0
    #Cantidad de filas y columnas que tendran las salas
    #IMPORTANTE: las filas y columnas deben concordar con la cantidad total de asientos.
    #la formula debe cumplirse: cantFilas*cantColumnas == cantAsientos
    cantFilas=3
    cantColumnas=10
    #Peliculas,fechas y horarios disponibles
    peliculas=["Hereditary","Scott Pilgrim vs. The World","The Truman Show"]
    fechas=["30/7/2025","31/7/2025","1/8/2025"]
    horarios=["9:00","12:00","18:00"]
    # precios por funcion
    precios = [1200, 1500, 1000]
    # recaudado por funcion
    recaudaciones = [0, 0, 0]
    
    #Se crean las listas de asientos por funcion
    #True significa que esta ocupado
    #False significa que el asiento esta vacio
    asientosFuncion1=[]
    #Se llena la lista con n cantidad de asientos vacios
    for i in range(cantAsientos):
        asientosFuncion1.append(False)
    #Un indice que sera utilizado para saber si un asiento en especifico esta ocupado o vacio
    asientosDisponibles1=[]
    #Se llena la lista de asientos disponibles con todos los numeros hasta el asiento disponible
    #ej: si tengo 30 asientos, se llenaran de datos del 1 al 30
    for i in range(cantAsientos):
        asientosDisponibles1.append(i)
        
    asientosFuncion2=[]
    for i in range(cantAsientos):
        asientosFuncion2.append(False)
    asientosDisponibles2=[]
    for i in range(cantAsientos):
        asientosDisponibles2.append(i)
    
    asientosFuncion3=[]
    for i in range(cantAsientos):
        asientosFuncion3.append(False)
    asientosDisponibles3=[]
    for i in range(cantAsientos):
        asientosDisponibles3.append(i)
    
    #Bucle del menu
    while(salir!=2):
        #menu
        print("-------------------------------------------")
        print("1) Mostrar Cartelera")
        print("2) Reservar Asiento")
        print("3) Mostrar Asientos Disponibles")
        print("4) Borrar Reserva Asiento")
        print("5) Ver Recaudación por Función")
        print("6) Salir del Menu ")
        #eleccion del usuario sobre que funcion realizara
        opc=int(input("Seleccione La opcion: "))
        #Reingreso si el usuario se equivoca
        while (opc<1 or opc >6):
            print("Opcion Incorrecta, vuelva a ingresar:")
            print("1) Mostrar Cartelera")
            print("2) Reservar Asiento")
            print("3) Mostrar Asientos Disponibles")
            print("4) Borrar Reserva Asiento")
            print("5) Ver Recaudación por Función")
            print("6) Salir del Menu ")
            opc=int(input("Seleccione La opcion: "))
        #Se realizan las operaciones que el usuario elija
        if (opc==1):
            mostrarCartelera(peliculas,fechas,horarios,precios)
            
        elif (opc==2):
            estados=mostrarEstadoSala(asientosFuncion1,asientosFuncion2,asientosFuncion3)
            prohibir=prohibirSalaCompleta(estados)
            if(prohibir[0]==1 and prohibir[1]==1 and prohibir[2]==1):
                print("Lo sentimos no hay funciones disponibles")
            else:
                #La pelicula elegida por el usuario
                peliculaElegida=seleccionarFuncion(peliculas,fechas,horarios,prohibir,"agregar",precios)
                #Dependiendo de la pelicula elegida
                if (peliculaElegida==1):
                    cantidad = seleccionarAsiento(asientosFuncion1, asientosDisponibles1)
                    recaudaciones[0] += cantidad * precios[0]
                elif (peliculaElegida==2):
                    cantidad = seleccionarAsiento(asientosFuncion2, asientosDisponibles2)
                    recaudaciones[1] += cantidad * precios[1]                    
                elif (peliculaElegida==3):
                    cantidad = seleccionarAsiento(asientosFuncion3, asientosDisponibles3)
                    recaudaciones[2] += cantidad * precios[2]
                    
        elif (opc==3):
            #se muestran las peliculas
            mostrarCartelera(peliculas,fechas,horarios,precios)
            #Variable usada cuando el usuario desea ver mas de una sala
            reingreso=1
            while(reingreso==1):
                #Variable que determina si una sala es elegible
                valido=0
                #bucle mientras el ingreso sea invalido
                while (valido==0):
                    #se le solicita al usuario que elija la funcion para ver sus asientos
                    peliculaElegida=int(input("De que funcion desea ver la disponibilidad de los asientos: "))
                    if (peliculaElegida==1):
                        mostrarAsientos(asientosFuncion1,cantFilas,cantColumnas)
                        valido=1
                    elif (peliculaElegida==2):
                        mostrarAsientos(asientosFuncion2,cantFilas,cantColumnas)
                        valido=1
                    elif (peliculaElegida==3):
                        mostrarAsientos(asientosFuncion3,cantFilas,cantColumnas)
                        valido=1
                    else:
                        print("Opcion Incorrecta Vuelva a ingresar")
                        
                reingreso=int(input("Desea ver otras opciones? 1) SI. 2) NO: "))
                #verificacion de variables
                while (reingreso <1 or reingreso>2):
                    print("Opcion incorrecta, vuelva a ingresar.")
                    reingreso=int(input("Desea ver otras opciones? 1) SI. 2) NO: "))
                
        elif (opc==4):
            estados=mostrarEstadoSala(asientosFuncion1,asientosFuncion2,asientosFuncion3)
            prohibir=prohibirSalaVacia(estados)
            if(prohibir[0]==1 and prohibir[1]==1 and prohibir[2]==1):
                print("todas las funciones estan vacias")
            else:
                #La pelicula elegida por el usuario
                peliculaElegida=seleccionarFuncion(peliculas,fechas,horarios,prohibir,"borrar",precios)
                #Dependiendo de la pelicula elegida
                if (peliculaElegida==1):
                    cantidad=borrarRegistroAsiento(asientosFuncion1,asientosDisponibles1)
                    recaudaciones[0] -= cantidad * precios[0]
                elif (peliculaElegida==2):
                    cantidad=borrarRegistroAsiento(asientosFuncion2,asientosDisponibles2)
                    recaudaciones[1] -= cantidad * precios[1]
                elif (peliculaElegida==3):
                    cantidad=borrarRegistroAsiento(asientosFuncion3,asientosDisponibles3)
                    recaudaciones[2] -= cantidad * precios[2]
        elif (opc==5):
            #Muestra la recaudacion de las peliculas
            for i in range(len(peliculas)):
                print(f"{peliculas[i]}: ${recaudaciones[i]}")
                
        elif (opc==6):
            salir=2

        if(salir!=2):
            #Se pregunta al usuario si desea volver al menu
            salir=int(input("Desea volver al menu? 1) SI. 2) NO: "))
            while (salir <1 or salir>2):
                print("Opcion incorrecta, vuelva a ingresar.")
                salir=int(input("Desea volver al menu? 1) SI. 2) NO: "))
    print("----------------------------------------------------")
    print("Programa finalizado")
    print("Gracias por utilizar nuestros servicios")
main()
