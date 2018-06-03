# coding=utf-8
import socket
import six

# 可以封装成函数，方便 Python 的程序调用

class Socks():
    def __init__(self,coon):
        self.coon = coon
        self.CLI_VER = b'\x05'
        self.SER_VER = b'\x05'
        self.NMETHODS = b'\x00'
        self.METHODS = b'\xff'
        self.CMD = None
        self.RSV = None
        self.ATYP = None
        self.DST_ADDR = None
        self.DST_PORT = None
        self.REM_COON = None

    def set_coon(self):
        pass

    def rep_coon(self):
        res = self.coon.recv(2)
        self.CLI_VER = res[0]
        self.NMETHODS = res[1]
        if self.NMETHODS == b'\x00':
            self.coon.send(b'\x05\xff')
        else:
            res = self.coon.recv(int(str(res[1]),16))
            self.METHODS = res
            rep = b'\x05'+six.int2byte(self.METHODS[0])
            print(rep)
            self.coon.send(rep)
        print('成功接受连接')

    def send_req(self):
        pass

    def get_req(self):
        res = self.coon.recv(3)
        if res[1] == 1:
            self.REM_COON = socket.socket()
        res = self.coon.recv(1)
        if res == b'\x03':
            res = self.coon.recv(1)
            res = self.coon.recv(res[0])
            self.DST_ADDR = res.decode()
            print(self.DST_ADDR)
        res = self.coon.recv(2)
        self.DST_PORT = res[0]*256+res[1]
        print(self.DST_PORT)
        self.REM_COON.connect((self.DST_ADDR,self.DST_PORT))
        req = b'\x05\x00\x00\x03\x0a'+self.DST_ADDR.encode()+bytes(hex(self.DST_PORT),'utf-8')
        print(req)
        self.coon.send(req)
        res = b''
        while True:
            r = self.coon.recv(1025)
            res += r
            if len(r)<1025:
                break
        self.REM_COON.send(res)
        # print(res)
        while True:
            res = b''
            while True:
                r = self.REM_COON.recv(1025,)
                res += r
                if len(r) < 1025:
                    break
            print('flycold')
            if len(res) == 0:
                break
            print(res.decode('utf-8').split('\r\n\r\n'[0]))
            self.coon.send(res)
        self.REM_COON.close()
        self.coon.close()
if __name__ == '__main__':
    sock = socket.socket()
    sock.setsockopt(1,2,1)
    sock.bind(('127.0.0.1',1999))
    sock.listen(5)
    while True:
        coon, addr = sock.accept()
        ss = Socks(coon)
        ss.rep_coon()
        ss.get_req()

        coon.close()
        print('-----------')

