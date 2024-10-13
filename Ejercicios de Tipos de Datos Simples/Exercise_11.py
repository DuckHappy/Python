# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
# final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada 
# en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
# la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

dep = float(input("ingrese la cantidad depositada : "))

dep1 = dep*(1+(4/100))
print("en el primer anio el ahorro es de :" , round(dep1,2))

dep2 = dep1*(1+(4/100))
print("en el segundo anio el ahorro es de :" , round(dep2,2))

dep3 = dep2*(1+(4/100))
print("en el tercer anio el ahorro es de :" , round(dep3,2))