class CursoTemaVideo:
    def _init_(self, id_cursotem, id_cursotemvid,id_video):
        self.__id_cursotem = id_cursotem 
        self.__id_cursotemvid = id_cursotemvid
        self.__id_video = id_video
    def datoscursotemvid(self):
        f=open("cursotemavideo.txt")
        f.write (str(self.__id_cursotem))
        f.write (str(self.__id_cursotemvid))
        f.write(str(self.__id_video))
        f.close(None)
    