#ENTRADAS

calif_1 = float(input("calificacion 1= "))
calif_2 = float(input("calificacion 2= "))
calif_3 = float(input("calificacion 3= "))

#PROCESOS

suma_calif = calif_1 + calif_2 + calif_3
promedio_total = suma_calif / 3

#SALIDAS

print("El promedio de las calificaciones es de ", round(promedio_total, 2))