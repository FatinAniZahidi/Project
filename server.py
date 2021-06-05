import socket
import os
from _thread import*

s = socket.socket()
ip = ('192.168.56.104')
port = 8000
ThreadCount = 0

s.bind((ip,port))

s.listen(2000)
print(ip)
print(port)
print("\nWaiting for incoming connections ...\n")
print("----------------------------------------------")

def threaded_client(connection):
	connection.send(str.encode('File available = server2.py'))
	while True:
		data = connection.recv(1024)
		reply = 'Server notice your requested file : '+data.decode('utf-8')
		if not data:
			break
		connection.sendall(str.encode(reply))	
	connection.close()


while True:
	
	connect, addr = s.accept()
	print('\nConnected to :'+addr[0]+':'+str(addr[1]))
	start_new_thread(threaded_client, (connect, ))

	ThreadCount += 1
	print('Client Number : '+str(ThreadCount))
	
	
	filename = input(str("\nEnter back the filename of the file : "))
	file = open(filename , 'rb')
	file_data = file.read(1024)
	connect.send(file_data)
	print("Data has been successfully transmitted!\n")
	
s.close()
