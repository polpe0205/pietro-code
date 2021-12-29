import socket 


#oggetto soket
s =  socket.socket ()
#connesione a google 
s.connect(("www.google.it", 80 ))

print  (s) 


#richiesta home page google 
richiesta = "GET / HTTP/1.1\nHOST: www.google.it\n\n"
s.send(richiesta.encode())

risposta = s.recv(2048)
while len (risposta)   > 0:
    print(risposta)
    risposta = s.recv(2048)