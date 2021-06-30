import os
while True:
    print("browser, main.os , file.editor, quit, am i smart or dumb, binary generator, Img Opener, Games")
    user_query = input(str("Choose Your Program: "))

    if user_query == "browser":
        os.startfile('browser.py')

    elif user_query == "am i smart or dumb":
        os.startfile('smart_Dumb.py')

    elif user_query == "main.os":
        os.startfile('main.py')

    elif user_query == "file.editor":
        os.startfile('file_editor.py')

    elif user_query == "binary generator":
        os.startfile('binary.py')

    elif user_query == "quit":
        print(str("where will you exit "
                  "'1' to quit to the main system"
                  "'2' close the system"))
        a = input(">>>")
        if a == "1":
            os.startfile('main.py')
            quit()
            break
        else:
            quit()
            break

    elif user_query == "Img Opener":
        os.startfile('imgopener.py')

    elif user_query == "Games":
        os.startfile("Games.py")
        quit()
        break

    else:
        input("That Programs Seems To Not Exist or isn't compatible")
