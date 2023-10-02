import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='danilo',
    password='Skittles1996',
    database='prueba'
)

cursor = midb.cursor()

#listar datos
""" cursor.execute('select * from Usuario')
resultado = cursor.fetchall() #llama a todos
#resultado = cursor.fetchone() #llama al primer elemento que encuentre
print(resultado) """


#limit = mostrar la cantidad de elemntos que establescas 
cursor.execute('select * from Usuario limit 2')
resultado = cursor.fetchall() 
print(resultado)

#ver definiciones de tablas
#cursor.execute('show create table Usuario')

#insertar datos
#sql = 'insert into Usuario(email, username, edad) values(%s, %s, %s)'
#values = ('micorreo@correo.com', 'nombreusuario', 45)


#actualizar datos
""" sql = 'update Usuario set email = %s where id = %s'
values = ('correo@correo.com', 4)
cursor.execute(sql, values)
midb.commit()
print(cursor.rowcount) """

#eliminar datos
""" sql = 'delete from Usuario where id = %s'
values = (4,)
cursor.execute(sql, values)
midb.commit() """







