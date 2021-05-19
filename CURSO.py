class curso:

    def __init__(self, id_curso, desc, id_emp):
        self.__id_curso=id_curso
        self.__desc=desc 
        self.__id_emp=id_emp
    def datoscurso(self):
        f=open("c:\\Users\\victo\\Desktop\\ArchivosDeTexto\\curso.txt")
        f.write (str(self.__id_curso))
        f.write (str(self.__desc))
        f.write (str(self.__id_emp))
        f.close(None)