from sympy import symbols, sympify, diff, Subs

#Se crea los simbolos que vamos a ocupar


def leer_expresion():
    x = symbols("x")
    #Se lee la función a analizar
    try:
        string_expression = input("Ingresa la expresion: ")
        expression = sympify(string_expression)
        print(expression)
    except Exception as e:
        print("Error al analizar la expresion: ", e)

    return expression

def menu():
    print("1. Metodo Newton Raphson")

def Newton_Raphson():

    x = symbols("x")

    expression = leer_expresion()

    #Se obtiene la derivada de la expresión
    derivate = diff(expression, x)

    error_deseado = int(input("Ingresa el error deseado en porcentaje: "))
    error = 100
    raiz_n = float(input("Ingresa el valor inicial: "))
    raiz_x = 0.0 #Este es el valor de x_n+1


    while (error > error_deseado):
        #Se obtiene el valor 
        raiz_x = raiz_n - ((expression.subs(x, raiz_n)) / derivate.subs(x, raiz_n)) 
        error = abs((raiz_x - raiz_n)/raiz_x) * 100
        raiz_n = raiz_x

    print(f"Una buena aproximacion a la solucion con un porcentaje de error {error_deseado} es {raiz_x} ")


continuar = True

while continuar:
    menu()
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        Newton_Raphson()
    if opcion == 7:
        continuar = False
