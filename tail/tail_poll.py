import select

f = open('a','r')
poller = select.poll()
fd_to_file = {}
poller.register(f,select.POLLIN)
while True:
    try:
        events = poller.poll()
        for fd,flag in events:
            if flag and fd == f.fileno():
                print(f.read(),end='')
    except KeyboardInterrupt:
        f.close()
        break