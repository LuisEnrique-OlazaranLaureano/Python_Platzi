#Teorema de Wilson
def run():
    numero = int(input("Digita un numero: "))
    factorial = 1
    for i in range(1,numero):
        factorial *= i  
    factorial+=1
    if factorial % numero == 0:
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()

