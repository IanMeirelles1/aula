voos = {
    "AS7012": [2, 3, 5],
    "QX2002": [2, 3, 5],
    "AS2002": [2, 3, 5],
    "8E880": [2, 3, 5],
    "8E890": [2, 3, 5]
}
def main():
    for x, y in voos.items():
        print(x[2])
        while True:
            print("Voos disponíveis: AS7012, QX2002, AS2002, 8E880, 8E890")
            voo = input("Qual voo a ser consultado: ")
            if voo == "AS7012":


def sis(a, b, c):
    print(f"Este voo possui {a} passagens)
    quant = int(input("Quantidade de passagens: "))
    a -= quant
