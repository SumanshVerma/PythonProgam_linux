import os
import subprocess
import getpass
import sys

def networkinfo():
    subprocess.call(["ifconfig"])

def diskusage():
    subprocess.call(["df"])

def makedir():
    directory_name = input("Enter the name of directory to be created : ")
    subprocess.call(["mkdir",directory_name])

def removedir():
    directory_name = input("Enter the name of directory to be removed : ")
    subprocess.call(["rmdir",directory_name])

def ramusage():
    subprocess.call(["free"])

def adduser():
    username = input("Enter User Name : ")
    password = getpass.getpass()
    subprocess.run(["useradd", '-p', password, username ])

def deleteuser():
    username = input("Enter User to delete : ")
    subprocess.call(["userdel",username])


def main():
    while True:
        key = input ("Enter Digits from (1-8) :\n 1. Network Information \n 2. DiskUsage \n 3. Make a new Directory \n 4. Delete a Directory \n 5. RAM Usage \n 6. Add a new user \n 7. Delete a user \n E to exit \n ")

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

        elif key == 'e': 
            print("Exiting program.")
            break
        else:
            print("Invalid key. Please press a number key from 1-8.")

if __name__ == "__main__":
    main()
