class empleados:
        def __init__(self, id_empleado, nom, dir):
            self.__id_empleado = id_empleado
            self.__nom = nom 
            self.__dir = dir
        def guardar(self):
            f=open("empleados.txt", "w")
            f.write(f'{str(self.__id_empleado)} | {str(self.__nom)} | {str(self.__dir)}')
            f.close()
        def ConsultarTodo():
            bloc=open("empleados.txt", "r")
            print(bloc.read())
            bloc.close()
        def ConsultaID(cls):
            preg=input("Escribe el id que quieres buscar: ")
            bloc=open("empleados.txt", "r")
            for formato in bloc:
                datos=formato.strip().split("|")
                if datos[0]==preg:
                    print(datos)
            bloc.close()
        
