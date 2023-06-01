import threading
import socket

from ia.index_ia import openia_write


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input('Usuário> ')
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break


def sendMessages(client, username):
    while True:
        try:
            msg = input('\n')
            send(client, msg, username)
            if msg.startswith('#'):
                response = openia_write(msg)
                send(client, response, 'BOT-PROMETHEUS')
        except:
            return


def send(client, prompt, username):
    client.send(f'<{username}> {prompt}'.encode('utf-8'))


main()
