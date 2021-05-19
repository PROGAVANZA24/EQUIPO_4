class tema: 
    def _init_(self, id_tema, nom):
        self.__id_tema=id_tema
        self.__nom=nom 
    def guardar(self):
        f=open("tema.txt")
        f.write (str(self.__id_tema))
        f.write (str(self.__nom))
        f.close(None)
    def ConsultarTodo(cls):
        f=open("tema.txt")
        print(f.read())
        f.close() 
    def ConsultaID(cls):
        preg=input("Escribe el id que quieres buscar: ")
        bloc=open("tema.txt") 