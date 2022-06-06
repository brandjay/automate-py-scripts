import socket 
sitename = input("What websites IP would you like to find? ")
print(f' the {sitename} IP address is: {socket.gethostbyname(sitename)}')
