import asyncio
import aiohttp

host = 'http://www.baidu.com'
urls_todo = {'/'+str(i) for i in range(100)}

loop = asyncio.get_event_loop()

async def fetch(url):
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(url) as response:
            response = await response.read()
            return response

if __name__ == '__main__':
    import time
    start = time.time()
    task = [fetch(host+url) for url in urls_todo]
    loop.run_until_complete(asyncio.gather(*task))
    loop.close()
    print(time.time()-start)