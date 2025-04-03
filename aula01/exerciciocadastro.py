def cadastro_usuario(*args, **kwargs):
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    idade = kwargs.get('idade')
    return nome, sobrenome, idade, args

def coleta_dados():
    nome = str(input('Qual o seu nome: '))
    sobrenome = str(input('Qual o seu sobrenome: '))
    idade = str(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo M/F: '))
    if  not nome:
        print('Dados invalidos! Cadastro não concluido!')
    elif not sobrenome:
        print('Dados invalidos! Cadastro não concluido!')
    elif not idade:
        print('Dados invalidos! Cadastro não concluido!')
    else:
        print('Dados do usuario: ',cadastro_usuario(sexo,nome= nome, sobrenome= sobrenome, idade= idade))

coleta_dados()
