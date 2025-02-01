import sqlite3

try:
    # Conectar la base de datos
    mi_conexion = sqlite3.connect("database/db_meagendo")
    cursor = mi_conexion.cursor()

    # Crear la tabla usuarios
    cursor.execute("""
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY,
            nombre VARCHAR(50),
            imagen_perfil BLOB,
            clave VARCHAR(50),
            ultimo_inicio_de_sesion DATETIME
        )
    """)

    # Crear la tabla cuestionario
    cursor.execute("""
        CREATE TABLE cuestionario (
            id INTEGER PRIMARY KEY,
            Usuario_id INTEGER,
            objetivo_principal TEXT CHECK(objetivo_principal IN ('Estudiar', 'Trabajar')),
            nivel_educativo TEXT CHECK(nivel_educativo IN ('Educacion primaria', 'Educacion secundaria', 'Educacion universitaria', 'Educacion de Posgrado')),
            horario_de_estudio TIME,
            horario_de_trabajo TIME,
            FOREIGN KEY (Usuario_id) REFERENCES usuarios(id)
        )
    """)

    # Crear la tabla Preferencias
    cursor.execute("""
        CREATE TABLE Preferencias (
            id INTEGER PRIMARY KEY,
            Usuario_id INTEGER,
            Horario_inicio_trabajo TIME,
            Horario_fin_trabajo TIME,
            Notificaciones_activadas BOOLEAN,
            Tema TEXT CHECK(Tema IN ('Claro', 'Oscuro')),
            Configuracion_predeterminada BOOLEAN,
            Sidebar_posicion TEXT CHECK(Sidebar_posicion IN ('Izquierda', 'Derecha')),
            Idioma TEXT CHECK(Idioma IN ('Espanol', 'Ingles')),
            Frecuencia_notificaciones TEXT CHECK(Frecuencia_notificaciones IN ('Diario', 'Semanal', 'Mensual')),
            Efectos_de_sonido_activados BOOLEAN,
            FOREIGN KEY (Usuario_id) REFERENCES usuarios(id)
        )
    """)

    # Crear tabla Tareas
    cursor.execute("""
        CREATE TABLE Tareas (
            id INTEGER PRIMARY KEY,
            Usuario_id INTEGER,
            Recordatorio_id INTEGER,
            Titulo VARCHAR(50),
            Descripcion VARCHAR(250),
            Prioridad TEXT CHECK(Prioridad IN ('Baja', 'Media', 'Alta')),
            Fecha_limite DATETIME,
            Estado TEXT CHECK(Estado IN ('Pendiente', 'En progreso', 'Terminada', 'Atrasada')),
            Categoria TEXT CHECK(Categoria IN ('Trabajo', 'Estudio', 'Personal', 'Salud', 'Urgente')),
            FOREIGN KEY (Usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (Recordatorio_id) REFERENCES recordatorio(id)
        )
    """)

    # Crear tabla Eventos
    cursor.execute("""
        CREATE TABLE Eventos (
            id INTEGER PRIMARY KEY,
            Usuario_id INTEGER,
            Recordatorio_id INTEGER,
            Titulo VARCHAR(50),
            Descripcion VARCHAR(500),
            Fecha_limite DATETIME,
            Categoria TEXT CHECK(Categoria IN ('Trabajo', 'Estudio', 'Personal', 'Salud', 'Urgente')),
            Ubicacion VARCHAR(100),
            Fecha_Hora DATETIME,
            FOREIGN KEY (Usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (Recordatorio_id) REFERENCES recordatorio(id)
        )
    """)

    # Crear tabla Recordatorios
    cursor.execute("""
        CREATE TABLE Recordatorios (
            id INTEGER PRIMARY KEY,
            Usuario_id INTEGER,
            Titulo VARCHAR(50),
            Descripcion VARCHAR(100),
            Fecha_hora DATETIME,
            Repetir BOOLEAN,
            Frecuencia_repeticion TEXT CHECK(Frecuencia_repeticion IN ('Diaria', 'Semanal', 'Mensual')),
            Notificacion BOOLEAN,
            FOREIGN KEY (Usuario_id) REFERENCES usuarios(id)
        )
    """)

    # Crear tabla Configuracion_Pomodoro
    cursor.execute("""
        CREATE TABLE Configuracion_Pomodoro (
            id INTEGER PRIMARY KEY,
            Usuario_id INTEGER,
            Duracion_trabajo INTEGER,
            Duracion_descanso INTEGER,
            Numero_pomodoros TEXT CHECK(Numero_pomodoros IN ('1', '2', '3', '4', '5', '6', '7', '8')),
            Musica_fondo BOOLEAN,
            Seleccion_musica TEXT CHECK(Seleccion_musica IN ('Instrumental 1', 'Instrumental 2', 'Instrumental 3', 'Importar audio')),
            Ruta_musica_importada TEXT,
            FOREIGN KEY (Usuario_id) REFERENCES usuarios(id)
        )
    """)

except Exception as ex:
    print(f"Error {ex}")

finally:
    # Cerrar conexion
    if mi_conexion:
        mi_conexion.close()
