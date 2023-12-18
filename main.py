import random
from .messages import display_messages

message = displa_messages
print(message)

while True:
    resposta = input('Deseja receber um conselho? S|N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()

