import random
import requests

INTRO_TEXT = '''
Welcome {}
I am a RU-Bot
'''

LIST_TEXT = '''
Choose from below actions:
1. Send Image
2. Send Document
3. Send a message
4. Send List
'''

OPTIONS_LIST = ['1','2','3','4']

QUOTE_URL = "https://zenquotes.io/api/random"

UNKNOWN_ERROR = '''
Sorry! Can't process that response. Try "4" to list available options.
'''
DOC_URL = "http://www.africau.edu/images/default/sample.pdf"

MONGO_URI = "<MONGO URI>"

def get_rand_image():
	return f"https://picsum.photos/{random.randint(200,600)}"

def get_rand_quote():
	res = requests.get(QUOTE_URL).json()
	return "Here's a quote for you:\n\n"+res[0]['q']+'\n-'+res[0]['a']