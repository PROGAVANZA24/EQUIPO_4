class empleados:
        def __init__(self, id_empleado, nom, dir):
            self.__id_empleado = id_empleado
            self.__nom = nom 
            self.__dir = dir
        def guardar(self):
            f=open("c:\\Users\\victo\\Desktop\\ArchivosDeTexto\\empleados.txt")
            f.write (str(self.__id_empleado))
            f.write (str(self.__nom))
            f.write (str(self.__dir))
            f.close(None)
        def ConsultarTodo(cls):
            bloc=open("c:\\Users\\victo\\Desktop\\ArchivosDeTexto\\empleados.txt")
            print(bloc.read())
            bloc.close()
        
