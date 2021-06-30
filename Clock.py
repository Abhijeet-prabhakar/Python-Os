# import datetime
# import os
# from datetime import time
# from psutil import *
#
#
# while True:
#     hour = int(datetime.datetime.now().hour)
#     minute = int(datetime.datetime.now().minute)
#
#     print(hour, minute)
#
#     print(str("want a change time?"))
#     a = input("Add Your Time Here->>> ")
#     if a == "":
#         try:
#             b = input(int("please add your our here: "))
#             c = input(int("Please add the minutes here: "))
#
#             with open('user_time_hour.txt', 'w') as f:
#                 f.writelines(b)
#
#             with open('user_time_min.txt', 'w') as f:
#                 f.writelines(c)
#         except ValueError:
#             print("There is an error")
#     else:
#         print("Sorry something went wrong")
#
#     hour_user_time_open = open('user_time_hour.txt')
#     minute_user_time_open = open('user_time_min.txt')
#
#     hour_user_time_read = hour_user_time_open.read()
#     minute_user_time_read = minute_user_time_open.read()
#
#     user_time_min = int(minute_user_time_read)
#     user_time_hour = int(hour_user_time_read)
#
#     if user_time_min > 0:
#         var = user_time_min + 1
#     elif user_time_min > 60:
#         user_time_min = 0
#
# while False:
#     print("hello")
