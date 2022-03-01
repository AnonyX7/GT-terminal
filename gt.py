import os
from time import *

def run():
    _command_ = input(">>> ")
    if _command_ == "rm":
        os.system ('cd storage/shared/android/data/com.rtsoft.growtopia/files && rm save.dat')
        print ("[✓] Successfully deleting save.dat from com.rtsoft.growtopia")
        run()
    elif _command_ == "run":
        os.system ('cd storage/shared/gt && cp save.dat ../android/data/com.rtsoft.growtopia/files')
        print ("[✓] Successfully added  save.dat to com.rtsoft.growtopia")
        print ("[S] Do you want to start Growtopia.apk? [Y/N]")
        _run_ = input(">>>")
        if _run_ == "y" or "Y":
            print ("Starting Growtopia...")
            os.system ('am start --user 0 -n com.rtsoft.growtopia/com.rtsoft.growtopia.Main')
            run()
        else:
            run()
    elif _command_ == "exit":
        print ("[S] Exiting Program...")
    else:
        print ("[!] Command Not Found")
        
        run()

os.system('clear')
print ("[S] GT terminal v.1.0")
run()
