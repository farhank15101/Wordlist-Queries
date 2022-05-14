#server-word.py

#import from library to get methods from libraries
import socket
import sys
import time

myHost='127.0.0.1' #IP address of localhost
myPort=50159 #non-reserved port number
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #create socket object
serverSocket.bind((myHost,myPort)) #bind to server port number
serverSocket.listen(1) #listen for one connection


connection,address=serverSocket.accept() #accept client's request to connect

queryRequest=connection.recv(1024).decode() #recieve query from client and converts from bytes to strings
words=open("wordlist.txt","r") #open .txt file
lines=words.readlines() #allows you to read the file line by line
time.sleep(5) #wait for 5 seconds
for line in lines: #loop through the lines to find words
    splitline=line.split("(") #done so that the actual words are being compared to the query if there is a parenthesis
    length1=len(queryRequest)-1; #length of query excluding asterick
    if queryRequest[0]=="*": #if asterick is beginning of query
        if queryRequest[1:]==splitline[0][0-length1-1:-1]: #compares only the letters of query to specific letters in the line
            time.sleep(0.1) #make the program run more efficently
            connection.send(splitline[0].encode()) #sends the line to the client if it matches the query
    elif queryRequest[-1]=="*": #if asterick is at the end of the query
        if queryRequest[0:-1]==splitline[0][0:length1]: #compares letters of query to certain letters in the line
            time.sleep(0.1) #make the program run more efficently
            connection.send(splitline[0].encode()) #sends the line to query if the if statement is true
    else:
        splitquery=queryRequest.split("*") #if asterick is in the middle, split the words between them into two
        length2=len(splitquery[0]) #the letters before the asterick
        length3=len(splitquery[1]) #the letters after the asterick 
        if splitquery[0]==splitline[0][0:length2] and splitquery[1]==splitline[0][0-length3-1:-1]: #two comparisons made to see if each segment of query matches each specific segments of the line
            time.sleep(0.1) #make the program run more efficiently 
            connection.send(splitline[0].encode()) #send the line to the client if the line matches the requirements to match the query

endmessage="The server is done sending packets" #message to be sent
connection.send(endmessage.encode()) #send the message to the client 



connection.close() #server disconnects

    


