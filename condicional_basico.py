# Ejemplo básico de condicional con entrada por teclado

numero = int(input("Escribe un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
