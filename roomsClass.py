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

        if str(room[0]).lower() == 'r':
            room_num = room[1]
        else:
            room_num = 8 + int(room[1])

        room_link = driver.find_element_by_xpath(f'/html/body/div/a[{room_num}]')

        if str(17) > cls.time > str(15) and cls.today == "Thursday":
            room_link.click()
        else:
            room_link.click()

            try:
                WebDriverWait(driver, 10).until(EC.alert_is_present(), "Waiting for alert timed out!")
                alert_obj = driver.switch_to.alert
                alert_obj.accept()
            except TimeoutException:
                print("Can't find the alert box!")

