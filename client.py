import socket,sys,time #impordib socket, sys ja time

s = socket.socket() #teeb socket.socket() rea lühemaks.
host = input(str("Please enter the hostname of the server: ")) #Kasutaja peab sisestama serveri nime
port = 8080 #port
s.connect((host,port)) #kontrollib kas host ja port vastab tõele
print("Connected to chat server") #prindib, on ühendatud chat serveriga
while 1: #kuni 1

    incoming_message=s.recv(1024) #võtab kirju vastu
    incoming_message=incoming_message.decode() #decodib kirja
    print ("Server: ",incoming_message) #prindib, server ja siis kuvab selle järel serveri poolt saadetud kirja
    print("") #prindib tühja rea
    message=input(str(">> ")) #kasutaja saab sisestada kirja, mida ta soovib saata
    message=message.encode() #see kiri encoditakse
    s.send(message) #saadab kirja
    print("") #prindib tühjarea
