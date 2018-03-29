import socket
import select

s = socket.socket()
s.bind(('127.0.0.1',8888))
s.listen(5)
r_list = [s,]
num = 0
while True:
    print('\nselect')
    rl, wl, error = select.select(r_list,[],[])
    num+=1
    print('counts is %s'%num)
    print("rl's length is %s"%len(rl))
    for fd in rl:
        if fd == s:
            conn, addr = fd.accept()
            r_list.append(conn)
            msg = conn.recv(200)
            conn.sendall(('first----%s'%conn.fileno()).encode())
        else:
            try:
                msg = fd.recv(200)
                fd.sendall('second'.encode())
            except ConnectionAbortedError:
                r_list.remove(fd)
s.close()