def func(*args, **kwargs):
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    return args, nome, sobrenome

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
print(func(*lista, *lista2, nome='Luiz',sobrenome='Miranda'))