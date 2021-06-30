from PIL import Image
import os

while True:
    img_name = input('Enter your img name: ')

    if img_name == "":
        print(str("Please Input the file Name"))
        print(str("Type 'quit()' to quit"))

    elif img_name == "quit()":
        os.startfile('programs.py')
        quit()
    try:
        img = Image.open(img_name)
        img.show()
        os.startfile('programs.py')
        quit()
    except FileNotFoundError:
        # img_name
        print("File Not Found")
# if img_name == "":
#     print(str("Please Input the file Name"))
#     print(str("Type 'quit()' to quit"))
# elif img_name == "quit()":
#     os.startfile('programs.py')
#     quit()
