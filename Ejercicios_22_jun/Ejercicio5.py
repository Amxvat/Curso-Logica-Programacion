# ENTRADAS
import math


valor_a = float(input("valor de a="))

valor_b = float(input("valor de b="))

valor_c = float(input("valor de c="))

# PROCESO

# x_1 =  ((- valor_b)-(pow(((((valor_a*valor_c)*4)-(valor_b**2))),1/2)))/(valor_a*2)

# x_2 =  ((- valor_b)+(pow((((valor_a*valor_c)*4)-(valor_b**2)),1/2)))/(valor_a*2)
x_1 = (- valor_b - pow((valor_b**2)-(4*valor_a*valor_c),1/2))/(valor_a*2)

x_2 = (- valor_b + pow((valor_b**2)-(4*valor_a*valor_c),1/2))/(valor_a*2)


# SALIDAS

print("x1 = ", round(x_1,2))

print("x2 = ", round(x_2,2))