voos = {
    "AS7012": [2, 3, 5],
    "QX2002": [2, 3, 5],
    "AS2002": [2, 3, 5],
    "8E880": [2, 3, 5],
    "8E890": [2, 3, 5]
}


def main():
        while True:
            print("Voos disponíveis: AS7012, QX2002, AS2002, 8E880, 8E890")
            voo = input("Qual voo a ser consultado: ")
            if voo == "AS7012":
                valor1, valor2, valor3 = sis(voos["AS7012"][0], voos["AS7012"][1], voos["AS7012"][2], "AS7012")
            elif voo == "QX2002":
                valor1, valor2, valor3 = sis(voos["QX2002"][0], voos["QX2002"][1], voos["QX2002"][2], "QX2002")
            elif voo == "AS2002":
                valor1, valor2, valor3 = sis(voos["AS2002"][0], voos["AS2002"][1], voos["AS2002"][2], "AS2002")
            elif voo == "8E880":
                valor1, valor2, valor3 = sis(voos["8E880"][0], voos["8E880"][1], voos["8E880"][2], "8E880")
            elif voo == "8E890":
                valor1, valor2, valor3 = sis(voos["8E890"][0], voos["8E890"][1], voos["8E890"][2], "8E890")
            perg = input("Deseja continuar a compra: ")
            if perg == "Sim":
                continue
            elif perg == "Não":
                break
        valorf = valor1 + valor2 + valor3
        print(valorf)

def sis(a, b, c, d):
    print(f"Este voo possui {a} passagens de executiva, {b} passagens confort e {c} passagens econômicas")
    opt = input("Qual opção de passagem você deseja: ")
    if opt == "1":
        quant = quantidade(voos[d][0])
        valor1 = quant * 500

    elif opt == "2":
        quant = quantidade(voos[d][1])
        valor2 = quant * 350

    elif opt == "3":
        quant = quantidade(voos[d][2])
        valor3 = quant * 100
    return valor1, valor2, valor3



def quantidade(z):
    quant = int(input("Quantidade de passagens: "))
    if quant > z:
        print("Quantidade de passagens indisponíveis")
    else:
        z -= quant
    return quant







