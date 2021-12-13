import socket

host = "192.168.1.111"
port = 80

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.connect((host,port))

while 1:

    data = input("Mssage:")

    if data.encode("utf-8")=="exit":
        print("Bir kullanıcı ayrıldı.")
    else:
        s.sendall(data.encode("utf-8"))

    
    ldata = s.recv(1024)

    if ldata.decode("utf-8") == "exit":
        print("Bir kullanıcı ayrıldı.")

    else:
        ldata.decode("utf-8")