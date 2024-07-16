import socket

host_name = socket.gethostname()
print(host_name)

ip_address = socket.gethostbyname(host_name)
print(ip_address)


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print('Error creating socket'+ e)

