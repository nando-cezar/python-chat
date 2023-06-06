import threading
import socket
import time

import requests
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
                receivedContent = client.recv(2048).decode('utf-8')
                self.setReceiveMessage(receivedContent)

                if self.getReceiveMessage().startswith('BOT-PROMETHEUS: @'):
                    url_img = self.getReceiveMessage().removeprefix('BOT-PROMETHEUS: @').strip()
                    response = requests.get(url_img, stream=True)

                    with open(f"../assets/{self.getTaskId()}.png", "wb+") as handler:
                        for data in response.iter_content(self.__buffer_size):
                            handler.write(data)

                    img = Image.open(f"../assets/{self.getTaskId()}.png")
                    img.show()
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
                    if self.__send.startswith('#'):
                        response = chatGPT_write(self.__send)
                        self.send(client, 'BOT-PROMETHEUS', "# " + str(response).strip())
                    elif self.__send.startswith('@'):
                        image_token, url_image = midJourney_call(self.__send)
                        self.setTaskId(image_token)
                        self.send(client, 'BOT-PROMETHEUS', "@ " + str(url_image).strip())
                    self.setSendMessages('')
            except Exception as error:
                return print(error)

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

    def setTaskId(self, taskId):
        self.__taskId = taskId

    def getTaskId(self):
        return self.__taskId
