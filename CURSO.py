class curso:

    def __init__(self, id_curso, desc, id_emp):
        self.__id_curso=id_curso
        self.__desc=desc 
        self.__id_emp=id_emp
    def guardar(self):
        f=open("cursos.txt", "a")
        f.write(f'{str(self.__id_curso)} | {str(self.__desc)} | {str(self.__id_emp)}\n')
        f.close()
    def ConsultarTodo():
        bloc=open("cursos.txt", "r")
        print(bloc.read())
        bloc.close()
    def ConsultaID():
            preg=input("Escribe el id que quieres buscar: ")
            bloc=open("cursos.txt", "r")
            for formato in bloc:
                datos=formato.strip().split(" | ")
                if datos[0]==preg:
                    print(f'ID Curso: {datos[0]} | Descripción: {datos[1]} | ID Empleado: {datos[2]}')
            bloc.close()