import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
conexion.execute("PRAGMA foreign_keys = ON")

# En una cadena guardaremos el script de creacion de la tabla pais
tabla_pais = """CREATE TABLE pais(
                    idpais INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE,
                    estado TEXT
                    )

                                """
tabla_editorial = """ CREATE TABLE editorial(
                        ideditorial INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        estado TEXT
                    )
            """

tabla_autor = """ CREATE TABLE autor(
                    idautor INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    f_nacimiento TEXT
                    )
            """
tabla_libro = """ CREATE TABLE libro(
                    idlibro INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    cantidad INTEGER,
                    anio INTEGER,
                    precio REAL,
                    estado TEXT,
                    idpais INTEGER REFERENCES pais,
                    ideditorial INTEGER REFERENCES editorial,
                    idautor INTEGER REFERENCES autor,

                    FOREIGN KEY (idpais) REFERENCES pais(idpais),
                    FOREIGN KEY (ideditorial) REFERENCES pais(idpais),
                    FOREIGN KEY (idautor) REFERENCES pais(idautor)
                    )
            """

cursor = conexion.cursor()
cursor.execute(tabla_pais)
cursor.execute(tabla_editorial)
cursor.execute(tabla_libro)
cursor.execute(tabla_autor)
conexion.commit()
conexion.close()
