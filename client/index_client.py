import threading
import socket
import time

from ia.index_ia import openia_write


class Client():
    def __init__(self):

        self.__username = ''
        self.__receive = ''
        self.__send = ''

    def connectClient(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client.connect(('localhost', 7777))
        except:
            return print('\nNão foi possível se conectar ao servidor!\n')

        thread1 = threading.Thread(target=self.receiveMessages, args=[client])
        thread2 = threading.Thread(target=self.sendMessages, args=[client])

        thread1.start()
        thread2.start()

    def receiveMessages(self, client):
        while True:
            try:
                self.__receive = client.recv(2048).decode('utf-8')
                print(self.__receive)
            except:
                print('\nNão foi possível permanecer conectado no servidor!\n')
                print('Pressione <Enter> Para continuar...')
                client.close()

    def sendMessages(self, client):
        while True:
            try:
                if len(self.__send) > 0:
                    self.send(client, self.__send, self.__username)
                    if self.__send.startswith('#'):
                        response = openia_write(self.__send)
                        self.send(client, response, 'BOT-PROMETHEUS')
                    self.__send = ''
            except:
                return

    def send(self, client, prompt, username):
        client.send(f'<{username}> {prompt}'.encode('utf-8'))

    def getReceiveMessage(self):
        time.sleep(3)
        return self.__receive

    def setSendMessages(self, sendMessage):
        self.__send = sendMessage

    def setUsername(self, username):
        self.__username = username