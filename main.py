    


version = "0.0.1"

import sys
import os
os.system('clear')
try:
    import pickle
    import requests
    import simpleaudio
    import shutil
    import wget
    import random
except:
    if sys.platform == 'win32':
        os.system('pip instsall simpleaudio requests shutil pickle wget random')
        import simpleaudio
        import requests
        import shutil
        import pickle
        import wget
        import random
    elif sys.platform == 'linux':
        os.system('pip3 install simpleaudio requests shutil pickle wget random')
        import simpleaudio
        import requests
        import shutil
        import pickle
        import wget
        import random
    elif sys.platform == 'darwin':
        os.system('pip3 install simpleaudio requests shutil pickle wget random')
        import simpleaudio
        import requests
        import shutil
        import pickle
        import wget
        import random
    else:
        print('Unknown OS')
        exit()
import savelib

if requests.get("https://raw.githubusercontent.com/cobralang/bob-werld/main/main.py").status_code == 200:
    print("Connected to update server!")
    print("Checking for updates...")
    if requests.get("https://raw.githubusercontent.com/cobralang/bob-werld/main/main.py").text != open("main.py").read():
        print("Updating...")
        os.system('git pull')
        print("Done!")

def die():
    if disableMusic == False:
        bob.play()
    print("YOU DIED!")
    print("Press enter to continue...")
    input()
    exit()

def setup():
    musictype = input("Would you like to stream music or download it? (s/d) (you need to install Git) ")
    if musictype == 's':
        print("Adding streamMusic value to settings.pkl...")
        savelib.add("true")
    elif musictype == 'd':
        print("Adding downloadMusic value to settings.pkl...")
        savelib.add("false")
        print("Fetching music from GitHub...")
        os.makedirs('music', exist_ok=True)
        os.chdir('music')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/Bob.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/menyoo.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/jump.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/crash.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/build-n-break.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/bob_world_menu_theme.wav?raw=true')
        os.chdir('..')
    print("Done!")
    print("Saving settings.pkl...")
    savelib.save("settings.pkl")
    

try:
    open('settings.pkl', 'rb')
except:
    print('settings.pkl not found, assuming first run.')
    print("Creating settings.pkl...")
    open('settings.pkl', 'w+').close()
    print("Done.")
    setup()

print("Welcome to Bob Werld!")
print("NOTE: THIS IS BETA SOFTWARE. USE AT YOUR OWN RISK.")
print("DEV BUILD 5.2.9")
disableMusic = False
if savelib.loadslot(1, "settings.pkl") == 'true':
    print("Setting streamMusic variable to true")
    streamMusic = True
    if requests.get('https://example.com').status_code == 200:
        print("Internet connection established.")
    else:
        print("No internet connection detected. Music will not play.")
        streamMusic = False
        disableMusic = True

elif savelib.loadslot(1, "settings.pkl") == 'false':
    print("Setting streamMusic variable to false")
    streamMusic = False
else:
    print("Your settings.pkl is corrupted, please delete it and run the program again.")
    exit()


if disableMusic:
    print("Detected disableMusic variable, music will not play.")
else:
    if streamMusic:
        print("Music will be streamed.")
        os.makedirs('music', exist_ok=True)
        os.chdir('music')
        print("Fetching music from GitHub...")
        wget.download('https://github.com/cobralang/bob-werld/blob/music/Bob.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/menyoo.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/jump.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/crash.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/build-n-break.wav?raw=true')
        wget.download('https://github.com/cobralang/bob-werld/blob/music/bob_world_menu_theme.wav?raw=true')
        os.chdir('..')
        menu_theme = simpleaudio.WaveObject.from_wave_file("music/bob_world_menu_theme.wav")
        menyoo = simpleaudio.WaveObject.from_wave_file("music/menyoo.wav")
        jump = simpleaudio.WaveObject.from_wave_file("music/jump.wav")
        crash = simpleaudio.WaveObject.from_wave_file("music/crash.wav")
        buildnbreak = simpleaudio.WaveObject.from_wave_file("music/build-n-break.wav")
        bob = simpleaudio.WaveObject.from_wave_file("music/Bob.wav")
        shutil.rmtree("music")
    elif streamMusic is False:
        menu_theme = simpleaudio.WaveObject.from_wave_file("music/bob_world_menu_theme.wav")
        menyoo = simpleaudio.WaveObject.from_wave_file("music/menyoo.wav")
        jump = simpleaudio.WaveObject.from_wave_file("music/jump.wav")
        crash = simpleaudio.WaveObject.from_wave_file("music/crash.wav")
        buildnbreak = simpleaudio.WaveObject.from_wave_file("music/build-n-break.wav")
        bob = simpleaudio.WaveObject.from_wave_file("music/Bob.wav")

if disableMusic is False:
    playing_audio = menu_theme.play()
input("Press enter to start game...")
if disableMusic is False:
    playing_audio.stop()
    playing_audio = menyoo.play()
print("You awake in a strange place. You don't remember how you got here.")
print("You see a door to your left and a door to your right.")
print("Which one do you choose?")
print("1. Left")
print("2. Right")
if input() == "1":
    print("You walk into the door to your left.")
    print("You see a sign that says 'Bob's House'.")
    print("You walk up to the door and open it.")
    print("Suddenly, you hear a loud crash.")
    if disableMusic is False:
        playing_audio.stop()
        playing_audio = crash.play()
    print("A creature jumps out of the darkness.")
    print("It's a giant spider!")
    print("START OF CREATURE DIALOGUE")
    print("The spider says, 'Hello there! I'm Bob. I'm a giant spider.")
    print("Welcome to my land. This is bob werld, and I own it.")
    print("What is your name?'")
    username = input()
    print("Hello, " + username + "!")
    if input("What do you do? Run (1) or join bob? (2)") == "1":
        print("You hear bob yell, 'You're not going to run away from me, " + username + "! I'm going to eat you!'")
        print("Bob is faster than you. He catches up to you and eats you.")
        die()
    elif input() == "2":
        print("You join bob.")
        print("Bob and you walk into a dark room.")
        print("You see a door to your left and a door to your right.")
        print("Which one do you choose?")
        print("Bob reccomends the left door.")
        print("1. Left")
        print("2. Right")
        if input() == "1":
            print("You walk into the door to your left.")
        else:
            print("You walk into the room. It's dark.")
            print("The room flashes, and then you cease to exist.")
            die()
else:
    print("As soon as you touch the door, you die.")
    die()
