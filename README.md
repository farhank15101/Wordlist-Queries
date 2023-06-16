# Wordlist-Queries

This program consists of a server and client in a TCP connection. The client sends a query to the server and the server looks at each line in a wordlist.txt file to return all the words 
that match that query. An example of a query is ac*or and some of the words that match this query are activator, actor, and accelerator. Once all matching words are found, the server sends a message to the client indicating that it has finished sending the matching words for the client's query.
