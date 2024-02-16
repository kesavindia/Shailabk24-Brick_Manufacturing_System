import socket
host = input('Enter a website name to get IP address:')

try:
    addr = socket.gethostbyname(host)
    print('IP Address = '+ addr)
except socket.gaierror:
    print('The website does not exist')
