def op_administrar():
    acc = 0
    while acc < 1 or acc > 3:
        print("*"*26+"ACCIÓN A ADMINISTRAR"+"*"*26)
        print("1. Ingresar datos")
        print("2. Revisar todos los datos")
        print("3. Consultar por ID")
        print("4. Salir")
        acc = int(input("Ingrese una opción para administrar: "))
        if acc >= 1 or acc <= 3:
            return acc
        elif acc == 4:
            exit()
        
#Menú administrador
opcion = 0
while opcion < 1 or opcion > 6:    
    print("*"*26+"MENÚ ADMINISTRACIÓN"+"*"*26)
    print("1. Empleados")
    print("2. Cursos")
    print("3. Temas")
    print("4. Videos")
    print("5. Curso tema")
    print("6. Curso tema video")
    opcion = int(input("Ingrese opción por administrar: "))