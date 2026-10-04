import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                port=DB_PORT
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("✅ Conexión a BD exitosa")
        except mysql.connector.Error as err:
            print(f"❌ Error en conexión: {err}")

    def desconectar(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    # ===== USUARIOS TELEGRAM =====
    def obtener_usuario_telegram(self, telegram_id):
        query = "SELECT * FROM usuarios_telegram WHERE telegram_id = %s"
        self.cursor.execute(query, (telegram_id,))
        return self.cursor.fetchone()

    def registrar_usuario_telegram(self, telegram_id, nombre_usuario):
        query = """
        INSERT INTO usuarios_telegram (telegram_id, nombre_usuario, creditos, plan)
        VALUES (%s, %s, 0, 'gratis')
        """
        self.cursor.execute(query, (telegram_id, nombre_usuario))
        self.connection.commit()

    def obtener_creditos(self, telegram_id):
        usuario = self.obtener_usuario_telegram(telegram_id)
        return usuario['creditos'] if usuario else 0

    def restar_creditos(self, telegram_id, cantidad):
        query = "UPDATE usuarios_telegram SET creditos = creditos - %s WHERE telegram_id = %s"
        self.cursor.execute(query, (cantidad, telegram_id))
        self.connection.commit()

    def agregar_creditos(self, telegram_id, cantidad, admin_id=None, razon=""):
        # Actualizar créditos
        query = "UPDATE usuarios_telegram SET creditos = creditos + %s WHERE telegram_id = %s"
        self.cursor.execute(query, (cantidad, telegram_id))

        # Registrar transacción
        query_trans = """
        INSERT INTO transacciones_creditos (usuario_telegram_id, tipo, cantidad, razon, admin_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query_trans, (telegram_id, 'suma', cantidad, razon, admin_id))
        self.connection.commit()

    # ===== BÚSQUEDAS =====
    def buscar_por_dni(self, dni):
        query = "SELECT * FROM usuarios_juego WHERE dni = %s AND activo = TRUE"
        self.cursor.execute(query, (dni,))
        return self.cursor.fetchone()

    def buscar_por_telefono(self, telefono):
        query = "SELECT * FROM usuarios_juego WHERE telefoneo = %s AND activo = TRUE"
        self.cursor.execute(query, (telefono,))
        return self.cursor.fetchone()

    def buscar_por_nombre(self, nombre):
        query = "SELECT * FROM usuarios_juego WHERE nombre_completo LIKE %s AND activo = TRUE LIMIT 5"
        self.cursor.execute(query, (f"%{nombre}%",))
        return self.cursor.fetchall()

    def registrar_busqueda(self, telegram_id, tipo, criterio, usuario_encontrado_id, creditos_gastados):
        query = """
        INSERT INTO busquedas (usuario_telegram_id, tipo_busqueda, criterio, usuario_encontrado_id, creditos_gastados)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (telegram_id, tipo, criterio, usuario_encontrado_id, creditos_gastados))
        self.connection.commit()

    # ===== USUARIOS JUEGO =====
    def obtener_usuario_juego(self, usuario_id):
        query = "SELECT * FROM usuarios_juego WHERE id = %s"
        self.cursor.execute(query, (usuario_id,))
        return self.cursor.fetchone()

# Instancia global
db = Database()
