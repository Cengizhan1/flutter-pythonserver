import socket

host = "192.168.1.111"
port = 80

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen()

conn,addr = s.accept()

if conn:
    print("Bir kullanıcı baglandı:{addr}")
    while 1:
        ldata = conn.recv(1024)

        if ldata.decode("utf-8") == "exit":
            conn.close()
        else:
            print(ldata.decode("utf-8"))

        
        data=input("message:")

        if data.encode("utf-8") == "exit":
            conn.close

        else:
            conn.sendall(data.encode("utf-8"))
        
