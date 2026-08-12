print("Hoy aprenderemos If, Else, Elif")
print("------------------")
print("     Ejemplo      ")
print("------------------")

print("El puntaje para ir a la UNI es de 20")

puntaje = int(input("Ingrese su numero"))

if puntaje>=20:
    print("----------------------------------------------")
    print("      FELICIDADES INGRESASTE A LA UNI         ")
    print("----------------------------------------------")
    
elif puntaje==15:
    print("PASAS PERO CON EXAMEN DE PRUEBA")
    not2= int(input("Ingrese su nota del examen de prueba"))
    if not2>=13:
        print("Felicidades Ingresaste a la UNI")
    else: 
        print("No ingresaste intenta el proximo año")
else:
    print("No ingresas intenta el proximo año")