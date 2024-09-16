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
    print("1. Método Newton Raphson")
    print("2. Método Newton Raphson Mejorado")
    print("7. Salir")

def Newton_Raphson():

    x = symbols("x")

    expression = leer_expresion()

    #Se obtiene la derivada de la expresión
    derivate = diff(expression, x)

    error_deseado = int(input("Ingresa el error deseado en porcentaje: "))
    error = 100
    raiz_n = float(input("Ingresa el valor inicial: "))
    raiz_x = 0.0 #Este es el valor de x_n+1
    iteraciones = 0
    max_iteraciones = 1000


    while (error > error_deseado) and (iteraciones <= max_iteraciones):
        #Se obtiene el valor 
        numerador = (expression.subs(x, raiz_n))
        denominador = derivate.subs(x, raiz_n)

        if denominador == 0:
            print("El denominador vale cero. No se puede continuar con el método")
            return

        raiz_x = raiz_n - (numerador / denominador) 
        error = abs((raiz_x - raiz_n)/raiz_x) * 100
        raiz_n = raiz_x

        if iteraciones == max_iteraciones:
            print("Se alcanzo el limite de iteraciones (1000) y no ha convergido la función")

    print(f"Una buena aproximacion a la solucion con un porcentaje de error {error_deseado} es {raiz_x} ")

def Newton_Raphson_Mejorado():
    x = symbols("x")

    expresion = leer_expresion()

    #Se obtienen las derivadas
    primera_derivada = diff(expresion, x)
    segunda_derivada = diff(expresion, x, 2)

    error = 100.0
    error_deseado = float(input("Ingresa el error deseado: "))
    raiz_n = float(input("Ingresa el valor inicial del x: "))
    raiz_x = 0
    iteraciones = 0
    max_iteraciones = 1000

    while (error > error_deseado) and (iteraciones <= max_iteraciones):
        numerador = expresion.subs(x, raiz_n)*primera_derivada.subs(x, raiz_n)
        denominador = (primera_derivada.subs(x, raiz_n))**2 - (expresion.subs(x, raiz_n)*(segunda_derivada.subs(x, raiz_n)))

        if denominador == 0:
            print("El denominador vale cero, no se puede continuar con el método")
            return

        raiz_x = raiz_n - (numerador/denominador)
        error = abs((raiz_x - raiz_n) / raiz_x) * 100
        raiz_n = raiz_x

        if iteraciones == max_iteraciones:
            print("Se ha alcanzo el limite de iteraciones")
    print("Una buena aproximacion con un error menor al ", error, "es", raiz_x)


continuar = True

while continuar:
    menu()
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        Newton_Raphson()
    elif opcion == 2:
        Newton_Raphson_Mejorado()
    if opcion == 7:
        continuar = False
