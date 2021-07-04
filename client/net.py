import socket
import pickle
import threading

from client import SERVER


def send(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(SERVER)
    sock.send(data)
        
    return sock.recv(1024)