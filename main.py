#!/usr/bin/env python3
# Программа простой проверки соединения.
import socket
import re
import sys
import os
class MainSock():
    def __init__(self,address,port):
        '''Пишем адресс и порт в атрибуты экземпляра'''
        self.address = address
        self.port = port


    def __call__(self):
        '''Вызов экземпляра делает его сокетом'''
        self.connector = socket.socket()


    def __str__(self):
        '''Вся программа тут:)
        Через вызов self.__str__ выполняется вся работа программы.
        '''
        conntext = 'Try to connect {0} {1}'.format(self.address,self.port)
        try:
            print(conntext)
            self()
            self.connector.connect((self.address,self.port))
        except socket.error as err:
            return 'Connection failed!'
        else:
            return 'Connection succesfully!' 

if __name__ == '__main__':
    trysock = MainSock(os.sys.argv[1],int(os.sys.argv[2]))
    print(trysock)
