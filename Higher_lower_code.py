# Higher-Lower Game:

from rich.console import Console
from art import logo, vs

dic = {
    "Mukesh Ambani (Relaince)": 115.8,
    "Gautam Adani (Infrastructure)": 81.1,
    "Bill Gates (Microsoft)": 126.9,
    "Elon Musk (Tesla, SpaceX)": 198.1,
    "Jensen Huang (Nvidia)": 73.4,
    "David Thomson (Media)": 66.1,
    "Larry Ellison (Oracle)": 143.8,
    "Larry Page (Google)": 136.3,
    "Sergey Brin (Google)": 130.7,
    "Steve Ballmer (Microsoft)": 118.5,
    "Jim Walton (Walmart)": 77.2,
    "Michael Bloomberg (Bloomberg LP)": 106.2,
    "Francoise Bettencourt Meyers (L'Oréal)": 95.3,
    "Amancio Ortega (Zara)": 105.3,
    "Carlos Slim Helu (Telecom)": 99.9,
    "Rob Walton (Walmart)": 76.2,
    "Bernard Arnault (LVMH)": 209.0,
    "Michael Dell (Dell Tech)": 90.8,
    "Zhong Shanshan (Beverages)": 67.4,
    "Alice Walton (Walmart)": 71.1,
    "Mark Zuckerberg (Facebook)": 154.5,
    "Julia Koch (Koch Industries)": 65.3,
    "Warren Buffett (Berkshire Hathaway)": 131.5,
    "Jeff Bezos (Amazon)": 198.2,
    "Prajogo Pangestu (Petrochemicals)":59.6
}

def clearall():
    console = Console()
    console.clear()

def compare(dic):
    clearall()
    
    i = 1
    score = 0 
    for key in dic:
        print(logo)
        
        # list of all the keys of dictionary
        lst = list(dict.keys(dic))
        
        # all keys of dictionary
        print(f"Compare A: {key}")
        
        print(vs)
        
        # iterating the list 
        print(f"Against B: {lst[i]}")
        
        a = dic[key]
        b = dic[lst[i]]
        
        cmp = input("\nWho is more rich? Type 'A' or 'B' -> ").lower()
        
        i += 1
        clearall()
        
        # if player reaches to the end of the game
        if (i == 24):
            print(f"✨ Hurry! You had completed the Game. ✨")
            
            press = input(f"Want to play Again? Type 'y' or 'n' -> ")
            
            if (press == 'y'):
                clearall()
                compare(dic)
            else:  
                break
        
        # Determining the correct answer
        if (cmp == 'a'):
            if (a > b):
                score += 1
                print("**************************************\n")
                print(f"You're Right ✔️  -> Current Score is {score}\n")
                print("**************************************\n")
            else:
                print("****************************************\n")
                print(f"Sorry! Incorrect ❌  -> Your Score is {score}\n")
                print("****************************************\n")
                
                # if player wants to play again
                press = input(f"Want to play Again? Type 'y' or 'n' -> ")
                if (press == 'y'):
                    clearall()
                    compare(dic)
                else:  
                    break

        elif (cmp == 'b'):
            if (a < b):
                score += 1
                print("**************************************\n")
                print(f"You're Right ✔️  -> Current Score is {score}\n")
                print("**************************************\n")
            else:
                print("****************************************\n")
                print(f"Sorry! Incorrect ❌  -> Your Score is {score}\n")
                print("****************************************\n")
                
                # if player wants to play again
                press = input(f"Want to play Again? Type 'y' or 'n' -> ")
                if (press == 'y'):
                    clearall()
                    compare(dic)
                else:  
                    break
        
        else:
            clearall()
            
            print(f"⚠️ Please Enter Valid Option ⚠️")
            
            press = input(f"Want to play Again? Type 'y' or 'n' -> ")
            
            if (press == 'y'):
                clearall()
                compare(dic)
            else:  
                break
       
compare(dic)