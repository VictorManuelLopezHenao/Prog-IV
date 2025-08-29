suma = 0
contador = 0

print ("Si desea terminar presione 0")
estatura = float(input("Ingrese una estatura: "))

if estatura == 0:
    print("Error. Debe ingresar minimo una estatura")
else:
    while estatura != 0:
        suma += estatura
        contador += 1

        estatura = float(input("Ingrese una estatura: "))

    promedio = suma/contador
    print("El promedio de estaturas es: ", promedio)



    

