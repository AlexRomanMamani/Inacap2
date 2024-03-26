pat = "c:\\bdd\\datos.txt"


def contar(pat):
    fil = open(pat, "r")
    return len(fil.readlines())


# print(contar(pat)+1)


def buscar(r):
    pat = "c:\\bdd\\datos.txt"

    fil = open(pat, "r")
    reg = fil.readlines()
    for x in reg:
        # print("x",x)
        data = x.strip().split(",")  # formateo de valores(quita los espacios)
        print("data", data)
        # print("encontro", r)
        """""
        if r in data:
            return 1
        else:
            return 0
        """ ""
    fil.close()
