    



import sys
import os
import time
try:
    import pickle
    import requests
    import simpleaudio
    import shutil
except:
    if sys.platform == 'win32':
        os.system('pip install simpleaudio')
        os.system('pip install requests')
        os.system('pip install shutil')
        os.system('pip install pickle')
        import simpleaudio
        import requests
        import shutil
        import pickle
    elif sys.platform == 'linux':
        os.system('pip3 install simpleaudio')
        os.system('pip3 install requests')
        os.system('pip3 install shutil')
        os.system('pip3 install pickle')
        import simpleaudio
        import requests
        import shutil
        import pickle
    elif sys.platform == 'darwin':
        os.system('pip3 install simpleaudio')
        os.system('pip3 install requests')
        import simpleaudio
        import requests
        import shutil
        import pickle
    else:
        print('Unknown OS')
        exit()
import savelib

def setup():
    musictype = input("Would you like to stream music or download it? (s/d) (you need to install Git) ")
    if musictype == 's':
        print("Adding streamMusic value to settings.pkl...")
        savelib.add("true")
    elif musictype == 'd':
        print("Adding downloadMusic value to settings.pkl...")
        savelib.add("false")
        print("Fetching music from GitHub...")
        os.system('git clone -b music https://github.com/cobralang/bob-werld.git')
        os.rename("bob-werld", "music")
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


if disableMusic == True:
    print("Detected disableMusic variable, music will not play.")
else:
    if streamMusic == True:
        print("Music will be streamed.")
        os.system("git clone -b music https://github.com/cobralang/bob-werld.git")
        os.rename("bob-werld", "music")
        menu_theme = simpleaudio.WaveObject.from_wave_file("music/bob_world_menu_theme.wav")
        menyoo = simpleaudio.WaveObject.from_wave_file("music/menyoo.wav")
        jump = simpleaudio.WaveObject.from_wave_file("music/jump.wav")
        crash = simpleaudio.WaveObject.from_wave_file("music/crash.wav")
        buildnbreak = simpleaudio.WaveObject.from_wave_file("music/build-n-break.wav")
        bob = simpleaudio.WaveObject.from_wave_file("music/Bob.wav")
        shutil.rmtree("music")
    elif streamMusic == False:
        menu_theme = simpleaudio.WaveObject.from_wave_file("music/bob_world_menu_theme.wav")
        menyoo = simpleaudio.WaveObject.from_wave_file("music/menyoo.wav")
        jump = simpleaudio.WaveObject.from_wave_file("music/jump.wav")
        crash = simpleaudio.WaveObject.from_wave_file("music/crash.wav")
        buildnbreak = simpleaudio.WaveObject.from_wave_file("music/build-n-break.wav")
        bob = simpleaudio.WaveObject.from_wave_file("music/Bob.wav")



