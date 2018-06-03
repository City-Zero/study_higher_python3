# coidng=utf-8
import random
import socket
import json

PasswordLength = 256

class conf():
    def __init__(self,passwd=None,lp=None,si=None,sp=None):
        self.passwd = passwd
        self.local_port = lp
        self.server_ip = si
        self.server_port = sp

    def to_json(self):
        return json.dumps({x:y for x,y in self.__dict__.items() if not hasattr(y,'__call__') or not 'a'.startswith('_')})

    def set_server_ip(self,ip):
        self.server_ip = ip

    @staticmethod
    def get_public_ip():
        err = 0
        while True:
            try:
                sock = socket.socket()
                sock.connect(('ip.chinaz.com', 80))
                sock.send(b'GET /getip.aspx HTTP/1.1\r\nHost: ip.chinaz.com\r\n\r\n')
                res = sock.recv(1024)
                body = res.decode('utf-8').split('\r\n\r\n')[1]
                sock.close()
                break
            except Exception:
                err = err + 1
            finally:
                sock.close()
        return body.split(',')[0][5:-1]

    def save(self,files = '.mysocks.json'):
        f = open(files,'w')
        f.write(self.to_json())
        f.close()

class PW():
    def __init__(self):
        self.passwd = []
        self.repassword = []

    def get_new_passwd(self):
        self.passwd.clear()
        chi = list(range(0,256))
        for i in range(256):
            x = i
            while(x == i):
                x = random.choice(chi)
            chi.remove(x)
            self.passwd.append(x)
    def byte_to_assic(self):
        bytepass = b''
        for i in self.passwd:
            bytepass += bytes((i,))
            print(bytes((i,)))
        print(str(bytepass))

    def set_passwd(self,passwd):
        self.passwd = passwd

    def set_repasswd(self):
        self.repassword = list(range(256))
        if len(self.passwd) != PasswordLength:
            raise('You mast set password first!')
        else:
            for index,data in enumerate(self.passwd):
                self.repassword[data] = index

if __name__ == '__main__':
    pw = PW()
    pw.get_new_passwd()
    c = conf(si=conf.get_public_ip(),passwd=pw.passwd)
    c.save('my.json')
    pw.byte_to_assic()