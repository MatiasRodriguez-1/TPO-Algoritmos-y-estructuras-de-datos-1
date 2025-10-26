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

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
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
    nombre_valido = False
    while not nombre_valido:
        usuario = input("Nuevo usuario: ")
        if any(u["usuario"] == usuario for u in usuarios):
            print("Ese nombre de usuario ya existe. Elegí otro.")
        elif usuario == "":
            print("El nombre de usuario no puede ser dejado en blanco")
        else:
            nombre_valido = True

    print("La contraseña debe tener al menos 8 caracteres, una mayúscula y un número.")
    contraseña_valida = False
    while not contraseña_valida:
        contraseña = input("Contraseña: ")
        tiene_mayus = any(ch.isupper() for ch in contraseña)
        tiene_numero = any(ch.isdigit() for ch in contraseña)
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
    print("Usuario creado con éxito.")

# ------------------ FUNCIONES DE CINE ------------------ #
def mostrarCartelera(peliculas):
    print("-------------------------------------------")
    if len(peliculas) > 0:
        for i, peli in enumerate(peliculas, start=1):
            print(f"{i}) {peli['titulo']} - {peli['fecha']} {peli['horario']} - ${peli['precio']}")
    else:
        print("No hay peliculas disponibles")

def mostrarEstadoSala(peliculas):
    estados=[]
    for peli in peliculas:
        ocupados = sum(peli["asientos"])
        if ocupados == len(peli["asientos"]):
            estados.append(1)  # lleno
        elif ocupados == 0:
            estados.append(0)  # vacio
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
        try:
            asientoElegido=int(input("Seleccione asiento a liberar: ")) - 1
            if 0 <= asientoElegido < len(asientos) and asientos[asientoElegido] and asientoElegido not in asientosElegidos:
                print("Reserva eliminada correctamente")
                asientosElegidos.append(asientoElegido)
                contOcupados -= 1
                cantidadEliminados += 1
            else:
                print("Asiento inválido o ya libre")
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
        asientos[asiento] = True
        
    return cantidadReservados

def mostrarAsientos(asientosFuncion,cantFilas,cantColumnas):
    for j in range(cantFilas):
        for i in range(cantColumnas):
            print("X" if asientosFuncion[i+j*cantColumnas] else "O", end=" ")
        print("")
    print("")

def eliminarPelicula(peliculas):
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
    print("Pelicula eliminada correctamente")

def agregarPelicula(peliculas,cantAsientos):
    nombreValido = False
    while (nombreValido==False):
        nombre = input("Nombre de la película: ")
        if nombre == "":
            print("El nombre no puede estar vacío")
        elif any(p["titulo"].lower() == nombre.lower() for p in peliculas):
            print("Ya existe una película con ese nombre. Ingrese otro nombre.")
        else:
            nombreValido = True

    fecha=input("Fecha: ")
    while(fecha==""):
        print("la fecha no puede estar vacia")
        fecha=input("Fecha: ")
    horario=input("Horario: ")
    while(horario==""):
        print("el horario no puede estar vacio")
        horario=input("Horario: ")
        
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
    asientosFuncion=[False for _ in range (cantAsientos)]
    peliculas.append({
        "titulo": nombre,
        "fecha": fecha,
        "horario": horario,
        "precio": precio,
        "recaudacion": 0,
        "asientos": asientosFuncion
    })
    print(f'Película "{nombre}" agregada correctamente.')

# ------------------ MAIN ------------------ #

