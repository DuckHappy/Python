# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa 
# corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> 
# donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("ingrese peso en kg : "))
est = float(input("ingrese su estatura en metros :" ))

#cabe agregar que para calcular el indicie es el peso dividido la estatura al cuadrado

masa_corp = peso/(est**2)

print("Tu índice de masa corporal es ", round(masa_corp,2))

