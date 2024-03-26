# CREA ARCHIVO.TXT CON TABLA DE MULTIPLICAR
n = int(input('Introduce un numero entero entre 1 y 10: '))
#fiche = 'c:\\bdd\\tabla-' + str(n) + '.txt'
fiche = 'bdd2\\tabla-' + str(n) + '.txt'

with open(fiche, "w") as f:
    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')

f.close()  # EL WITH DEBE SIEMPRE CERRARSE
