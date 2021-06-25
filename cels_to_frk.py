# convert celsius

celsius = float(input("Temperatur celsius: "))

fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius = %0.2f Fahrenheit' %(celsius,fahrenheit))
reanmur = (celsius * 4/5)
print('%.2f Celsius = %0.2f Reanmur' %(celsius,reanmur))
kelvin = (celsius + 273)
print('%.2f Celsius = %0.2f Kelvin' %(celsius,kelvin))