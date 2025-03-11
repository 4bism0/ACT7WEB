import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("escuela_robotica.db")
cursor = conn.cursor()

# Abrir un archivo y guardar el dump
with open("actividad7.sql", "w") as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")

conn.close()
print("Base de datos exportada a actividad7.sql")