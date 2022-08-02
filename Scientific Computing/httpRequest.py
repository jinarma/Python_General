import socket
import urllib.request


def socket_request(url, port, page):
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		mysock.connect((url, port))
		cmd = f'GET http://{url}/{page} HTTP/1.0\r\n\r\n'.encode()
		mysock.send(cmd)

		while True:
			data = mysock.recv(8)
			if len(data) < 1:
				break
			print(data.decode(), end='')
		mysock.close()
	except Exception as error:
		print(error)

def urllib_request(url):

	# retrieves headers
	data = urllib.request.urlopen(url)
	headers = data.getheaders()
	for ele in headers:
		print(ele[0], ' - ', ele[1])

	for line in data:
		print(line.decode().strip())

# socket_request('data.pr4e.org', 80, 'romeo.txt')
urllib_request('http://data.pr4e.org/romeo.txt')
