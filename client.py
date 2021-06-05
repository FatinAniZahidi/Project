import socket
import os
from _thread import*

s = socket.socket()
ip = input(str("Enter ip address of the server: "))
port = 8000
s.connect((ip,port))
print("Successfully Connected ...\n")

respons = s.recv(1024)
print(respons)

Input = input('\nEnter name of the requested file: ')
s.send(str.encode(Input))
response = s.recv(1024)
print(response.decode('utf-8'))


filename = input(str("\nEnter a filename for the incoming file: "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been successfully received!\n")

s.close()
