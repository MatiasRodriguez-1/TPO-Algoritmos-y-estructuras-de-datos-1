# CineApp 🎬

Proyecto de simulación de un sistema de cine, desarrollado en Python como trabajo práctico de la materia **Algoritmia y Programación**.

##  Funcionalidades principales
- Login con usuarios, roles y validación de credenciales.
- Roles disponibles:
  - **Admin**: puede agregar/eliminar películas, ver recaudación, gestionar reservas.
  - **User**: puede reservar y liberar asientos.
  - **Guest**: acceso limitado a visualización.
- Cartelera de películas con fechas, horarios y precios.
- Gestión de asientos (reservar, liberar, mostrar sala).
- Registro de recaudaciones por película.

##  Estructura del código
- 'login()' y 'registrarUsuario()' → Gestión de usuarios.
- Funciones de **cartelera**: `mostrarCartelera()`, `mostrarEstadoSala()`, etc.
- Funciones de **asientos**: `seleccionarAsiento()`, `mostrarAsientos()`, `borrarRegistroAsiento()`.
- Funciones de **películas**: `agregarPelicula()`, `eliminarPelicula()`.
- `main()` → Control principal del flujo del programa.

##  Validaciones incluidas
- Credenciales incorrectas → acceso denegado.
- Contraseñas seguras: al menos 8 caracteres, una mayúscula y un número.
- Asientos y opciones de menú validadas para evitar errores.
- No se puede reservar en una sala llena ni borrar en una sala vacía.

##  Futuras mejoras
- Guardar usuarios y películas en un archivo o base de datos.
- Uso de funciones `lambda` para simplificar filtros y búsquedas.
- Interfaz gráfica en lugar de consola.

## 👥 Equipo
Trabajo realizado por el grupo:  
- STANLEY PIERRE
- MATIAS RODRIGUEZ
- JOAQUIN LOPEZ
- FACUNDO BARBIERI 

