class ClientSocketThread(threading.Thread):
    def __init__(self, addr, lock):
        threading.Thread.__init__(self)
        self.lock = lock
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.data = []

    def decode(data: bytes) -> dict:
        return pickle.loads(data)

    def run(self):
        while True:
            data, addr = self.sock.recv(1024)
            self.lock.acquire()

            decoded = self.decode(data)

            if not decoded:
                continue

            try:
                self.data.append(decoded)
            finally:
                self.lock.release()

    def stop(self):
        self.sock.close()