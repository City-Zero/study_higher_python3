f = open('a','r')
print(f.read(),end='')
while True:
    try:
        print(f.read(),end='')
    except KeyboardInterrupt:
        f.close()
        break