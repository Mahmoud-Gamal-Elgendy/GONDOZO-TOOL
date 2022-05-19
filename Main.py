from Moduels.DesignGon.DesGondozo import Design        
from Moduels.Getiplib.Getip import Getipadd
from Moduels.ipLocationlib.ipLocation import Ip
from Moduels.PortScanlib.PortScan import port
from Moduels.WebScrappinglib.WebScrapping import Scrap

#to use design file
Design.Gon()
#to use getip file
hostname=input("Enter the hostname  : ")  #input the host name in hostname variable
ip=Getipadd.ipgetter(hostname) 
print("\n")
print("The IP Address For "+hostname+" is "+ip) #to print the ip address for hostname variable
print("\n")
#to get ip location 
loc=Ip.loc(ip)
print(loc)
print("\n")
#to do port scan for ip 
port.scan(ip)
print("\n")
#search about ip in whois website and print the result using WebSrapping lib
result=Scrap.whois(ip)
print(result)