# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de 
# años, y muestre por pantalla el capital obtenido en la inversión.

inv = float(input("cantidad a invertir : "))
int_anual = float(input("el interes anual : "))
anios = float(input("numero de anios :"))

print("el capital obtenido es de ", round(inv * (int_anual / 100 + 1) ** anios, 2))