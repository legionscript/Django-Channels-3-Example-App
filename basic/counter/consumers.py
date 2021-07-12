import json
from time import sleep
from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()

		count = 0
		for i in range(1000):
			if count < 10:
				count += 1
				self.send(json.dumps({'message': count}))
				sleep(1)
			else:
				count = 1
				self.send(json.dumps({'message': count}))
				sleep(1)