#Copyrigth©: beemicizi 2021-2021. You are free to reuse, remix and redistribute this softwere at your pleasing, 
#as per stated in the liscence.md file
import sys
import random
import time
import names
from threading import Thread
copyrigth = "Copyrigth©: beemicizi 2021-2021"
ut = ["get the number", "countdown", "random name generator", "full cpu prank", "rock paper sciccors"]
while True:
    print("Welcome to python utilyties and games!")
    print("Wat wloud you like to do?")
    print("We currently offer: ")
    for u in ut:
        print(u)
    utChoose = input()

    if utChoose == "get the number":
        global playerExit, rns, loadT

        loadT = True
        rns = False
        playerExit = False
        play_confirm = False
        while play_confirm == False:
            print("Welcome to guess the number!")
            print("Wuold you like to play? (input y or n)")
            play_confirm = input()
            if play_confirm == "y":
                break
            elif play_confirm == "cheats=true":
                rns = True
                play_confirm = False
            elif play_confirm == "load=0":
                loadT = False
                play_confirm = False
            else:
                playerExit = True
                break
            
        if playerExit == True:
            sys.exit()


        print("Ok generating random number")
        if loadT == True:   
            time.sleep(2)
        random_number = random.randint(1, 10)
        if rns == True:
            print(random_number)
        print("Generated")
        attempts = 3
        print("Please input a number between 1 and 10")

        while attempts != 0:
            print("You have " + str(attempts) + " attempts left")
            player_choice = int(input())
            if player_choice == random_number:
                print("You won!")
                if attempts == 3:
                    print("Very lucky!")
                elif attempts == 2:
                    print("GG, good game!")
                elif attempts == 1:
                    print("Saved on corner!")
                break
            elif player_choice < random_number:
                print("You got it wrong try again! Also try a little higer")
            elif player_choice > random_number:
                print("You got it wrong try again! Also try a little lower")
            elif player_choice < random_number and attempts == 0:
                print("You got it wrong try again!")
            elif player_choice > random_number and attempts == 0:
                print("You got it wrong try again!")
            elif player_choice > 10:
                print("Input in 1 and 10")
            attempts -= 1

    elif utChoose == "countdown":
        def countdown(t):
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs )
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
            print("Timer compleated! ")
        t = input("Enter the time in seconds: ")
        countdown(int(t))
        print("exiting program")
    elif utChoose == "name generator":
        print("Welcome to name generator, want to generate a name? (input y or n)")
        gn = input()
        if gn == "y":
            print("Ok strting proccess")
        elif gn == "n":
                sys.exit()

        time.sleep(5)

        print("okey dokey, what type of name. (First, last, full)")
        ton = input()
        print("Want to add a gender? (input m or f)")
        gen = input()
        print("ok generating\n")
        time.sleep(2)
        while True:
            if ton == "f":
                first = names.get_first_name()
                print(first)
                break
            elif ton == "l":
                last = names.get_last_name()
                print(last)
                break
            elif ton == "fu":
                full = names.get_full_name()
                print(full)
                break
            elif ton == "f" and gen == "m":
                first_male = names.get_first_name(gender="male")
                print(first_male)
                break
            elif ton == "l" and gen == "m":
                last_male = names.get_last_name(gender="male")
                print(last_male)
                break
            elif ton == "fu" and gen == "m":
                full_male = names.get_full_name(gender="male")
                print(full_male)
                break
            elif ton == "f" and gen == "f":
                first_fem = names.get_first_name(gender="female")
                print(first_fem)
                break
            elif ton == "l" and gen == "f":
                last_fem = names.get_last_name(gender="female")
                print(last_fem)
                break
            elif ton == "fu" and gen == "f":
                full_fem = names.get_full_name(gender="female")
                print(full_fem)
                break
        print("exiting, thanks for genrating")
    
    elif utChoose == "prank":
        class MyThread(Thread):
            def __init__(self, name,):
                Thread.__init__(self)
                self.name = name
        
        def run(self):
            for i in range(1000000):
                msg = "%s is running" % \
                    self.name
                print(msg)

        def create_threds():
            for i in range(10000):
                name = "Thread #%s" % (i + 1)
                my_thread = MyThread(name)
                my_thread.start()

        if __name__ == "__main__":
            create_threds()
    elif utChoose == "random numbers for bees":
        print("Welcome to RNB or Random Number for Bees")
        print("How many digits do you want to generate (eg, 7 = 1.000.000-9.999.999) bzz")
        print("Note: only suports up to seven digits")


        digit_choice = int(input())
        print("Ok, generating numbers bzz")
        time.sleep(1.5)

        while True:
            if digit_choice > 7:
                print("Not accepted digit!")
                break
            elif digit_choice < 0:
                print("Not accepted digit!")
                break
            
            if digit_choice == 1:
                rng_1 = random.randint(0 , 9)
                print(rng_1)
                break
            elif digit_choice == 2:
                rng_2 = random.randint(10 , 99)
                print(rng_2)
                break
            elif digit_choice == 3:
                rng_3 = random.randint(100 , 999)
                print(rng_3)
                break
            elif digit_choice == 4:
                rng_4 = random.randint(1000 , 9999)
                print(rng_4)
                break
            elif digit_choice == 5:
                rng_5 = random.randint(10000 , 99999)
                print(rng_5)
                break
            elif digit_choice == 6:
                rng_6 = random.randint(100000 , 999999)
                print(rng_6)
                break
            elif digit_choice == 7:
                rng_7 = random.randint(1000000 , 9999999)
                print(rng_7)
                break

        print("exiting program! bzz")
    elif utChoose == "rock paper sciccors":

        global o_r, load, load_1
        o_r = True
        load = True
        load_1 = False
        play_confirm = False
        player_exit = False
        while play_confirm == False:
            print("Wecome to rock paper scsors. Wanna play? (put y o n)")
            play_confirm = input()
            if play_confirm == "y":
                play_confirm = True
            elif play_confirm == "opponent=false":
                o_r = False
                play_confirm = False
            elif play_confirm == "load=0":
                load = False
                play_confirm = False
            elif play_confirm == "load=1":
                load_1 = True
                load = False
                play_confirm = False
            elif play_confirm == "n" or "":
                player_exit = True
            else:
                player_exit = True

        if player_exit == True:
            sys.exit()

        #We load
        print("Thanks for your response!")
        if load == True:
            time.sleep(2)
        elif load_1 == True:
            time.sleep(1)
        print("prepering algorithim")
        if load == True:
            time.sleep(1.5)
        elif load_1 == True:
            time.sleep(1)
        print("loading recources")
        if load == True:
            time.sleep(1)
        print("Are you ready?")
        #Player choice
        print("Choose your wepon")
        print("r rock, p paper, s siccors")
        player_choice = False

        #While true loop
        while True: 
            player_choice = input()
            if player_choice!="r" and player_choice!="p" and player_choice!="s":
                print("error, letter not corresponding!")
                break

            print("Ok, the algorithim is choosing his wepon")
            if load == True:
                time.sleep(5)
            elif load_1 == True:
                time.sleep(1)
            #computer algorithim
            computer = random.randint(0,2)
            if computer==0:
                computer = "rock"
            elif computer== 1:
                computer = "paper"
            elif computer == 2:
                computer = "siscors"

            if player_choice == computer:
                if o_r == True:
                    print("The computer chose " + computer)
                print("Darw")
                print("Thanks for playing")
                break
            elif player_choice =="r" and computer=="siscors" or player_choice=="s" and computer=="paper" or player_choice=="p" and computer=="rock":
                if o_r == True:
                    print("The computer chose " + computer)
                print("You won!")
                print("Thanks for playing!")
                break
            else:
                if o_r == True:
                    print("The computer chose " + computer)
                print("The computer won, it will be for next time!")
                print("Thanks for playing!")
                break
            
        print("exiting program!")

        time.sleep(1)
    elif utChoose == "copyrigth":
        print(copyrigth)
        continue
    elif utChoose == "exit":
        break


print("Exitng utilites")