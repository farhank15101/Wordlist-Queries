# Wordlist-Queries

This program consists of a server and client in a TCP connection. The client sends a query to the server and the server looks at each line in a wordlist.txt file to return all the words 
that match that query. An example of a query is ac*or and some of the words that match this query are activator, actor, and accelerator. The server then sends a message to the client that indiciates that it is done sending words that match the query that was sent by the client. 
