from pymongo import MongoClient
from helpers import MONGO_URI
import datetime



class DB_ctrl:
	def __init__(self):
		self.client = MongoClient(MONGO_URI)
		self.db = self.client.bot
		self.users = self.db.users
		self.messages = self.db.messages
		print("DB Connected")

	def _get_user(self, contact):
		return self.users.find_one({"contact": contact})

	def _add_user(self, name, number):
		obj = {
			"name" : name,
			"contact": number,
			"date_joined": datetime.datetime.utcnow()
		}
		self.users.insert_one(obj)

	def _add_message(self,recv, text, user_id):
		obj = {
			"user_id" : user_id,
			"request" : recv,
			"response" : text[0],
			"res_media" : text[1],
			"date" : datetime.datetime.utcnow()
		}
		self.messages.insert_one(obj)