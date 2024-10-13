#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el 
#coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

n_trab = input("ingrese horas trabajadas : ")
n_trab = float(n_trab)

c_hrs = input("costo por hora : ")
c_hrs = float(c_hrs)

cobro = n_trab*c_hrs

cobro = str(cobro)

print("su paga que le corresponde es de " + cobro)

#otra opcion es :

n_trab = float(input("ingrese horas trabajadas : "))
c_hrs = float(input("costo por hora : "))
cobro = n_trab * c_hrs
print("su paga que le corresponde es de ", cobro)