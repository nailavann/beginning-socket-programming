import socket                

s = socket.socket()          

host = "127.0.0.1"
port = 8080

try:
    s.connect((host, port)) 

    yanit = s.recv(1024)
    print(yanit.decode("utf-8"))
    
    s.close() 


except socket.error as msg:
    print(msg)