class video:
    def _init_(self, id_video, nom,url,publi):
        self.__id_video=id_video
        self.__nom=nom
        self.__url=url
        self.__publi=publi
    def guardar(self):
        f=open("video.txt")
        f.write (str(self.__id_video))
        f.write (str(self.__nom))
        f.write(str(self.__url))
        f.write(str(self.__publi))
        f.close(None)
    def ConsularTodo(cls):
        f=open("video.txt")
        print(f.read())
        f.close()