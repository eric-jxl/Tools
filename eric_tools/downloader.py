import asyncio
import aiohttp
import os
import time
from collections import deque

class Downloader:
    def __init__(self, urls, max_concurrent=5, delay=0):
        self.urls = deque(urls)
        self.max_concurrent = max_concurrent
        self.delay = delay
        self.queue = asyncio.Queue()
        self.session = aiohttp.ClientSession()

    async def download(self, url):
        async with self.session.get(url) as response:
            filename = os.path.basename(url)
            with open(filename, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
        print(f"{url} downloaded")

    async def worker(self):
        while True:
            url = await self.queue.get()
            try:
                if self.delay:
                    time.sleep(self.delay)
                await self.download(url)
            except Exception as e:
                print(f"Error downloading {url}: {e}")
            self.queue.task_done()

    async def run(self):
        for url in self.urls:
            self.queue.put_nowait(url)

        tasks = []
        for _ in range(self.max_concurrent):
            task = asyncio.create_task(self.worker())
            tasks.append(task)

        await self.queue.join()

        for task in tasks:
            task.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)
        await self.session.close()

if __name__ == "__main__":
    urls = ["https://example.com/file1.txt", "https://example.com/file2.txt", "https://example.com/file3.txt"]
    downloader = Downloader(urls, max_concurrent=2, delay=1)
    asyncio.run(downloader.run())