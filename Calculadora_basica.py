"""\n EJERCICIO PRACTICO: Calculadora.
Desarrollar una calculadora de una sola variable con estas caracteristicas:
1. Debe ser capaz de resolver todas las operaciones basicas.
2. El usuario puede elegir cual desee.
3. La calculadora debera solicitar unicamente dos valores por cada operación.
Requerimientos:
El codigo solo puede funcionar con numero """

print("Calculadora con una sola variable. \n")

print("* Menu de opciones*")
print("===================")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto")

numero = int(input("Introduce la opcion deseada:"))

if numero == 1:
    print("Elegiste suma \n")
    numero = int(input("Introduce el primer numero:"))
    numero += int(input("Introduce el segundo numero:"))
    print("El resultado de la suma es:", numero)

    
elif numero == 2:
    print("Elegiste resta \n")
    numero = int(input("Introduce el primer numero:"))
    numero -= int(input("Introduce el segundo numero:"))
    print("El resultado de la resta es:", numero)

elif numero == 3:
    print("Elegiste multiplicación \n")
    numero = int(input("Introduce el primer numero:"))
    numero *= int(input("Introduce el segundo numero:"))
    print("El resultado de la multiplicació es:", numero)

elif numero == 4:
    print("Elegiste división \n")
    numero = float(input("Introduce el primer numero:"))
    numero /= float(input("Introduce el segundo numero:"))
    print("El resultado de la división es:", numero)


elif numero == 5:
    print("Elegiste división entera \n")
    numero = int(input("Introduce el primer numero:"))
    numero //= int(input("Introduce el segundo numero:"))
    print("El resultado de la división entera es:", numero)


elif numero == 6:
    print("Elegiste exponente \n")
    numero = int(input("Introduce el primer numero:"))
    numero **= int(input("Introduce el segundo numero:"))
    print("El resultado del exponente es:", numero)



elif numero == 7:
    print("Elegiste módulo o resto \n")
    numero = int(input("Introduce el primer numero:"))
    numero %= int(input("Introduce el segundo numero:"))
    print("El resultado deL  módulo o resto es:", numero)


else:
    print("La opción elegida no existe, vuelve a intentar")
