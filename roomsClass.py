from selenium import webdriver
from selenium.webdriver import opera
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import time

class Rooms:
    now = datetime.datetime.now()

    today = now.strftime('%A')
    time = now.strftime('%H')

    @classmethod
    def connect(cls, room):
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

        if str(17) > cls.time > str(15) and cls.today == "Thursday":
            E5.click()
        else:
            if room == "R1" or room == "r1":
                R1.click()
            elif room == "R2" or room == "r2":
                R2.click()
            elif room == "R3" or room == "r3":
                R3.click()
            elif room == "R4" or room == "r4":
                R4.click()
            elif room == "R5" or room == "r5":
                R5.click()
            elif room == "R6" or room == "r6":
                R6.click()
            elif room == "R7" or room == "r7":
                R7.click()
            elif room == "R8" or room == "r8":
                R8.click()
            elif room == "E1" or room == "e1":
                E1.click()
            elif room == "E2" or room == "e2":
                E2.click()
            elif room == "E3" or room == "e3":
                E3.click()
            elif room == "E4" or room == "e4":
                E4.click()
            elif room == "E5" or room == "e5":
                E5.click()
            elif room == "E6" or room == "e6":
                E6.click()
            elif room == "E7" or room == "e7":
                E7.click()
            elif room == "E8" or room == "e8":
                E8.click()

            try:
                WebDriverWait(driver, 10).until(EC.alert_is_present(), "Waiting for alert timed out!")
                alert_obj = driver.switch_to.alert
                alert_obj.accept()
            except TimeoutException:
                print("Can't find the alert box!")

