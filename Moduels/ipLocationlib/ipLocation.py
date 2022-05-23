import json          #this lib to get ip location
import requests      #webscrapping lib

try:
    class Ip:
        def loc(ip):
            print("===========================")
            print("    THE LOCATION OF IP    ")
            print("===========================")
            request_for_geo=requests.get("https://geolocation-db.com/jsonp/"+ip) #send requst to URL
            result_for_geo=request_for_geo.content.decode() #decode the result
            result_for_geo = result_for_geo.split("(")[1].strip(")") # Clean the returned string so it just contains the dictionary data for the IP address
            result_for_geo  = json.loads(result_for_geo) # Convert this data into a dictionary
            return result_for_geo
except:
    print("Error in Detect IP's Location of The Target!")        