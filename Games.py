import os

while True:
    print(str("Avialable game: Snake Game"))

    user_query = input("Input your Game: ")

    if user_query == "Snake Game":
        os.startfile("snakegame.py")

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
    else:
        print(str("cannot find that game"))
        print("Type quit to quit")
