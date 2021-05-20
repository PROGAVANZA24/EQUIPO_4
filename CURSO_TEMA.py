class CursoTema:
    def __init__(self,id_cursotem,id_curso,id_tema):
        self.__id_cursotem=id_cursotem
        self.__id_curso=id_curso
        self.__id_tema=id_tema
    def guardar(self):
        f=open("cursotema.txt", "w")
        f.write(f'{str(self.__id_cursotem)} | {str(self.__id_curso)} | {str(self.__id_tema)}')
        f.close()
    def ConsultarTodo(cls):
        f=open("cursotema.txt", "r")
        print(f.read())
        f.close()
    def ConsultarID(cls):
        preg=input("Escribe el id que quieres buscar: ")
        bloc=open("cursotema.txt", "r")
        for formato in bloc:
            datos=formato.strip().split("|")
            if datos[0]==preg:
                print(datos)
        bloc.close()