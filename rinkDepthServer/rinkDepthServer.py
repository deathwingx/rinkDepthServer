from socket import *
from datetime import date

HOST = ''
PORT = 9090

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
today = date.today()
file = r'C:\Users\berna\Documents\rinkDepth\\'
#file+=today.strftime("%m/%d/%y")
file+='test'
file+='.csv'
f = open(file, 'x')
s.listen(5)
while True:
	c, addr = s.accept()
	print('Connected to: ',addr)
	l = c.recv(1024)
	while (l):
		print('Receiving...\n')
		f.write(l.decode())
		l = c.recv(1024)
	#c.send(b'Received!')
	#c.send()
	f.close()
	print('Done!')
	c.close()

# with socket(AF_INET, SOCK_STREAM) as sock:
# 	sock.bind((HOST, PORT))
# 	sock.listen(1)
# 	conn, addr = sock.accept()
# 	with conn:
# 		print('Connected by: ', addr)
# 		while True:
# 			data = conn.recv(1024)
# 			print(data.decode())
# 			if not data: break
# 			conn.sendall(b'Recieved')
# 			#conn.sendall(data)
# 		conn.close()
# 		sock.close()