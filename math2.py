import os
import time
print("-----------")
print("CALCULADORA")
print("-----------")
print(" ")
time.sleep(0.5)
print ("To exit Type 'sair' ")
time.sleep(0.5)
print ("To clear the screen Type 'clear' ")
print(" ")
time.sleep(0.5)


while True:
    conta = input("Digite Sua Equação (2 + 3): ")

    if " " in conta:
        num1, operador, num2 = conta.split()

        num1 = int(num1)
        num2 = int(num2)

        if operador == "+":
            res = num1 + num2
            print("Resposta: ",res)
            print(" ")
        elif operador == "-":
            res = num1 - num2
            print("Resposta: ",res)
            if res < 0:
                print("Resultado Negativo")
            print(" ")
        elif operador == "x":
            res = num1 * num2
            print("Resposta: ",res)
            print(" ")
        elif operador == "/":
            res = num1 / num2
            print("Resposta: ",res)
            if res < 0:
                print("Resposta Negativa")
            print(" ")
    if conta == "sair":
        time.sleep(1)
        print("Até Mais...")
        time.sleep(1)
        break
    if conta == "clear":
        os.system("cls")
        print("-----------")
        print("CALCULADORA")
        print("-----------")
        print(" ")
        time.sleep(0.5)
        print ("To exit Type 'sair' ")
        time.sleep(0.5)
        print ("To clear the screen Type 'clear' ")
        print(" ")
        time.sleep(0.5)

    elif " " not in conta:
        print("Resposta Invalida")
        time.sleep(0.5)

