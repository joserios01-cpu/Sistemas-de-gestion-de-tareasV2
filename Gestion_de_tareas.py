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
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion
        self.fecha_vencimiento = nueva_fecha
        
# clase usuario
class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.tareas = []
        
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        
    def eliminar_tarea(self, titulo_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo_tarea]
        # Recorre toda la lista de tareas hasta llegar a la tarea que tenga el titulo igual al ingresado
        
    def obtener_tareas(self):
        return self.tareas

# Clase sistema de gestion de tareas
class SistemaGestionTareas:
    #Inicializacion de sistema de gestion de un archivo
    def __init__(self, archivos_datos = "datos_usuario.json"):
        self.usuarios = {}
        self.archivos_datos = archivos_datos
        self.cargar_datos()
        
    def cargar_datos(self):
        # Cargar datos del usuario en formato json
        try:
            with open(self.archivos_datos, "r") as archivo:
                datos = json.load(archivo)
                for nombre_usuario, info in datos.items():
                    # Crea un objeto usuario para cada usuario en los datos
                    usuario = Usuario(nombre_usuario, info["contrasena"])
                    for tarea_info in info["tareas"]:
                            # Crea un objeto tarea para cada tarea del usuario
                        tarea = Tarea(tarea_info["titulo"], tarea_info["descripcion"], tarea_info["fecha_vencimiento"])
                        tarea.completado = tarea_info["completado"]
                        usuario.agregar_tarea(tarea)
                    self.usuarios[nombre_usuario] = usuario
        except FileNotFoundError: # manejo de excepciones
            print("Archivo de datos no encontrado, se creara uno nuevo al guardar")
            
    def guardar_datos(self): 
        # Guardar los datos de los usuarios en el archivo
        datos = {} # Este es el diccionario de datos
        for nombre_usuario, usuario in self.usuarios.items():
            #Organiza las tareas e informacion del usuario en un diccinario
            datos[nombre_usuario] = {
                "contrasena": usuario.contrasena,
                "tareas": [
                    {"titulo" : tarea.titulo, "descripcion" : tarea.descripcion, "fecha_vencimiento" : tarea.fecha_vencimiento, "completado" : tarea.completado}
                    for tarea in usuario.tareas
                ]
            }            
        with open(self.archivos_datos, "w") as archivo:
            json.dump(datos, archivo)
            
            
    def registrar_usuario(self, nombre_usuario, contrasena):
        # Registrar un nuevo usuario si el nombre de usuario no existe
        if nombre_usuario in self.usuarios:
            print("El nombre de usuario ya existe")
            return False
        else:
            self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contrasena)
            self.guardar_datos()
            print("Usuario registrado con exito")
            return None
        
    def iniciar_sesion(self, nombre_usuario, contrasena):
        # Inicia sesion si el usuario y contrasena coinciden
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.contrasena == contrasena:
                print("Inicio de sesion exitoso")
                return usuario
        else:
            print("Nombre de usuario o contrasena incorrectos.")
            return None


        
    def menu_usuarios(self, usuario):
        while True:
            print("\n1. Crear Tarea")
            print("\n2. Ver Tarea")
            print("\n3. Editar Tarea")
            print("\n4. Completar Tarea")
            print("\n5. Eliminar Tarea")
            print("\n6. Cerrar sesion")
            
            opcion = input("Selecciona una opcion: ")
            if opcion == "1":
                titulo = input("Titulo de la tarea: ")
                descripcion = input("Ingresa la descripcion: ")
                fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
                tarea = Tarea(titulo, descripcion, fecha_vencimiento)
                usuario.agregar_tarea(tarea)
                self.guardar_datos()
                print("Tarea guardada con exito")
                
            elif opcion == "2":
                tareas = usuario.obtener_tareas()
                if not tareas:
                    print("No tienes tareas")
                for idx, tarea in enumerate(tareas, start=1):
                    estado = "Completado" if tarea.completado else "Pendiente"
                    print(f"{idx}. {tarea.titulo} = {estado} (Vence: {tarea.fecha_vencimiento})")
            
            elif opcion == "3":
                # Editar las tareas
                titulo_tarea = input("Titulo de la tarea a editar: ")
                tarea = next((t for t in usuario.tareas if t.titulo == titulo_tarea), None)
                if tarea:
                    nuevo_titulo = input("Nuevo titulo: ")
                    nueva_descripcion = input("Nueva descripcion: ")
                    nueva_fecha = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")
                    tarea.editar_tarea(nuevo_titulo, nueva_descripcion, nueva_fecha)
                    print("Tarea actualizada con exito")
                else:
                    print("Tarea no encontrada")

            elif opcion == "4":
                # Marcar como tarea completada
                titulo_tarea = input("Titulo de la tarea a completar: ")
                tarea = next((t for t in usuario.tareas if t.titulo == titulo_tarea), None)
                if tarea:
                    tarea.marcar_completado()
                    self.guardar_datos()
                    print("Tarea marcada como completada")
                else:
                    print("Tarea no encontrada")
                    
            elif opcion == "5":
                # Eliminar una tarea
                titulo_tarea = input("Titulo de la tarea a eliminar: ")
                usuario.eliminar_tarea(titulo_tarea)
                self.guardar_datos()
                print("Tarea eliminada con exito")
                
            elif opcion == "6":
                # Cerrando sesion
                print("Cerrando sesion....")
                break
            else:
                print("Opcion no valida. Intente nuevamente")
                
# Ejecucion del sistema
if __name__ == "__main__":
    sistema = SistemaGestionTareas()
    while True:
        print("\n------ Sistema de gestion de tareas --------")
        print("1. Registrar usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            nombre_usuario = input("Ingrese nombre de usuario: ")
            contrasena = input("Ingrese la contrasena: ")
            sistema.registrar_usuario(nombre_usuario, contrasena)
        
        elif opcion == "2":
            nombre_usuario = input("Nombre de usuario: ")
            contrasena = input("Contrasena: ")
            usuario = sistema.iniciar_sesion(nombre_usuario, contrasena)
            if usuario:
                sistema.menu_usuarios(usuario)
                
        elif opcion == "3":
            print("Saliendo del sistema.....")
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.") 
        
