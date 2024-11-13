from Usuarios import Conexion as conexion
import datetime

connect = conexion.conectar()  
dataBase = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellido, correo, password, rol_id):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo 
        self.password = password
        self.rol_id = rol_id

    def registro(self):

        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.correo, self.password, self.rol_id)

        try:
            cursor.execute(sql, usuario)
            dataBase.commit()
            resultado = [cursor.rowcount, self]
            
        except: 
            resultado = [0, self]

        return resultado
    
    def identificar(self):
        sql = f"SELECT * FROM usuarios WHERE correo = %s AND password = %s"
        usuario = (self.correo, self.password)

        cursor.execute(sql, usuario)
        resultado = cursor.fetchone()

        return resultado

    

         