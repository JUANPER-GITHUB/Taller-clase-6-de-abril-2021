print("Ingrese 3 numeros")
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 7:
    print("Promocionado")
elif 4 <= promedio < 7:
    print("Regular")
elif promedio < 4:
    print("No habilitado")
