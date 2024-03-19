voos = {
    "AS7012": [2, 3, 5],
    "QX2002": [2, 3, 5],
    "AS2002": [2, 3, 5],
    "8E880": [2, 3, 5],
    "8E890": [2, 3, 5]
}
for x, y in voos.items():
    while True:
        print("Voos disponíveis: AS7012, QX2002, AS2002, 8E880, 8E890")
        voo = input("Qual voo a ser consultado: ")

