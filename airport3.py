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
                sis(voos["AS7012"][0], voos["AS7012"][1], voos["AS7012"][2], "AS7012")



def sis(a, b, c, d):
    print(f"Este voo possui {a} passagens de executiva, {b} passagens confort e {c} passagens econômicas")
    opt = input("Qual opção de passagem você deseja: ")
    if opt == "1":
        quantidade(voos[d][0])

    elif opt == "2":
        quantidade(voos[d][1])

    elif opt == "3":
        quantidade(voos[d][2])





def quantidade(z):
    quant = int(input("Quantidade de passagens: "))
    if quant > z:
        print("Quantidade de passagens indisponíveis")
    else:
        z -= quant
        



def valor():



