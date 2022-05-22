import argparse     #to use parsing and enter data with terminal
from Moduels.DesignGonlib.DesignGon import Design
from Moduels.Getiplib.Getip import Getipadd
from Moduels.ipLocationlib.ipLocation import Ip
from Moduels.PortScanlib.PortScan import port
from Moduels.WebScrappinglib.WebScrapping import Scrap

#use parser
parser=argparse.ArgumentParser(description="Pen-testing tool")
parser.add_argument("-N","--hostname",type=str,help="Enter the host name")
args=parser.parse_args()
hostname=args.hostname
if hostname==None:
    print(parser.usage)
else:
    #to use design file
    Design.Gon()
    print("\n")
    #to use getip file
    ip=Getipadd.ipgetter(hostname) 
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