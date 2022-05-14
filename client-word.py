#client-word.py

#import from library to get methods from these specific libraries
import socket
import sys
import time

myHost='127.0.0.1' #IP address of localhost
myPort=50159 #non-reserved port number
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #create a socket object 
clientSocket.connect((myHost,myPort)) #use the socket to try and connect to the server

query=input() #where you will type in query

clientSocket.send(query.encode()) #send that query to server

while True: #continue in the loop until server says they are done sending packets
    data=clientSocket.recv(1024).decode() #decode the received message from bytes to string
    if data=="The server is done sending packets": #message server sends when it is done sending packets. 
        break #break out of the while loop
    print(data) #print all the words for the query

clientSocket.close() #client disconnects
