import socket


url = input('Enter URL: ')
#use split('/') to break the URL into its component parts so you can extract the host name
host = url.split('/')[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET http://'+url+' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

received = list()

while True:
    #The return value is a bytes object
    data = mysock.recv(1000)
    if len(data) < 1:
        break
    #make a list of bytes
    received.append(data.decode())
    for line in received:
        line = line.split('\n')
        print(line)
        

mysock.close()
