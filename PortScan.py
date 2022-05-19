#this library to use ports and ip
import socket 

class port:
    def scan(ip):
         print("=======================")
         print("    Scanning Result    ")
         print("=======================")
         ports=[19,20,21,22,23,24,25,80,443,53,411,412,465,500,5050,5190,5554,6699,6999,8000,12345] #list of ports
         for port in ports:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # for ipv4
            s.settimeout(2) #wait 5 seconds
            r=s.connect_ex((ip,port)) #to connected ip and start test ports
            if r==0: #the port is open
                service=socket.getservbyport(port) #to get the service name of the port
                print("[{} is open ] ==> {}".format(port,service))
            s.close()