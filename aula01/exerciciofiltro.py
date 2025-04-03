pessoas = [
            ("Ana", 25),
            ("Bruno", 30),
            ("Carlos", 20),
            ("Daniela", 35),
            ("Eduardo", 28)
]

reverso = sorted(pessoas, key=lambda i: i[1])
print(reverso)
filtro = list(filter(lambda x: x[1] >= 25, reverso))
print(filtro)
