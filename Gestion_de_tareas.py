import json
from datetime import datetime

# CLase tarea
class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completado = False # hasta que nosotros no le demos una indicacion de completado, debe mantenerse
        # en falso
    def marcar_completado(self):
        self.completado = True
        
    def editar_tarea(self, nuevo_titulo, nueva_descripcion, nueva_fecha):
        self.nuevotitulo = nuevo_titulo
        self.nuevadescripcion = nueva_descripcion
        self.nuevafecha = nueva_fecha
        
# clase usuario
class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.tareas = []
        
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        
    def eliminar_tarea(self, titulo_tarea):
        self.tareas = {tarea for tarea in self.tareas if tarea.titulo != titulo_tarea}
        # Recorre toda la lista de tareas hasta llegar a la tarea que tenga el titulo igual al ingresado
        
    def obtener_tareas(self):
        return self.tareas