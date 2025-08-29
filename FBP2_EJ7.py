alumnos_prog_III = []
alumnos_prog_IV = []
alumnos_prog_III_y_IV = []

cantidad_alumnos = int(input("\nIngrese la cantidad de alumnos de Programacion III: "))

for i in range(cantidad_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    alumnos_prog_III.append(nombre)

cantidad_alumnos = int(input("\nIngrese la cantidad de alumnos de Programacion IV: "))

for i in range(cantidad_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    alumnos_prog_IV.append(nombre)

for alumno in alumnos_prog_III:
    if alumno in alumnos_prog_IV:
        alumnos_prog_III_y_IV.append(alumno)


print("\nAlumnos en Programacion III Y IV simultaneamente: ", alumnos_prog_III_y_IV)

