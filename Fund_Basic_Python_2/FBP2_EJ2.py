suma = 0
contador = 0
ciclo = "S"

while ciclo != "N":
    estatura = float(input("Ingrese una estatura: "))
    suma += estatura
    contador += 1

    ciclo = input("Desea ingresar mas estaturas [S/N]: ")

promedio = suma/contador
print("El promedio de estaturas es: ",promedio)



