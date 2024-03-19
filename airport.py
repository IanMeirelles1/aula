x1 = 10
x2 = 10
x3 = 10
x4 = 10
x5 = 10


def main():
    while True:
        print("Voos disponíveis: AS7012, QX2002, AS2002, 8E880, 8E890")
        voo = input("Qual voo a ser consultado: ")
        if voo == "AS7012":
            sis(x1)
        elif voo == "QX2002":
            sis(x2)
        elif voo == "AS2002":
            sis(x3)
        elif voo == "8E880":
            sis(x4)
        elif voo == "8E890":
            sis(x5)
        else:
            print("Voo inválido")


def sis(x):
    print(f"Este voo possui {x} passagens")
    quant = int(input("Quantidade de passagens: "))
    x -= quant
    if x < 0:
        print("Passagens insuficientes")
        x += quant
    else:
        if x <= 5:
            valor = (quant * 100) + (quant * 100) * 0.20
            print(f"O valor a ser pago é de R${valor}")
        else:
            valor = quant * 100
            print(f"O valor a ser pago é de R${valor}")
        cont = input("Quer continuar sua compra? ")
        if cont == "Sim":
            continue
        else:
            break


main()
