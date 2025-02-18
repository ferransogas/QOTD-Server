import socket
import json
import sys
import time

HOST = ''
PORT = ''	# assign a port

while True:
	if len(sys.argv) < 2:
		# sys.argv takes the command from the keyboard, sys.argv[0] = file name, sys.argv[1] = "-op"
		break
	
	op = sys.argv[2]
	if op == 'get':
		if len(sys.argv) < 4:
			break
	
		mode = sys.argv[4]
		if mode == 'random':
			cmd = json.dumps({'op':'get', 'mode': 'random'})
	
		elif mode == 'day':
			cmd = json.dumps({'op':'get', 'mode': 'day'})
	
		elif mode == 'index':
			if len(sys.argv) < 6:
				break
			index = int(sys.argv[6])
			cmd = json.dumps({'op':'get', 'mode': 'index', 'index': index})
		
		else:
			break
	
	elif op == 'add':
		if len(sys.argv) < 4:
			break
		qotd = str(sys.argv[4])
		cmd = json.dumps({'op': 'add', 'quote': qotd})
	
	elif op == 'count':
		cmd = json.dumps({'op': 'count'})
	
	else:
		break

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(cmd.encode('utf-8'))
	qotd_recv = s.recv(512).decode('utf-8')
	print(qotd_recv)
	s.close()
	
	time.sleep(2)
	
