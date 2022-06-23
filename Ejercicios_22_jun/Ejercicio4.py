# ENTRADAS

grados = float(input("Cantidad de Grados= "))

# PROCESOS

celsius_kelvin = grados + 273.15

celsius_fahrenheit = ((9 * grados) / 5) + 32


fahrenheit_celsius = ((grados - 32) * 5) / 9

fahrenheit_kelvin = (((grados - 32) * 5) / 9) + 273.15


kelvin_celsius = grados - 273.15

kelvin_fahrenheit = (((grados - 273.15) * 9) / 5) + 32

# SALIDAS

print ("celsius a kelvin= ", round(celsius_kelvin,2))
print ("celsius a fahrenheit= ", round(celsius_fahrenheit,2))
print ("fahrenheit a celsius= ", round(fahrenheit_celsius,2))
print ("fahrenheit a kelvin= ",round(fahrenheit_kelvin,2))
print ("kelvin a celsius= ", round(kelvin_celsius,2))
print ("kelvin a fahrenheit= ", round(kelvin_fahrenheit,2))

