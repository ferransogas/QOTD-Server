import json
import socket
import time

FILE = "quotes.json"
PORT = 17

qotd_srvs = ['djxmmx.net', 'cygnus-x.net', 'alpha.mike-r.com']
qotd_list = []

i = 0
while len(qotd_list) < 31:
	# don't stop until we get 31 quotes
	actual_srv = qotd_srvs[i % len(qotd_srvs)]	# rotate between the 3 servers
	try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# tcp
		s.settimeout(5)	# if the connection takes too long, it prevents it
		s.connect((actual_srv, PORT))
		actual_qotd = s.recv(512).decode('utf-8')
		if actual_qotd not in qotd_list:
			qotd_list.append(actual_qotd)
			print(f"{len(qotd_list)}/31")
		s.close()

	except Exception as e:
		print(f'Error: {e}')

	i += 1
	time.sleep(2)

with open(FILE, 'w') as file:
		# save the list to a JSON file
        json.dump(qotd_list, file)

 


