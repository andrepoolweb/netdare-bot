# 🚀 GUÍA RÁPIDA PARA COMENZAR

## Paso 1: Preparar la Base de Datos

```bash
# Abre tu cliente MySQL (phpMyAdmin o terminal)
# Ejecuta el archivo: database/schema.sql

# O en terminal:
mysql -u root -p < database/schema.sql
```

## Paso 2: Obtener Token de Telegram

1. Abre Telegram y busca `@BotFather`
2. Usa `/newbot` y sigue las instrucciones
3. Copia el token que te da

## Paso 3: Obtener tu ID de Telegram

1. Abre Telegram y busca `@userinfobot`
2. Escribe `/start`
3. Copia tu ID

## Paso 4: Configurar el Proyecto

1. Copia `.env.example` a `.env`
```bash
cp .env.example .env
```

2. Edita `.env` con tus datos:
```
BOT_TOKEN=Tu_Token_Aqui
ADMIN_ID=Tu_ID_Aqui
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=netdare_db
```

## Paso 5: Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Paso 6: Insertar Datos de Prueba

```bash
python datos_prueba.py
```

Deberías ver:
```
✅ Insertado: Juan Carlos Mendoza
✅ Insertado: María García López
...
✅ Datos de prueba insertados correctamente
```

## Paso 7: Ejecutar el Bot

```bash
python bot.py
```

Deberías ver:
```
✅ Conexión a BD exitosa
✅ Bot listo. Escuchando mensajes...
```

## Paso 8: Testear el Bot

1. En Telegram, busca tu bot por nombre
2. Usa `/start`
3. Haz clic en botones
4. Prueba una búsqueda

**Ejemplo de búsqueda:**
- Click en "🔍 Buscar por DNI"
- Escribe: `12345678`
- Recibirás la información de Juan Carlos Mendoza

## ✅ Checklist

- [ ] Base de datos creada
- [ ] Token de Telegram obtenido
- [ ] ID de Telegram obtenido
- [ ] .env configurado
- [ ] Dependencias instaladas
- [ ] Datos de prueba insertados
- [ ] Bot ejecutándose
- [ ] Bot funciona en Telegram

## 🆘 Problemas Comunes

**Error: "No module named 'mysql'"**
```bash
pip install mysql-connector-python
```

**Error: "Connection refused"**
- Verifica que MySQL esté ejecutándose
- Comprueba usuario/contraseña en .env

**Bot no responde**
- Verifica que el token sea correcto
- Verifica que el bot esté en ejecución

## 📞 Próximos Pasos

1. Crear más usuarios de prueba
2. Hacer pruebas de carga
3. Implementar panel web de admin
4. Agregar más funciones (árbol genealógico, denuncias)
5. Desplegar en servidor gratuito (Railway, Render)

¡Listo! Tu bot está funcionando. 🎉
