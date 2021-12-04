    



import sys
import os
try:
    import playsound
    import pickle
except:
    if sys.platform == 'win32':
        os.system('pip install playsound')
        os.system('pip install pickle')
        import playsound
        import pickle
    elif sys.platform == 'linux':
        os.system('pip3 install playsound')
        os.system('pip3 install pickle')
        import playsound
        import pickle
    elif sys.platform == 'darwin':
        os.system('pip3 install playsound')
        os.system('pip3 install pickle')
        import playsound
        import pickle
    else:
        print('Unknown OS')
        exit()
import savelib

def setup():
    musictype = input("Would you like to stream music or download it? (s/d) (for download you need to install Git)")
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


