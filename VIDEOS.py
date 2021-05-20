class video:
    def __init__(self, id_video, nom,url,publi):
        self.__id_video=id_video
        self.__nom=nom
        self.__url=url
        self.__publi=publi
    def guardar(self):
        f=open("videos.txt", "w")
        f.write(f'{str(self.__id_video)} | {str(self.__nom)} | {str(self.__url)} | {str(self.__publi)}')
        f.close()
    def ConsularTodo():
        f=open("videos.txt", "r")
        print(f.read())
        f.close()
    def ConsultaID():
        preg=input("Escribe el id que quieres buscar: ")
        bloc=open("videos.txt", "r")
        for formato in bloc:
            datos=formato.strip().split("|")
            if datos[0]==preg:
                print(datos)
        bloc.close()