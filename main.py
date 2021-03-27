import datetime
from selenium import webdriver

now = datetime.datetime.now()

today = now.strftime('%A')
time = now.strftime('%H')
roomInput = ""
if str(17) > time > str(15) and today == "Thursday":
    pass
else:
    roomInput = input("Enter room:")

driver = webdriver.Chrome()

driver.get('https://rooms.iee.ihu.gr/')


R1 = driver.find_element_by_xpath('/html/body/div/a[1]')
R2 = driver.find_element_by_xpath('/html/body/div/a[2]')
R3 = driver.find_element_by_xpath('/html/body/div/a[3]')
R4 = driver.find_element_by_xpath('/html/body/div/a[4]')
R5 = driver.find_element_by_xpath('/html/body/div/a[5]')
R6 = driver.find_element_by_xpath('/html/body/div/a[6]')
R7 = driver.find_element_by_xpath('/html/body/div/a[7]')
R8 = driver.find_element_by_xpath('/html/body/div/a[8]')

E1 = driver.find_element_by_xpath('/html/body/div/a[9]')
E2 = driver.find_element_by_xpath('/html/body/div/a[10]')
E3 = driver.find_element_by_xpath('/html/body/div/a[11]')
E4 = driver.find_element_by_xpath('/html/body/div/a[12]')
E5 = driver.find_element_by_xpath('/html/body/div/a[13]')
E6 = driver.find_element_by_xpath('/html/body/div/a[14]')
E7 = driver.find_element_by_xpath('/html/body/div/a[15]')
E8 = driver.find_element_by_xpath('/html/body/div/a[16]')

if str(17) > time > str(15) and today == "Thursday":
    E5.click()
else:
    if roomInput == "R1" or roomInput == "r1":
        R1.click()
    elif roomInput == "R2" or roomInput == "r2":
        R2.click()
    elif roomInput == "R3" or roomInput == "r3":
        R3.click()
    elif roomInput == "R4" or roomInput == "r4":
        R4.click()
    elif roomInput == "R5" or roomInput == "r5":
        R5.click()
    elif roomInput == "R6" or roomInput == "r6":
        R6.click()
    elif roomInput == "R7" or roomInput == "r7":
        R7.click()
    elif roomInput == "R8" or roomInput == "r8":
        R8.click()
    elif roomInput == "E1" or roomInput == "e1":
        E1.click()
    elif roomInput == "E2" or roomInput == "e2":
        E2.click()
    elif roomInput == "E3" or roomInput == "e3":
        E3.click()
    elif roomInput == "E4" or roomInput == "e4":
        E4.click()
    elif roomInput == "E5" or roomInput == "e5":
        E5.click()
    elif roomInput == "E6" or roomInput == "e6":
        E6.click()
    elif roomInput == "E7" or roomInput == "e7":
        E7.click()
    elif roomInput == "E8" or roomInput == "e8":
        E8.click()
