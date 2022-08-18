import time
from datetime import date
import os
from sys import platform

# Whoami
name = "Xatt"
print("Welcome to my Website.")
time.sleep(0.2)

def age(birthdate):  # Calculating age
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Defining age
cage = age(date(2001, 10, 12))
print(f"My name is {name}. I\'m {cage} years old.")
time.sleep(1)

# Education section
accomplishments = "College"
time.sleep(1)
if accomplishments == "College":
    print("At the moment I am studying for System Administrator.")
    time.sleep(1)
    print("After I finish College I\'d like to enroll into a Cyber-Security Bachlor degree.")

elif accomplishments == "Bachlor":
    print("At the moment I am doing a Bachlor in Cyber-Security.")

elif accomplishments == "Redo":
    print("At the moment I am redoing my exams to finish College.")

else:
    print("Please contact me for this error,\nme@xatt.dev")
time.sleep(1)

# Getting to know more about me.
print("But you\'d probably want to know more about what I do in my free time?")
vul = input("Choose: \"Y\" or \"N\" \n")
if vul.lower() == "y":
    print("Cool,")
    time.sleep(0.5)
    print("I like to learn new stuff in my free-time, like C, Python, SQL, CTF\'s ect.")

elif vul.lower() == "n":
    print("Sorry to see you go.")
    exit()

else:
    print("You didn\'t follow the instructions.")
    exit()

# Sharing github.
time.sleep(1)
print("I have created a couple of GitHub repositories.")
time.sleep(0.8)
print("This is the place where I like to share my creations.")
time.sleep(1)
print("Would you like to take a look at this?")
github = input("Choose: \"Y\" or \"N\" \n")
if github.lower() == "y":
    if platform == "linux":
        os.system('firefox https://github.com/maliciousxatt')
        print("Opening Firefox: https://github.com/maliciousxatt")
        print("30 Seconds before continueing.")
        time.sleep(30)

    elif platform == "darwin":
        os.system('safari https://github.com/maliciousxatt')
        print("Opening Safari: https://github.com/maliciousxatt")
        print("30 Seconds before continueing.")
        time.sleep(30)

    elif platform == "win32":
        os.system('msedge.exe https://github.com/maliciousxatt')
        print("Opening Edge: https://github.com/maliciousxatt")
        print("30 Seconds before continueing.")
        time.sleep(30)

    else:
        print("Failed to detect OS.")
        print("Go to https://github.com/maliciousxatt")

    print("Hopefully you found something interesting to contribute to or use.")

else:
    print("That\'s fine, take a look when you want.")

# Continueing
time.sleep(1)
print("And what to totally not forget, is that I am a Full-Time Linux user.")
time.sleep(1)
print("I\'ve been switching distros, and used: Debian, Arch and at the moment on Fedora.")
time.sleep(1)
print("I am not thinking of ever going back to Windows on my machines.")
time.sleep(3)
print("As you noticed, I am a fully dedicated IT\'er.")
time.sleep(2)

# Shooting my shot.
work = "yes"
which = "internship"
if work == "yes":
    print("Do you work in Cyber-Security?")
    cyberwork = input("Choose: \"Y\" or \"N\" \n")
    if cyberwork.lower() == "y":
        print(f"At the moment I\'m looking for a {which}.")
        time.sleep(1)
        print("I would like to know what company you work for and what it\'s functions are.")
        time.sleep(1)
        print("I am sure that I\'d be a great fit in the company!")
        time.sleep(1)
        print("Please e-mail me at:\nme@xatt.dev\n")

    elif cyberwork.lower() == "n":
        print("Okay! If you know anyone in Cyber-Security, please share my website!")

    else:
        print("Wrong input.")

# The End is coming
print("I enjoy creating a future in my hobby.")
time.sleep(1)
print("That was it! thank you for following along my introduction.")  # The End.
time.sleep(1)
print("Enjoy my website! https://xatt.dev/ and https://blog.xatt.dev/")
