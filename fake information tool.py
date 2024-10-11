import os
import time
from faker import Faker
from faker.providers import internet
from colorama import init, Fore
from colorama import init
init(autoreset=True)
print(Fore.BLUE+"""
___        __                            _   _             
|_ _|_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __  
 | || '_ \| |_ / _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
 | || | | |  _| (_) | |  | | | | | | (_| | |_| | (_) | | | |
|___|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|
                                                           
 _____     _                                                 
|  ___|_ _| | _____ _ __                                     
| |_ / _` | |/ / _ \ '__|                                    
|  _| (_| |   <  __/ |                                       
|_|  \__,_|_|\_\___|_|                                       
                                     ⚡️⚡️⚡️⚡️⚡️⚡️                          
                                                 #by Rlkcode
""")
time.sleep(2)
def id_card():
    f = Faker()
    num_repeats = int(input('==> How many do you want? '))
    os.system('clear')
    time.sleep(3)
    for _ in range(num_repeats):
        print("---------id card----------")
        print("Name:"+f.name())
        print("Date of birth:",f.date_of_birth())
        print("Address:"+f.address())
        print("Email:"+f.email())
        print("Company Name:"+f.company())
        print("Country:"+f.country())
        print("Number phone:"+f.phone_number())
        print("Job:"+f.job())
        input(Fore.GREEN+"Press Enter to more...")
        os.system("clear")
def credit_card():
    f = Faker()
    num_repeats = int(input('==> How many do you want? '))
    for _ in range(num_repeats):
        print("_______credit card___________")
       
        print("Card Name:"+f.name())
        print("Card Number:"+f.credit_card_number())
        print("Expiration Date:"+f.credit_card_expire())
        print("Card Provider:"+f.credit_card_provider())
        input(Fore.GREEN+"Press Enter to more...") 
        os.system("clear")        
def main():
    while True:
        print( Fore.WHITE+"==> What do you want :")
        print("[1] ID_card 📋")
        print("[2] Credit_card 💳")
        print("[3]Exit")      
        choice = input("Enter =>:")
        os.system('clear')
        if choice == '1':
            id_card()        
        elif choice == '2':
                        credit_card()       
        elif choice == '3':                     
            break
        else:
            input(Fore.RED+"try again..")  
            os.system('clear')
            input(Fore.WHITE)
if __name__ == "__main__":
  main()
