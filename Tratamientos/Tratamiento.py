from Usuarios import Conexion as conexion


connect = conexion.conectar()  
dataBase = connect[0]
cursor = connect[1]


class Tratamiento:

    def __init__(self, paciente_id, fecha_inic, tipo, duracion):
        self.paciente_id = paciente_id
        self.fecha_inic = fecha_inic
        self.tipo = tipo 
        self.duracion = duracion
    
    def crear(self):
        

        sql = "INSERT INTO tratamientos VALUES (null, %s, %s, %s, %s)"
        tratamiento = (self.paciente_id, self.fecha_inic, self.tipo, self.duracion)
    
        try:
            print(f"Ejecutando SQL: {sql} con datos: {tratamiento}")  # Agrega esta línea para depurar
            cursor.execute(sql, tratamiento)
            dataBase.commit()
            resultado = [cursor.rowcount, self]
        except Exception as e:
            print(f"Error al crear visita: {e}")  # Muestra el error si ocurre
            resultado = [0, self]
    
        return resultado