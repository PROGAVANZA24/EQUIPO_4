class video:
    def __init__(self, id_video, nom,url,publi):
        self.__id_video=id_video
        self.__nom=nom
        self.__url=url
        self.__publi=publi
    def guardar(self):
        f=open("videos.txt", "a")
        f.write(f'{str(self.__id_video)} | {str(self.__nom)} | {str(self.__url)} | {str(self.__publi)}\n')
        f.close()
    def ConsularTodo():
        f=open("videos.txt", "r")
        print(f.read())
        f.close()
    def ConsultaID():
        preg=input("Escribe el id que quieres buscar: ")
        bloc=open("videos.txt", "r")
        for formato in bloc:
            datos=formato.strip().split(" | ")
            if datos[0]==preg:
                print(f'ID Video: {datos[0]} | Nombre: {datos[1]} | URL: {datos[2]} | Fecha publicación: {datos[3]}')
        bloc.close()