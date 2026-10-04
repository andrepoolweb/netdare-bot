"""Script para insertar datos de prueba en la BD"""
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

# Usuarios de prueba realistas peruanos
USUARIOS_PRUEBA = [
    {
        'dni': '12345678',
        'nombre': 'Juan Carlos Mendoza',
        'telefono': '987654321',
        'edad': 28,
        'profesion': 'Policía',
        'dinero': 50000,
        'nivel': 15,
        'estado_civil': 'Soltero'
    },
    {
        'dni': '24681379',
        'nombre': 'María García López',
        'telefono': '985432109',
        'edad': 25,
        'profesion': 'Abogada',
        'dinero': 75000,
        'nivel': 12,
        'estado_civil': 'Casada'
    },
    {
        'dni': '36925814',
        'nombre': 'Carlos Antonio Ramos',
        'telefono': '981234567',
        'edad': 35,
        'profesion': 'Mecánico',
        'dinero': 30000,
        'nivel': 8,
        'estado_civil': 'Divorciado'
    },
    {
        'dni': '44885522',
        'nombre': 'Rosa Martínez Silva',
        'telefono': '984567890',
        'edad': 42,
        'profesion': 'Enfermera',
        'dinero': 45000,
        'nivel': 10,
        'estado_civil': 'Viuda'
    },
    {
        'dni': '15963852',
        'nombre': 'Fernando Quispe Huanca',
        'telefono': '986789012',
        'edad': 31,
        'profesion': 'Vendedor',
        'dinero': 20000,
        'nivel': 5,
        'estado_civil': 'Soltero'
    },
    {
        'dni': '25874136',
        'nombre': 'Sandra Patricia Torres',
        'telefono': '989012345',
        'edad': 29,
        'profesion': 'Contadora',
        'dinero': 85000,
        'nivel': 18,
        'estado_civil': 'Casada'
    },
    {
        'dni': '36741963',
        'nombre': 'Roberto Luis Castillo',
        'telefono': '982345678',
        'edad': 45,
        'profesion': 'Taxista',
        'dinero': 15000,
        'nivel': 4,
        'estado_civil': 'Casado'
    },
    {
        'dni': '47852369',
        'nombre': 'Daniela Morales Rojas',
        'telefono': '987654098',
        'edad': 23,
        'profesion': 'Estudiante',
        'dinero': 5000,
        'nivel': 2,
        'estado_civil': 'Soltera'
    },
    {
        'dni': '58963741',
        'nombre': 'Miguel Ángel Flores',
        'telefono': '981098765',
        'edad': 38,
        'profesion': 'Ingeniero',
        'dinero': 120000,
        'nivel': 25,
        'estado_civil': 'Casado'
    },
    {
        'dni': '69074852',
        'nombre': 'Alejandra Cruz Vega',
        'telefono': '983210987',
        'edad': 26,
        'profesion': 'Diseñadora',
        'dinero': 35000,
        'nivel': 7,
        'estado_civil': 'Soltera'
    }
]

def insertar_datos():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        cursor = conexion.cursor()

        query = """
        INSERT INTO usuarios_juego
        (dni, nombre_completo, telefoneo, edad, profesion, dinero_juego, nivel, estado_civil)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        for usuario in USUARIOS_PRUEBA:
            try:
                cursor.execute(query, (
                    usuario['dni'],
                    usuario['nombre'],
                    usuario['telefono'],
                    usuario['edad'],
                    usuario['profesion'],
                    usuario['dinero'],
                    usuario['nivel'],
                    usuario['estado_civil']
                ))
                print(f"✅ Insertado: {usuario['nombre']}")
            except mysql.connector.Error as err:
                print(f"⚠️  Error en {usuario['nombre']}: {err}")

        conexion.commit()
        cursor.close()
        conexion.close()
        print("\n✅ Datos de prueba insertados correctamente")

    except mysql.connector.Error as err:
        print(f"❌ Error de conexión: {err}")

if __name__ == '__main__':
    print("Insertando datos de prueba...")
    insertar_datos()
