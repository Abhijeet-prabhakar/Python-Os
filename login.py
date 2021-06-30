import os
import psutil
import shutil

print(str("Type 'Log' If You are a old user(not talking about the age)"))
print(str("Type 'Sign' If You are a new user(not talking about the age)"))
su = "Process Success"
while True:
    user_command = input(str(">>>"))
    if user_command == "Sign":
        # user_name = input("Set Your User Name: ")
        # user_pass = input("Set Your New Password "+user_name+": ")
        # os.write(username.txt,user_name)

        userlogin_name = input("Enter Your User Name: ")
        userlogin_password = input("Enter Your Password: ")

        with open('user_name.txt', 'w') as f:
            f.writelines(userlogin_name)

        with open('user_password.txt', 'w') as f:
            f.writelines(userlogin_password)

        print(su)
        print(str("now Log-In with the 'Log' command"))

    elif user_command == "Log":
        # a = input("enter user's password: ")

        userlogin_name = open('user_name.txt')
        userlogin_password = open('user_password.txt')

        u_p = userlogin_password.read()
        u_s = userlogin_name.read()

        a = input("enter "+u_s+"'s password: ")

        if a == u_p:
            os.startfile("main.py")
            break
            quit()
    elif user_command == "quit":
        break
        quit()
    else:
        print("type 'quit' to quit the setup")
