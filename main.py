import os
import subprocess



def networkinfo():
    subprocess.call(["ifconfig"])

def diskusage():
    subprocess.call(["df"])

def makedir():
    subprocess.call(["mkdir","testsumansh"])

def removedir():
    subprocess.call(["rm","testsumansh"])

def ramusage():
    subprocess.call(["top"])

def adduser():
    username = input("Enter Directory Name")
    subprocess.call(["Sudo","useradd",username])

def deleteuser():
    Deletedir = input("Enter directory to delete")
    subprocess.call(["userdel",Deletedir])


def main():
    while True:
        key = input("Press a number key (1-8): ")
        if key == '1':
            networkinfo()
        
        elif key == '2':
            diskusage()

        elif key =='3':
             makedir()
        
        elif key =='4':
            removedir()     

        elif key =='5':
            ramusage()

        elif key =='6':
            adduser()
        
        elif key =='7':
            deleteuser()
            
        elif key == 'e':  # If you want to quit on 'q'
            print("Exiting program.")
            break
        else:
            print("Invalid key. Please press a number key from 1-8.")

if __name__ == "__main__":
    main()
