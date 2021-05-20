class TEMA: 
    def __init__(self, id_tema, nom):
        self.__id_tema=id_tema
        self.__nom=nom 
    def guardar(self):
        f=open("temas.txt", "w")
        f.write(f'{str(self.__id_tema)} | {str(self.__nom)}')
        f.close() 
    def ConsultarTodo():
        f=open("temas.txt", "r")
        print(f.read())
        f.close()
    def ConsultaID():
        preg=input("Escribe el id que quieres buscar: ")
        bloc=open("temas.txt", "r")  
        for formato in bloc:
            datos=formato.strip().split(" | ")
            if datos[0]==preg:
                print(f'ID Tema: {datos[0]} | Nombre: {datos[1]}')
        bloc.close() 