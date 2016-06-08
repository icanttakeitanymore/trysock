#!/usr/bin/env python3
# Программа простой проверки соединения.
import socket
import re

class MainSock():
    def __init__(self,address,port):
        '''Пишем адресс и порт в атрибуты экземпляра'''
        self.address = address
        self.port = port


    def __call__(self):
        '''Вызов экземпляра делает его сокетом атрибут connector'''
        self.connector = socket.socket()


    def __str__(self):
        '''Вся программа тут:)
        Через вызов self.__str__ выполняется вся работа программы.
        '''
        try:
            self()
            self.connector.connect((self.address,self.port))
        except socket.error as err:
            return 'Connection to {0}:{1} failed!'.format(self.address,self.port)
        else:
            return 'Connection to {0}:{1} succesfully !'.format(self.address,self.port) 

if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-a", "--address",
                     dest = "address",
                     type = "str",
                     help = 'IP адрес сервера или имя',
                     metavar = "ADDRESS")
    parser.add_option("-p","--port",
                      dest = "port",
                      type = "int",
                      help = "TCP порт сервера",
                      metavar = "PORT")


    try:
        options,args = parser.parse_args()
        if options == {'address': None, 'port': None}:
            raise TypeError
        else:
            check_server = MainSock(options.address,options.port)
            print(check_server)
    except TypeError:
        parser.print_help()
