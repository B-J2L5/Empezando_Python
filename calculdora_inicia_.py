a= int(input("ingrese numero: "))
b= int(input("ingrese numero: "))

operacion = input("ingrese el signo que desea utilizar (+,-,*,/): " )

if operacion == "+":
    resultado=a+b
elif operacion == "-":
    resultado = a-b
elif operacion == "*":
    resultado = a*b
elif operacion == "/":
    resultado = a/b
else:
    print("operacion no valido")
    
print("El resultado de la operacion es: ", resultado)
    
        
        
        