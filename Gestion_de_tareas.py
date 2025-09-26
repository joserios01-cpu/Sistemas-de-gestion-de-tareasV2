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
        
        