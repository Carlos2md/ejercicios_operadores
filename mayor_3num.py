name=str(input("¡Hola! cual es tu nombre: " ))
print(f"¡{name}! Vamos a verificar si alguno de los 2 valores a ingresar son >10")
num1=int(input("Ingresa el primer valor: "))
num2=int(input("Ingresa el segundo valor: "))
resultado1=(num1>10)
resultado2=(num2>10)
rfinal=resultado1 or resultado2
print("El resultado es:",rfinal)