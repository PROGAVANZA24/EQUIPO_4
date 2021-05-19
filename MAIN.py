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