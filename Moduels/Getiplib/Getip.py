#this library to use ports and ip
import socket 

class Getipadd:
    def ipgetter(hostname):
        print("====================")
        print("      IP Result     ")
        print("====================")
        ip=socket.gethostbyname(hostname)  # get ip for host name and save that in ip variable
        return ip
        