import asyncio


class AsyncMessageQueue:
    def __init__(self, num_workers=3):
        self.queue = asyncio.Queue()
        self.num_workers = num_workers

    async def process_message(self, message):
        raise NotImplementedError

    async def worker(self):
        while True:
            message = await self.queue.get()
            await self.process_message(message)
            self.queue.task_done()

    async def start(self):
        tasks = [asyncio.create_task(self.worker())
                 for _ in range(self.num_workers)]

        # 等待所有任务完成
        await self.queue.join()
        for task in tasks:
            task.cancel()


class EmailMessageQueue(AsyncMessageQueue):
    async def process_message(self, message):
        # 模拟发送邮件的耗时操作
        await asyncio.sleep(2)
        print(f"发送邮件: {message}")


async def main():
    email_queue = EmailMessageQueue()

    # 向队列中添加消息
    for i in range(5):
        await email_queue.queue.put(f"邮件{i}")

    await email_queue.start()

if __name__ == "__main__":
    asyncio.run(main())
