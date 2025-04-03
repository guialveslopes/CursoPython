#Funções - def em Python 
def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e','3')
    print(msg, nome)

saudacao(nome='Zezo', msg='Hi')
saudacao('Oi','Luiz')
saudacao('Ola', 'Otavio')
saudacao('Hi','Maria')

def divide(n1, n2):
    return n1/n2

print(divide(4,2))
