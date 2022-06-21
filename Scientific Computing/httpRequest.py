import socket


fhand = open('D:\Programming\Python\Github\Python_General\Scientific Computing\dataRecievedFromSocketCall.html', 'w')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	mysock.connect(('data.pr4e.org', 80))
	cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
	mysock.send(cmd)

	while True:
		data = mysock.recv(8)
		if len(data) < 1:
			break
		fhand.write(data.decode())
		print(data.decode(), end='')
	mysock.close()
except Exception as error:
	print(error)
fhand.close()
