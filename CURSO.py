class curso:

    def __init__(self, id_curso, desc, id_emp):
        self.__id_curso=id_curso
        self.__desc=desc 
        self.__id_emp=id_emp
    def guardar(self):
        f=open("cursos.txt")
        f.write(f'{str(self.__id_curso)} | {str(self.__desc)} | {str(self.__id_emp)}')
        f.close()
    def ConsultarTodo(cls):
        bloc=open("cursos.txt")
        print(bloc.read())
        bloc.close()
    def ConsultaID(cls):
            preg=input("Escribe el id que quieres buscar: ")
            bloc=open("cursos.txt")
            for formato in bloc:
                datos=formato.strip().split("|")
                if datos[0]==preg:
                    print(datos)
            bloc.close()