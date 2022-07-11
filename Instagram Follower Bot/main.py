from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os

Email = os.environ.get('Insta_Email')
Password = os.environ.get('Insta_Password')
SIMILAR_ACCOUNT = 'nina'  # account you want to become


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('E:\Chrome Driver\chromedriver.exe'))

    def login(self):
        self.driver.get(url='https://www.instagram.com/')
        time.sleep(3)

        email = self.driver.find_element(By.NAME, 'username')
        password = self.driver.find_element(By.NAME, 'password')

        email.send_keys(Email)
        password.send_keys(Password)
        password.send_keys(Keys.ENTER)
        time.sleep(7)

        save_info = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        save_info.click()
        time.sleep(3)

        turn_off_notifications = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        turn_off_notifications.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(3)

        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)

        bar = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')

        '''for _ in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', bar)
            time.sleep(2)'''
        bar.send_keys(Keys.PAGE_DOWN)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li button')

        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
