import socket,sys,time #impordib socket, sys ja time

s=socket.socket() #lühendab socket.socket rida
host = socket.gethostname() #otsib hosti
print("server will start on host: ",host) #prindib kliendi arvuti nime
port = 8080 #port
s.bind((host,port)) #paneb kokku serveri hosti ja pordi ühendamiseks
print("") #prindib tühirea
print("Server done binding to host and port succesfully") #prindib server saab ühendada host ja pordiga
print("")
print("Server is waiting for incoming connections") #Server ootab ühendusi
s.listen(1) #kuulab ühendaiaid

conn,addr=s.accept() #Võtab hosti vastu
print(addr,"Has connected to the server and is now online...") #Prindib, et on ühendanud serveriga ja on nüüd online
print("") #prindib tühja rea

while 1: #kuni 1
    message=input(str(">> ")) #kasutaja saab sisestada teksti, mida soovib saata
    message=message.encode() #encodib kirja
    conn.send(message) #Kiri saadetakse
    print("message has been sent....") #prindib, kiri on edukalt saadetud
    print("") #prindib tühjarea
    incoming_message=conn.recv(1024) #võtab kirju vastu
    incoming_message=incoming_message.decode() #decodib kirja loetavale kujule
    print ("Client: ",incoming_message) #pridnib klient ja klienti poolt saadetud kirja
    print("") #prindib tühja rea
















