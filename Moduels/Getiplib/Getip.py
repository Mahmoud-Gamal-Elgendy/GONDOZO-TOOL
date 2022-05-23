#this library to use ports and ip
import socket 

try:
    class Getipadd:
        def ipgetter(hostname):
            print("====================")
            print("      IP Result     ")
            print("====================")
            ip=socket.gethostbyname(hostname)  # get ip for host name and save that in ip variable
            return ip
except:
    print("Error in Get IP of The Target!")   