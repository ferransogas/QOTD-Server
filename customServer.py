import json
import socket
import random
import datetime

HOST = 'localhost'
PORT = ''	# assign a port
FILE = "quotes.json"

with open(FILE, 'r') as file:
	qotd_list = json.load(file)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)


def cmd_impl(cmd_raw):
	try:
		cmd = json.loads(cmd_raw)	# converts the command from JSON format to a dictionary
		
		op = cmd['op']
		if op == 'get':
			# receives a quote
			mode = cmd['mode']
			if mode == 'random':
				return random.choice(qotd_list)
	
			elif mode == 'day':
				return qotd_list[datetime.now().day]
			
			elif mode == 'index':
				index = cmd['index']
				return qotd_list[index-1]
			else:
				return {'res':'KO'}
	
		elif op == 'count':
			# receives the number of quotes
			return len(qotd_list)
	
		elif op == 'add':
			# adds a quote
			qotd = cmd['quote']
			if qotd not in qotd_list:
				qotd_list.append(cmd['quote'])
				return {'res':'OK'}
			else:
				return {'res':'KO'}
		else:
			return {'res':'KO'}
	except:
		return {'res':'KO'}

while 1:
	conn, addr = s.accept()
	print ('Connected by', addr)
	
	cmd_raw = conn.recv(1024).decode('utf-8')
	if not cmd_raw:
		break
	
	conn.send(json.dumps(cmd_impl(cmd_raw)).encode('utf-8'))
	conn.close()



	

		

