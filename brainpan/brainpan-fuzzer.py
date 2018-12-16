import socket

buf = ['A']
counter = 100

while len(buf) <= 30:
	buf.append('A'* counter) 
	counter += 100

for el in buf:
	print("[*]sending %s bytes" % len(el))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 9999))
	s.recv(1024)
	s.send(el + '\r\n')
	s.close()
	print("[*]Done")
