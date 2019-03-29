# Autor: Ronaldo Estefano Lira Buendia
# Programa que divide por medio de restas y de una lista encontrar el mayor numero.

def probarDivisiones(dividendo, divisor):
    div = 0
    residuo = dividendo
    while residuo >= divisor:
        residuo -= divisor
        div += 1
        x = (dividendo, "/", divisor, '=', div, "sobra", residuo)
    return x


def encontrarMayor():
    x = 0
    y = 0
    x = int(input("introduce tu valor[coloca -1 para salir]:"))
    y = x
    while x != (-1):
        if x < 0 and x != -1:
            b =("tus numeros deben de ser positivos")
        elif x > y:
            y = x
        x = int(input("introduce tu valor[coloca -1 para salir]:"))
    if y == -1:
        b = ("No hay numeros mayores")
    else:
        b = ("El mayor es" ,y, "")
    return b


def main():
    opc = 1
    while opc != 0:
        print("""Mision 07. Ciclos White 
        Autor: Ronaldo Estefano Lira Buendia.
        Matricula: A01748428.
        1.-Calcular divisores
        2.-Encontrar el mayor')
        3.-Salir""")
        opc = int(input("Teclea tu opcion: "))
        if opc > 0 and opc < 4:
            if opc == 1:
                dividendo = int(input("Introduce tu dividendo: "))
                divisor = int(input("Introduce tu divisor: "))
                x = probarDivisiones(dividendo, divisor)
                print (x)
            else:
                if opc == 2:
                    a = encontrarMayor()
                    print(a)
                else:
                    if opc==3:
                        print("Hasta luego")
                    else:
                        print("ERROR")

main ()