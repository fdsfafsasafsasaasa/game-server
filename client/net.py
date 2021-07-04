import socket
import pickle
import threading

from client import SERVER


def send(data):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect(SERVER)
        sock.send(data)
        
        return sock.recvfrom(1024)