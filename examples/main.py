import asyncio
from ducts_client import Duct

class MyPlayground:
    def __init__(self):
        self.duct = Duct()

    async def catchall_event_handler(self, rid, eid, data):
        print(eid, data) 

    async def on_open(self, event):
        await self.duct.send(self.duct.next_rid(), self.duct.EVENT["LIST_PROJECTS"], None)

    async def main(self):
        self.duct.connection_listener.onopen = self.on_open
        self.duct.catchall_event_handler = self.catchall_event_handler
        await self.duct.open("http://localhost/ducts/wsd")

if __name__=="__main__":
    pg = MyPlayground()
    asyncio.run(pg.main())
