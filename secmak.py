import random

def generator(): 
    print(r""" ____   ____  _____   __  ___   ___    __ __
  / __/  / __/ / ___/  /  |/  /  / _ |  / //_/
 _\ \   / _/  / /__   / /|_/ /  / __ | / ,<        
/___/  /___/  \___/  /_/  /_/  /_/ |_|/_/|_|  
                                     
 ********************************************
                                                        """)
    
    pool = "abcdefghijklmnopqrstuvwxyz"
    
    if input("Uppercase? (y/n): ").lower() == "y":
        pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if input("Numbers? (y/n): ").lower() == "y":
        pool += "0123456789"
    if input("Symbols? (y/n): ").lower() == "y":
        pool += "!@#$%^&*()-_+="

    length = int(input("Number of characters: "))
    print("Password:", ''.join(random.choices(pool, k=length)))

generator()
