x1 = 10
x2 = 10
x3 = 10
x4 = 10
x5 = 10
avião = [
    {"AS7012": x1},
    {"QX2002": x2},
    {"AS2002": x3},
    {"8E880": x4},
    {"8E890": x5}
]


while True:
    print("Voos disponíveis: AS7012, QX2002, AS2002, 8E880, 8E890")
    voo = input("Qual voo a ser consultado: ")

    if voo == "AS7012":
        print(f"Este voo possui {x1} passagens")
        quant = int(input("Quantidade de passagens: "))
        x1 -= quant
        if x1 < 0:
            print("Passagens insuficientes")
            x1 += quant
        else:
            if x1 <= 5:
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

    elif voo == "QX2002":
        print(f"Este voo possui {x2} passagens")
        quant = int(input("Quantidade de passagens: "))
        x2 -= quant
        if x2 < 0:
            print("Passagens insuficientes")
            x2 += quant
        else:
            if x2 <= 5:
                valor = (quant * 100) + (quant * 100) *valo 0.20
                print(f"O valor a ser pago é de R${r}")
            else:
                valor = quant * 100
                print(f"O valor a ser pago é de R${valor}")
            cont = input("Quer continuar sua compra? ")
            if cont == "Sim":
                continue
            else:
                break

    elif voo == "AS2002":
        print(f"Este voo possui {x3} passagens")
        quant = int(input("Quantidade de passagens: "))
        x3 -= quant
        if x3 < 0:
            print("Passagens insuficientes")
            x3 += quant
        else:
            if x3 <= 5:
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

    elif voo == "8E880":
        print(f"Este voo possui {x4} passagens")
        quant = int(input("Quantidade de passagens: "))
        x4 -= quant
        if x4 < 0:
            print("Passagens insuficientes")
            x4 += quant
        else:
            if x4 <= 5:
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

    elif voo == "8E890":
        print(f"Este voo possui {x5} passagens")
        quant = int(input("Quantidade de passagens: "))
        x5 -= quant
        if x5 < 0:
            print("Passagens insuficientes")
            x5 += quant
        else:
            if x5 <= 5:
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

    else:
        print("Voo inválido")

