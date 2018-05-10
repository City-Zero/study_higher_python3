import asyncio

urls_todo = {'/'+str(i) for i in range(100)}

async def wget(host,url):
    #print('wget %s...' % (host+url))
    connect = asyncio.open_connection(host,80)
    reader,writer = await connect
    header = 'GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' % (url,host)
    writer.write(header.encode('utf-8'))
    await writer.drain()
    response = b''
    while True:
        line = await reader.readline()
        if line:
            response += line
        else:
            break
    # print(response.decode('utf-8'))
    writer.close()
import time
start = time.time()
loop = asyncio.get_event_loop()
tasks = [wget('www.baidu.com',url) for url in urls_todo]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
print(time.time()-start)