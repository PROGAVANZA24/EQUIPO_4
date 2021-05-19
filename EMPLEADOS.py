class empleados:
        def __init__(self, id_empleado, nom, dir):
        self.__id_empleado = id_empleado
        self.__nom = nom 
        self.__dir = dir

        def datosemp(self):
        f=open("c:\\desktop\\ArchivosDeTexto\\empleados.txt")
        f.write (str(self.__id_empleado))
        f.write (str(self.__nom))
        f.write (str(self.__dir))
        f.close(None)
