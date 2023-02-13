import sys

def descomponer(numero):
    numero_str = str(numero)
    longitud = len(numero_str)
    
    for i in range(longitud):
        unidad = int(numero_str[i])
        potencia = 10 ** (longitud - i - 1)
        print("{:0>4}".format(unidad * potencia))

if len(sys.argv) == 2:
    try:
        numero = int(sys.argv[1])
        if numero >= 0:
            descomponer(numero)
        else:
            print("El número debe ser positivo.")
    except ValueError:
        print("El argumento debe ser un número entero.")
else:
    print("Uso: python descomposicion.py NUMERO")
    print("Descompone el número en unidades, decenas, centenas, miles...")
