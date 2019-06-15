import socket
import sys
print ("Simple Port Scanner using socket lib")
print("Usage: python scanner.py startport endport")
port_strt=sys.argv[1]
port_end=sys.argv[2]

ip_addr = input("IP->")

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
for n in range(int(port_strt),int(port_end)):
    if sock.connect_ex((str(ip_addr),n)):           
        print("Port is closed!",n)
    else:
        print("Port is open!",n)

