import select

f = open('a','r')
while True:
    try:
        rs, ws, es = select.select([f, ], [], [])
        for i in rs:
            buf = i.read()
            print(buf, end='')
    except KeyboardInterrupt:
        f.close()
        break