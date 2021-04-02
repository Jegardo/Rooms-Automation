import datetime
from selenium import webdriver
from roomsClass import *

now = datetime.datetime.now()

today = now.strftime('%A')
time = now.strftime('%H')
roomInput = ""
if str(17) > time > str(15) and today == "Friday":
    Rooms.connect('e5')
else:
    roomInput = input("Enter room:")
    Rooms.connect(roomInput)

