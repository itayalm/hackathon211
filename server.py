import socket as soc



s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
s.bind(('172.1.0.123', 50000))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break
    print(data)
    print(data)
    conn.sendall(data)
conn.close()