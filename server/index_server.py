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
            contains_ia = str(msg).__contains__('PROMETHEUS')
            broadcast(msg, client, contains_ia)
        except:
            deleteClient(client)
            break


def broadcast(msg, client, contains_ia):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)
        elif clientItem == client and contains_ia:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)

def deleteClient(client):
    clients.remove(client)


main()
