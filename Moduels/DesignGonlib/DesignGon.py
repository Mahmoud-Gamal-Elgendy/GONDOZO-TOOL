# To create my Designe gondozo tool Use pyfiglet lib
from pyfiglet import figlet_format

try:
    class Design:
        def Gon():
            print("\n")
            print(figlet_format("Gondozo Tool ",font="standard"))
            print("***************************************************************************************************")
            print("")
            print("* Developed By Mahmoud El-Gendy ,2022                                                             *")
            print("* Linkedin : https://www.linkedin.com/in/mahmoud-elgendy-4650021a0/                               *")
            print("* GitHub   : https://github.com/Mahmoud-Gamal-Elgendy                                             *")
            print("")
            print("***************************************************************************************************")
except:
    print("Error in Generate The Design of Tool!")           