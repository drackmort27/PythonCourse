import _sqlite3

conexion = _sqlite3.connect("mi_base_de_datos.db")

cursor = conexion.cursor()

##cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
##cursor.execute("INSERT INTO usuarios VALUES ('Juan', 30, 'juan@example.com')")


#usuarios = [ ('Pedro', 31, 'pedro@example.com'), ('Maria', 25, 'maria@example.com') ,('Pedro', 40, 'pedro@example.com')]

#cursor.executemany("INSERT INTO usuarios VALUES (?, ?, ?)", usuarios)

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)



conexion.commit()
conexion.close()
