import random

def main():
    """Start an elements guessing game."""
    print ("Start The Game")
    
    name = input(str("What Is Your Name? "))
    # Here the user is asked to enter the name first
    
    print("Selamat Mencuba >3", name)
    
    print("")
    print("Oxygen")
    print ("Hydrogen")
    print("Helium")
    print("Neon")
    print("Calcium")
    print("Sodium")
    print("Silicon")
    print("Chlorine")
    print("Iodine")
    print("Copper")
    
    
    # list of element
    element_list = ["Oxygen","Hydrogen","Helium","Neon","Calcium","Sodium","Silicon","Chlorien","Iodine","Copper"]
    
    x = random.choice (element_list)
    guess = None
    while x != guess:
        
        guess = str(input("Pick an element: "))
        
        if x == guess:
            print("CONGRATULATIONS,YOU'RE CLEVER")
        elif x != guess:
            print("Try another one.")
            
main()
               