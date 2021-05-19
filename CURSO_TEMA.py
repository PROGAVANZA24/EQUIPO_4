class CursoTema:
    def __init__(self,id_cursotem,id_curso,id_tema):
        self.__id_cursotem=id_cursotem
        self.__id_curso=id_curso
        self.__id_tema=id_tema
    def guardar(self):
        f=open("cursotema.txt")
        f.write (str(self.__id_cursotem))
        f.write (str(self.__id_curso))
        f.write(str(self.__id_tema))
        f.close(None)