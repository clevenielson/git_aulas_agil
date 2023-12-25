from messages import display_messages
import random
import time

print('Iniciando o Projeto 3..2..1..')
time.sleep(3)

login_username = [
    'hugo',
    'joão',
    'benjamin'
]

username = input('usuario para login: ')

while True:
    username = input('Usuario para login:' )
    while(username not in login_username):
        print()
        print('Usuario Invalido! Tente novamente! ')

    resposta = input('Deseja receber um conselho? S|N: ')
    if (resposta == 'S' or resposta == 's'):
        print()
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
    elif (resposta == 'N' or resposta == 'n'):
        exit()

