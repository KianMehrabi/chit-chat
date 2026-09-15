from channels.generic.websocket import AsyncWebsocketConsumer


class HahahaConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        print("hahaha:", text_data)

    async def disconnect(self, close_code):
        pass
