#Exercício: Calculadora Simples
def soma(n1,n2):
    return n1 + n2
def subtracao(n1,n2):
    return n1 - n2
def divisao(n1,n2):
    return n1/n2
def multiplicacao(n1,n2):
    return n1*n2

def escolha():
    esc = input('O que quer fazer? somar: S/subtrair: SB/dividir: D/multiplicar: M ')
    if esc == 'S':
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))
        print('O resultado foi: ', soma(n1,n2))
    elif esc == 'SB':
        n1 = float(input('Digite um nummero: '))
        n2 = float(input('Digite outro numero: '))
        print('O resultado foi: ', subtracao(n1,n2))
    elif esc == 'D':
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))
        print('O resultado foi: ', divisao(n1,n2))
    elif esc == 'M':
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))
        print('O resultado foi: ', multiplicacao(n1,n2))
    else: 
        print('Dados invalidos')

escolha()
