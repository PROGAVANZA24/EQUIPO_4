class tema: 
    def _init_(self, id_tema, nom):
        self.__id_tema=id_tema
        self.__nom=nom 
    def guardar(self):
        f=open("temas.txt", "w")
        f.write(f'{str(self.__id_tema)} | {str(self.__nom)}')
        f.close() 
    def ConsultarTodo(cls):
        f=open("temas.txt", "r")
        print(f.read())
        f.close()
    def ConsultaID(cls):
        preg=input("Escribe el id que quieres buscar: ")
        bloc=open("temas.txt", "r")  
        for formato in bloc:
            datos=formato.strip().split("|")
            if datos[0]==preg:
                print(datos)
        bloc.close() 