#importar una libreria o Biblioteca de funciones  Matematicas

import  math

# ENTRADAS DE DATOS
# Declarar o crear Variables
from audioop import mul


número_1 = float(input("Escribe el 1er numero: "))
número_2 = float(input("Escribe el 2do numero: "))



#PROCESOS (Cálculos u operaciones matematicas o logicas)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicacion = número_1 * número_2
divicion = número_1 / número_2

# potencia =

potencia1 = número_1 ** número_2
potencia2 = pow(número_1, número_2)

cuadrado = número_1 ** 2

raiz_cuadrada1 = math.sqrt(9)
raiz_cuadrada2 = pow(9, 1/2)

raíz_cubica = pow(27, 1/3)

modulo_residuo = número_1 % número_2


# SALIDA DE DATOS
print("La suma es igual a", round(suma, 2))
print("La suma es igual a " + str(suma)) #CONCATENACIÓN (Union de textos)
#CASTEO (Conversion de un tipo de dato en otro tipo de dato)
print(f"La suma es igual a {suma}")

#EJERCICIO

print("La Multiplicacion es igual a", multiplicacion)
print(f"La Divicion es igual a {divicion}")

print("La Potencia es igual a", potencia1)
print("La Potencia es igual a", potencia2)

print("El cuadrado de", número_1, "es igual a", cuadrado) 
print("la raiz cuadrada es igual a", round(raiz_cuadrada1), 3)
print("la raiz cuadrada es igual a", raiz_cuadrada2)

print("La raiz cubica es igual a", raíz_cubica)

print(f"El modulo o residuo o residuo de numero1 y numero2 es igual a {modulo_residuo}")