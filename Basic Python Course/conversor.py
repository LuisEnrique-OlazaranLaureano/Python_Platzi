def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("Cuantos pesos "+tipo_pesos+" tienes?: "))
    valor_dolar = valor_dolar
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+dolares+" dolares")  


menu = """
Bienvenido al conversor de monedas 💰

1.- Pesos colombianos
2.- Pesos argentinos
3.- Pesos mexicanos

Elige una opción: 
"""

opcion = input(menu)
if opcion == "1":
    conversor("colombianos",3875)
elif opcion == "2":
    conversor("argentinos",65)
elif opcion == "3":
    conversor("argentinos",24)
else:
    print("Ingresa una opción correcta")

