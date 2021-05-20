class empleados:
        def __init__(self, id_empleado, nom, dir):
            self.__id_empleado = id_empleado
            self.__nom = nom 
            self.__dir = dir
        def guardar(self):
            f=open("empleados.txt")
            f.write (str(self.__id_empleado))
            f.write (str(self.__nom))
            f.write (str(self.__dir))
            f.close(None)
        def ConsultarTodo(cls):
            bloc=open("empleados.txt")
            print(bloc.read())
            bloc.close()
        def ConsultaID(cls):
            preg=input("Escribe el id que quieres buscar: ")
            bloc=open("empleados.txt")
            for formato in bloc:
                datos=formato.strip().split("|")
                if datos[0]==preg:
                    print(datos)
            bloc.close()
        
