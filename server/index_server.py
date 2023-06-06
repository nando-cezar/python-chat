import threading
import socket

clients = []


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print('Bem-vindo ao PROMETHEUS, central de ajuda mais integrado do mundo!')
        server.bind(('localhost', 7777))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()


def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            print(f'Message receive server: {msg}\n')
            broadcast(msg)
        except:
            deleteClient(client)
            break


def broadcast(msg):
    for clientItem in clients:
        try:
            clientItem.send(msg)
        except:
            deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)


main()
