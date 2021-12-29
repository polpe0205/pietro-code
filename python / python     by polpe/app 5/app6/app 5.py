import sys
import socket



socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



for host  in range (110, 150):
    ports  = open ('porte.txt', 'r')
    for port in ports:
        try:
            socket. connect((str(sys.argv[1]+'.'+str(host)), int(port)))
            print ('connesione in corso')+str(sys.argv[1]+'.'+str(host))+ nella porta: + str(port)
            socket.settimeout(1)
            banner = socket.recv (1024)
            for vulnbanner in vulnbanner:
                if banner.strip() in vulnbanner.strip():
                    print ('ok ho trvato qual cosa ' ) +banner
                    print ('host') +str(sys.argv[1]+'.'+str(host))
        except :
            #print 'errore di connessione: ' 
            pass