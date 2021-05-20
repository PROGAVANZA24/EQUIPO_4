from CTV import CursoTemaVideo
from CURSO_TEMA import CursoTema
from CURSO import curso
from EMPLEADOS import empleados
from VIDEOS import video
from tema import tema

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
        else:
            print("*"*60)
            print("Opción invalida.")
        
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
    accion = op_administrar()
    if opcion == 1: #Empleados
        if accion == 1: #Guardar datos
            id = input("Ingresa la id del empleado: ")
            nombre = input("Ingresa el nombre del empleado: ")
            dir = input("Ingresa la dirección del empleado: ")
            data = empleados(id, nombre, dir)
            data.guardar()
        if accion == 2: #Consultar todo
            print("ID | Nombre | Dirección")
            empleados.ConsultarTodo()
        if accion == 3: #Consultar por ID
            empleados.ConsultaID()
    elif opcion == 1: #Cursos
        if accion == 1: #Guardar datos
            id = input("Ingresa la id del empleado: ")
            nombre = input("Ingresa el nombre del empleado: ")
            dir = input("Ingresa la dirección del empleado: ")
            data = curso(id, nombre, dir)
            data.guardar()
        if accion == 2: #Consultar todo
            print("ID | Nombre | Dirección")
            curso.ConsultarTodo()
        if accion == 3: #Consultar por ID
            curso.ConsultaID()