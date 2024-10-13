# Ejercicio 12
# Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el 
# programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca 
# y el coste final total.

n_vend = int(input("ingrese el numero de barras de pan vendidas que no son del dia: "))

print("el precio habitual de pan es de :", 3.49)
print("el precio con descuento (por no ser del dia) es de:", 60, "%" )
print("el costo final es de ", round(n_vend * 3.49 * (1 - 0.6),2))

