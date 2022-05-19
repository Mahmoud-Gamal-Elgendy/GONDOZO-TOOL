#webscrapping lib
import requests
from bs4 import BeautifulSoup

class Scrap:
    def whois(ip):
            print("====================")
            print("    Whois Result    ")
            print("====================")
            print("\n")
            result=requests.get("https://www.whois.com/whois/"+ip) #search about ip
            getpage=result.content #get the content of page in variable getpage
            soup=BeautifulSoup(getpage,"lxml")
            whois_data=soup.find_all("div",{"class":"df-block"}) #get the result and store it in whois_data
            return whois_data