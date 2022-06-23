# ENTRADAS

import math

radio_del_circulo = float(input("¿Cual es el radio del circulo en cm?= "))
PI = math.pi

# PROCESOS

pi_por_radio = PI * radio_del_circulo
radio_al_cuadrado = radio_del_circulo **2

perimetro = pi_por_radio *2
area = radio_al_cuadrado * PI


# SALIDAS

print("Perimetro= ", round(perimetro,2),"cm")
print("Area= ", round(area,3),"cm2")
