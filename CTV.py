class CursoTemaVideo:
    def _init_(self, id_cursotem, id_cursotemvid,id_video):
        self.__id_cursotem = id_cursotem 
        self.__id_cursotemvid = id_cursotemvid
        self.__id_video = id_video
    def guardar(self):
        f=open("cursotemavideo.txt", "a")
        f.write(f'{str(self.__id_cursotem)} | {str(self.__id_cursotemvid)} | {str(self.__id_video)}\n')
        f.close()
    def ConsultarTodo():
        f=open("cursotemavideo.txt", "r")
        print(f.read())
        f.close()
    def ConsultarID():
        preg=input("Escribe el id que quieres buscar: ")
        bloc=open("cursotemavideo.txt", "r")
        for formato in bloc:
            datos=formato.strip().split(" | ")
            if datos[0]==preg:
                print(f'ID Tema del curso: {datos[0]} | ID Video asignado al tema: {datos[1]} | ID Video: {datos[2]}')
        bloc.close()