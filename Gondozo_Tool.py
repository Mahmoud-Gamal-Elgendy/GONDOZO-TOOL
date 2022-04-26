import socket #this library to use ports and ip
import requests #webscrapping lib
import lxml
from bs4 import BeautifulSoup #webscrapping lib
import json #this lib to get ip location
from pyfiglet import figlet_format # To create my Designe gondozo tool


#print gondozo tool
print("\n")
print(figlet_format("Gondozo Tool ",font="standard"))
print("***************************************************************************************************")
print("")
print("* Developed By Mahmoud El-Gendy ,2022                                                             *")
print("* Linkedin : https://www.linkedin.com/in/mahmoud-elgendy-4650021a0/                               *")
print("* GitHub   : https://github.com/Mahmoud-Gamal-Elgendy                                             *")
print("")


#get ip
try:
    print("***************************************************************************************************")
    print("")
    hostname=input("Enter the hostname  : ")  #input the host name in hostname variable
    print("")
    ip=socket.gethostbyname(hostname)  # get ip for host name and save that in ip variable
    print("The IP Address For "+hostname+" is "+ip) #to print the ip address for hostname variable
    print("\n")
except:
    print("We have Error !!! ")


#find ip geolocated
try:
    print("===========================")
    print("    THE LOCATION OF IP    ")
    print("===========================")
    request_for_geo=requests.get("https://geolocation-db.com/jsonp/"+ip) #send requst to URL
    result_for_geo=request_for_geo.content.decode() #decode the result
    result_for_geo = result_for_geo.split("(")[1].strip(")") # Clean the returned string so it just contains the dictionary data for the IP address
    result_for_geo  = json.loads(result_for_geo) # Convert this data into a dictionary
    print(result_for_geo)
    print("\n")
except:
    print("We have Error !!! ")


#port scan
try:
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
    print("\n")
except:
    print("We have Error !!! ")


#search about ip in whois website and print the result
try:
    print("====================")
    print("    Whois Result    ")
    print("====================")
    result=requests.get("https://www.whois.com/whois/"+ip) #search about ip
    getpage=result.content #get the content of page in variable getpage
    soup=BeautifulSoup(getpage,"lxml")
    whois_data=soup.find_all("div",{"class":"df-block"}) #get the result and store it in whois_data
    print(whois_data)
    print("\n")
except:
    print("We have Error !!! ")
