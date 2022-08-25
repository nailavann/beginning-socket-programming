import socket

host = "localhost"
port = 8080

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port)) 

    s.listen(1)      
    print("Dinliyor.")
    
except socket.error as msg:
    print(msg)

while True: 

   c, addr = s.accept()      
   print('Gelen bağlantı:', addr)

   mesaj = 'Bağlandınız'
   c.send(mesaj.encode('utf-8')) 

   c.close()