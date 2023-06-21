import threading
import socket
import time

import urllib.request as request
from PIL import Image

from ia.chatGPT.index_chatGPT import chatGPT_write
from ia.midJourney.index_midJourney import midJourney_call


class Client():
    def __init__(self):

        self.__username = ''
        self.__receive = ''
        self.__send = ''
        self.__taskId = ''
        self.__buffer_size = 2048

    def connectClient(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client.connect(('localhost', 7777))
        except:
            return print('\nNão foi possível se conectar ao servidor!\n')

        thread1 = threading.Thread(target=self.receiveMessages, args=[client])
        thread2 = threading.Thread(target=self.sendMessages, args=[client, self.__username])

        thread1.start()
        thread2.start()

    def receiveMessages(self, client):
        while True:
            try:
                time.sleep(1)
                print('[Listener receive message in client scope] - Under monitoring...\n')
                self.setReceiveMessage(client.recv(2048).decode('utf-8'))
                self.renderImage()
            except:
                print('\nNão foi possível permanecer conectado no servidor!\n')
                print('Pressione <Enter> Para continuar...')
                client.close()

    def sendMessages(self, client, username):
        while True:
            try:
                time.sleep(1)
                print('[Listener send message in client scope] - Under monitoring...\n')
                if len(self.__send) > 0:
                    self.send(client, username, self.__send)
                    self.AIChoice(client)
                    self.setSendMessages('')
            except Exception as error:
                return print(error)

    def AIChoice(self, client):
        if self.__send.startswith('#'):
            response = chatGPT_write(self.__send)
            self.send(client, 'BOT-PROMETHEUS', "# " + str(response).strip())
        elif self.__send.startswith('@'):
            image_token, url_image = midJourney_call(self.__send)
            self.__taskId = image_token
            self.send(client, 'BOT-PROMETHEUS', "@ " + str(url_image).strip())

    def renderImage(self):
        if self.__receive.startswith('BOT-PROMETHEUS: @'):
            url_img = self.__receive.removeprefix('BOT-PROMETHEUS: @').strip()

            opener = request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            request.install_opener(opener)
            try:
                request.urlretrieve(url_img, f"./assets/{self.__taskId}.png")
                print('Success!')
            except Exception as ex:
                print(ex)

            img = Image.open(f"./assets/{self.__taskId}.png")
            img.show()

    def send(self, client, username, prompt):
        client.send(f'{username}: {prompt}'.encode('utf-8'))

    def getReceiveMessage(self):
        return self.__receive

    def setReceiveMessage(self, receiveMessage):
        self.__receive = receiveMessage

    def setSendMessages(self, sendMessage):
        self.__send = sendMessage

    def setUsername(self, username):
        self.__username = username

    def getUsername(self):
        return self.__username
