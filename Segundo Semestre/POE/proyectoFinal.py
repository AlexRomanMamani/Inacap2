import random

sumaPromedios = 0
asignatura = input("Nombre asignatura: ")
cantAlumnos = int(input("Cantidad alumnos: "))
cantNotas = int(input("Cantidad de notas: "))

for i in range(cantAlumnos):
    sumaNota = 0
    print("Alumno {}".format(i + 1))
    nombre = input("Nombre: ")
    for j in range(cantNotas):
        nota = round(random.uniform(1, 7), 1)
        sumaNota += nota
        print("Nota:  {}".format(nota))

    promedio = round(sumaNota / cantNotas, 1)
    sumaPromedios += promedio

    if promedio < 4.0:
        print("El alumno {} ha REPROBADO la asignatura {} con promedio {}.".format(
            nombre, asignatura, promedio))
    else:
        print("El alumno {} ha APROBADO la asignatura {} con promedio {}.".format(
            nombre, asignatura, promedio))

sumaPromedios = round(sumaPromedios / cantAlumnos, 1)
print("El promedio final del curso es {}, de un total de {} alumnos.".format(
    sumaPromedios, cantAlumnos))
