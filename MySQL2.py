import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="test"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejemplo: Insertar un estudiante n la tabla de estudiantes
estudiantes = 1
nombre = "Juan "
apellido = "gonzales"
DNI= 20.343.434
telefono=+5415343443
direccion= 12334
fechadenacimiento= 2002/12/8
# Consulta SQL para la inserción
consulta = "INSERT INTO estudiantes (estudiantes, nombre, DNI, direccion, fechadenacimiento,telefono,apellido) VALUES (%s, %s, %s, %s, %s, %s, %s)"
datos = (estudiantes, nombre, DNI, apellido, direccion,fechadenacimiento,telefono)

# Ejecutar la consulta
cursor.execute(consulta, datos)

# Confirmar los cambios en la base de datos
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()