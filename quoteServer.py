import socket
import json
import random

HOST = 'localhost'
PORT = 0	# assign a port
FILE = "quotes.json"

with open(FILE, 'r') as file:
	# load json into a list
	qotd_list = json.load(file)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while 1:
	conn, addr = s.accept()
	print ('Connected by', addr)
	
	rand_quote = random.choice(qotd_list)
	if not rand_quote: 
		break
	conn.send(rand_quote.encode('utf-8'))
	conn.close() 
