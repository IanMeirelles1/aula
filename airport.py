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

def sis(x, y):
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