def main():
    rol, usuario = login()
    while (rol == None):
        print("Usuario invalido")
        print("Volviendo a la pantalla de login")
        rol, usuario = login()

    print(f"Acceso concedido: {usuario} ({rol})")

    cantAsientos=30
    cantFilas=3
    cantColumnas=10

    peliculas=[
        {"titulo":"Hereditary","fecha":"30/7/2025","horario":"9:00","precio":1200,"recaudacion":0,"asientos":[False for _ in range(cantAsientos)]},
        {"titulo":"Scott Pilgrim vs. The World","fecha":"31/7/2025","horario":"12:00","precio":1500,"recaudacion":0,"asientos":[False for _ in range(cantAsientos)]},
        {"titulo":"The Truman Show","fecha":"1/8/2025","horario":"18:00","precio":1000,"recaudacion":0,"asientos":[False for _ in range(cantAsientos)]}
    ]

    salir=0
    while salir!=2:
        print("-------------------------------------------")
        opcAdmin=opcUser=opcGuest=0

        if (rol=="Admin"):
            print("1) Mostrar Cartelera\n2) Reservar Asiento\n3) Mostrar Asientos Disponibles\n4) Borrar Reserva Asiento\n5) Ver Recaudación\n6) Eliminar Pelicula\n7) Agregar Pelicula\n8) Salir")
            opcValido=False
            while (opcValido==False):         
                try:
                    opcAdmin=int(input("Seleccione opción: "))
                    if (opcAdmin>0 and opcAdmin<9):
                        opcValido=True
                    else:
                        print("El numero debe estar entre (1-8)")
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
            if all(p==1 for p in prohibir):
                print("No hay funciones disponibles")
            else:
                peliculaElegida = seleccionarFuncion(peliculas,prohibir,"agregar")
                cantidad = seleccionarAsiento(peliculas[peliculaElegida-1]["asientos"])
                peliculas[peliculaElegida-1]["recaudacion"] += cantidad * peliculas[peliculaElegida-1]["precio"]

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
                cantidad = borrarRegistroAsiento(peliculas[peliculaElegida-1]["asientos"])
                peliculas[peliculaElegida-1]["recaudacion"] -= cantidad * peliculas[peliculaElegida-1]["precio"]

        elif (opcAdmin==5):
            for peli in peliculas:
                print(f"{peli['titulo']}: ${peli['recaudacion']}")

        elif (opcAdmin==6):
            mostrarCartelera(peliculas)
            eliminarPelicula(peliculas)

        elif (opcAdmin==7):
            agregarPelicula(peliculas,cantAsientos)

        elif (opcAdmin==8 or opcUser==5 or opcGuest==3):
            # ======= NUEVO: submenú para decidir volver al login o salir =======
            print("¿Qué desea hacer?")
            print("1) Volver al menú de login")
            print("2) Salir del programa")
            sub = 0
            while sub not in [1, 2]:
                try:
                    sub = int(input("Seleccione opción (1-2): "))
                except ValueError:
                    print("Ingrese un número válido (1-2)")
            if sub == 1:
                # Volver al login SIN terminar el programa
                return main()   # relanza login y menú (conserva tus líneas)
            else:
                # (antes: salir=2)  <-- línea original conservada como comentario
                salir = 2       # misma semántica que tu código: cierra el bucle y cae al final

        if salir != 2:
            salir = 0
            while salir not in [1, 2]:
                try:
                    salir = int(input("¿Desea volver al menú? 1)SI 2)NO: "))
                    if salir not in [1, 2]:
                        print("Ingrese un número válido (1-2)")
                except ValueError:
                    print("No se permiten caracteres, solo números")

            # ======= NUEVO: si el usuario NO quiere volver al menú, ofrecer volver al LOGIN =======
            if salir == 2:
                volver_login = 0
                while volver_login not in [1, 2]:
                    try:
                        volver_login = int(input("¿Querés volver al menú de login? 1)SI 2)NO: "))
                        if volver_login not in [1, 2]:
                            print("Ingrese un número válido (1-2)")
                    except ValueError:
                        print("No se permiten caracteres, solo números")
                if volver_login == 1:
                    return main()  # reingresa al login sin finalizar
                else:
                    salir = 2     # mantiene el flujo original: cerrar menú y caer al final
            
    # ------------------ AGRGAMOS ALGO DE CONJUNTOS ------------------ #
    print("\n=== Ejemplo de uso de conjuntos ===")

    # Crear un conjunto con los roles existentes
    roles_existentes = {u["rol"] for u in usuarios}
    print("Roles existentes en el sistema:", roles_existentes)

    # Crear un conjunto con todos los nombres de usuario
    nombres_usuarios = {u["usuario"] for u in usuarios}

    # Agregar un usuario duplicado para mostrar la propiedad de unicidad
    nombres_usuarios.add("admin")
    print("Usuarios registrados (sin duplicados gracias al conjunto):", nombres_usuarios)

    # Diferencia de conjuntos (usuarios y roles)
    print("Cantidad total de usuarios:", len(nombres_usuarios))
    print("Cantidad total de roles:", len(roles_existentes))

    print("----------------------------------------------------\nPrograma finalizado\nGracias por utilizar nuestros servicios")

main()
