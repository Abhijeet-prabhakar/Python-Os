# packages
# import webbrowser
import shutil
import random
import os
import smtplib
import psutil
import datetime
from PIL import Image
from datetime import time

# variables
battery = psutil.sensors_battery()
error1 = ":Command not found"
Thanks = "thanks for using me :), made by abhijeet prabhakar"
java1 = "java download"
python1 = "python download"
help1 = "type help! to see all commands"
duh1 = 'r'
exit1 = "press any key to close"
wifi = "This is not available"
user_name = open('user_name.txt')
u_n = user_name.read()
timee = "Good"
# main loop for functions

while True:

    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if hour > 12:
        timee = "Good Afternoon"
    elif hour < 12:
        timee = "Good Morning"
    elif hour < 18:
        timee = "Good Evening"
    else:
        timee = "Good Night"

    print("type 'help!' to see all commands :)")
    print(timee, u_n)
    command1 = input("add a command:")

    if command1 == "open browser":
        os.startfile('browser.py')
        # print("thanks for using me :), made by abhijeet prabhakar")

    elif command1 == 'help!':
        # print('commands: python download, java download, open browser, open browser youtube, open browser github')
        # print('open browser spotify, open browser stackoverflow, close, open browser java, open browser jdk')
        # print('gmail login, close, move file, download c#, download donut, download unity c#, open browser gmail')
        print("open browser, copy file, creator, who is your creator")
        print("choose random num, choose random number, read file, write file, open new file, delete file, rename file")
        print("mail a person, open new folder, delete folder, battery percent, random binary generator, os.info")
        print("create a new file, programs , file.editor, time, img-ope")
        input('press any key to end the program, ')

    elif command1 == "img-ope":
        os.startfile("imgopener.py")
        quit()

    elif command1 == "time":
        print(hour, "Hour", minute, "Minutes")
        print("this is a 24 hour clock")

    elif command1 == "file.editor":
        os.startfile("file_editor.py")

    elif command1 == "st-f":
        startfile1 = input("print the file name you want to start: ")
        os.startfile(startfile1)

    elif command1 == "os.info":
        oinfo = open('info.txt')
        info = oinfo.read()
        print(info)
        input(exit1)

    elif command1 == "programs":
        os.startfile('programs.py')
        quit()
        break

    elif command1 == "random binary generator":
        os.startfile('binary.py')

    elif command1 == "battery percent":
        print(battery.percent)

    elif command1 == "wifi":
        print(wifi)

    elif command1 == 'creator':
        print('Made by Abhijeet Prabhakar')
        input('press any key to exit')

    elif command1 == 'who is your creator':
        print('Made by Abhijeet Prabhakar')
        input('press any key to exit')

    # elif command1 == 'open browser youtube':
    #     webbrowser.open_new_tab('https://www.youtube.com')
    #     print("type help! to see all commands")
    #     print("thanks for using me :), made by abhijeet prabhakar")
    #
    # elif command1 == 'open browser github':
    #     webbrowser.open_new_tab('https://www.github.com')
    #     print("type help! to see all commands")
    #     print("thanks for using me :), made by abhijeet prabhakar")
    #
    # elif command1 == 'open browser stackoverflow':
    #     webbrowser.open_new_tab('https://www.stackoverflow.com')
    #     print("type help! to see all commands")
    #     print("thanks for using me :), made by abhijeet prabhakar")
    #
    # elif command1 == 'open browser fiverr':
    #     webbrowser.open_new_tab('https://www.fiverr.com')
    #     print("type help! to see all commands")
    #     print("thanks for using me :), made by abhijeet prabhakar")
    #
    # elif command1 == 'open browser itch':
    #     webbrowser.open_new_tab('https://www.itch.io')
    #     print("type help! to see all commands")
    #     print("thanks for using me :), made by abhijeet prabhakar")
    #
    # elif command1 == 'open browser blender':
    #     webbrowser.open_new_tab('https://www.blender.org')
    #     print("type help! to see all commands")
    #     print("thanks for using me :), made by abhijeet prabhakar")
    #
    # elif command1 == 'open browser python':
    #     webbrowser.open_new_tab('https://www.python.org')
    #     print("type help! to see all commands")
    #     print("thanks for using me :), made by abhijeet prabhakar")
    #
    # elif command1 == 'open browser jdk':
    #     webbrowser.open_new_tab('https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html')
    #     print("type help! to see all commands")
    #     print("thanks for using me :), made by abhijeet prabhakar")
    #
    # elif command1 == 'open browser java':
    #     webbrowser.open_new_tab('https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html')
    #     print("type help! to see all commands")
    #     print("thanks for using me :), made by abhijeet prabhakar")
    #
    # elif command1 == java1:
    #     webbrowser.open_new_tab('https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html')
    #     print("type help! to see all commands")
    #     print(Thanks)
    #
    # elif command1 == python1:
    #     webbrowser.open_new_tab('https://www.python.org')
    #     print("type help! to see all commands")
    #     print(Thanks)
    #
    # elif command1 == 'open browser spotify':
    #     webbrowser.open_new_tab('https://www.spotify.com')
    #     print(help1)
    #     print(Thanks)
    #
    # elif command1 == 'download c#':
    #     webbrowser.open_new_tab('https://dotnet.microsoft.com/download/dotnet-framework')
    #     print(help1)
    #     print(Thanks)
    #
    # elif command1 == 'download donut':
    #     webbrowser.open_new_tab('https://dotnet.microsoft.com/download/dotnet-framework')
    #     print(help1)
    #     print(Thanks)
    #
    # elif command1 == 'download unity c#':
    #     webbrowser.open_new_tab('https://dotnet.microsoft.com/download/dotnet-framework')
    #     print(help1)
    #     print(Thanks)
    #
    # elif command1 == 'open browser gmail':
    #     webbrowser.open_new_tab('https://mail.google.com')
    #     print(help1)
    #     print(Thanks)
    #
    # elif command1 == 'gmail login':
    #     webbrowser.open_new_tab('https://accounts.google.com/')
    #     print(help1)
    #     print(Thanks)

    elif command1 == "move file":
        origin1 = input('origin:')
        target1 = input('target:')
        shutil.move(origin1, target1)
        print(Thanks)
        print(help1)
        input('press any key to exit')

    elif command1 == "copy file":
        origin2 = input('origin:')
        target2 = input('target:')
        shutil.copy(origin2, target2)
        print(Thanks)
        print(help1)
        input('press any key to exit')

    elif command1 == "close":
        print(Thanks)


    elif command1 == "choose random num":
        print(random.randrange(1, 1000000))
        print("tadha i am good at maths boiiiii")
        # print(help1)
        print(Thanks)
        print(help1)
        input('press any key then enter to exit')

    elif command1 == "choose random number":
        random_num1 = input("add first number:")
        random_num2 = input("add second number:")
        random_num3 = input("add third number:")
        random_num4 = input("add fourth number:")
        random_num5 = input("add fifth number:")
        list = [random_num1, random_num2, random_num3, random_num4, random_num5]
        random_number = random.choice(list)
        print(random_number)
        print(Thanks)
        print(help1)
        input(exit1)

    elif command1 == "read file":
        try:
            readfile1 = input('input file name:')
            file = open(readfile1)
            if readfile1 == "user_name.txt":
                input("You cannot access that file")
                os.startfile('login.py')
                quit()
            if readfile1 == "user_password.txt":
                input("You cannot access that file")
                os.startfile('login.py')
                quit()
            print(file.read())
            input(exit1)
        except FileNotFoundError:
            print("sorry that file was not found:")


    elif command1 == "write file":
        writefile1 = input('input file name:')
        if writefile1 == "user_name.txt":
            print("You cannot access that file")
        if writefile1 == "user_password.txt":
            print("You cannot access that file")
        text2 = input('input what you wanna write in that file:')
        file = open(writefile1, "w")
        print(file.write(text2))
        input(exit1)

    elif command1 == "create a new file":
        createfile1 = input(str('Input your new file name: '))
        wtrst = input(str('do you want to write anything in it? If Not Just Press Enter And Leave It'))
        if createfile1 == "user_name.txt":
            print("invalid name")
        elif createfile1 == "user_password.txt":
            print("invalid name")
        file = open(createfile1, "w")
        print(file.write(wtrst))

        # if wtrst = "y":
        #     text3 = input("Write your text here: ")
        #     file = open(createfile1, "w")
        #     print(file.write(text3))

    # elif command1 == "open file":
    # openfile1 = input('input your file name')
    # file = open(openfile1,"w")
    # input(exit1)

    elif command1 == "open new file":
        opennewfile = input('input your new file name:')
        file = open(opennewfile, "w")

    elif command1 == "open new folder":
        print("please enter in where you want your folder to be for exaple D:\\New folder")
        opennewfolder = input("please enter the new folder path:")
        os.makedirs(opennewfolder)

    elif command1 == "delete folder":
        deletefolder = input("enter the folder path:")
        os.remove(deletefolder)
        print("process was successful")
        input(exit1)

    elif command1 == "rename folder":
        renamefolder = input("enter the old name of the folder:")
        renamefolder2 = input('enter the new folder name')
        os.rename(renamefolder, renamefolder2)
        print('process was success:)')
        input(exit1)

    elif command1 == "delete file":
        deletefile1 = input("enter the file path:")
        os.remove(deletefile1)
        print('process was success')
        input(exit1)

    elif command1 == "close":  # to close the program
        print("thanks for using me :), made by abhijeet prabhakar")
        quit()
        break

    elif command1 == "quit":
        print(Thanks)
        quit()
        break
    # D:\pythonterminalproject\Lib\main.py
    elif command1 == "rename file":
        oldfilename = input('enter the old file name:')
        newfilename = input('enter the new file name:')
        os.rename(oldfilename, newfilename)
        print('process was a success')
        input(exit1)

    elif command1 == "mail a person":
        # try
        sender_mail = input("add your email/add the sender email:")
        target_mail = input("add the email in which you will send the mail:")
        password = input(str("please enter your password:"))
        message = input("please input your message:")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, password)
        print("login success")
        server.sendmail(sender_mail, target_mail, message)
        print("the email was successfully send to", target_mail)
        input(exit1)
        exit()

    else:
        print("Please type a correct command/", command1, error1)
        print(Thanks)
        input('press any key to close')
