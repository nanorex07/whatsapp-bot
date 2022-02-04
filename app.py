from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random
from helpers import *
from db_ctrl import *

app = Flask(__name__)


@app.route("/")
def index():
	return "Hello, World!"

db = DB_ctrl()

@app.route("/sms", methods=['POST'])
def reply():
	response = MessagingResponse()
	recv = request.form.get('Body')
	name = request.form.get('ProfileName')
	number = request.form.get('From')[9:]

	user = db._get_user(number)

	if user:
		text = ["",""]
		if recv not in OPTIONS_LIST:
			m = response.message(UNKNOWN_ERROR)
		else:
			if recv == '1':
				m = response.message("Here's a random image for you")
				im = get_rand_image()
				m.media(im)
				text[0] = "Here's a random image for you"
				text[1] = im

			elif recv == '3':
				q = get_rand_quote()
				m = response.message(q)
				text[0] = q;

			elif recv == '4':
				m = response.message(LIST_TEXT)
				text[0] = LIST_TEXT

			else:
				m = response.message("Here's a random doc")
				m.media(DOC_URL)
				text[0] = "Here's a random doc"
				text[1] = DOC_URL
		db._add_message(recv, text, user["_id"])

	else:
		m = response.message(INTRO_TEXT.format(name) + LIST_TEXT)
		db._add_user(name, number)

	return str(response)

if __name__ == "__main__":
	app.run(debug=True, port=4040)
