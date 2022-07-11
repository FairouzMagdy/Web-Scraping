from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

email = os.environ.get('Twitter_Email')
password = os.environ.get('Twitter_Password')
Promised_DOWN = 30
Internet_Provider = 'VodafoneEgypt'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('E:\Chrome Driver\chromedriver.exe'))
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(50)

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        time.sleep(4)

        log_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        log_in.click()
        time.sleep(3)

        username = self.driver.find_element(By.TAG_NAME, 'input')
        username.send_keys(email)
        username.send_keys(Keys.ENTER)
        time.sleep(3)

        Password = self.driver.find_element(By.NAME, 'password')
        Password.send_keys(password)
        Password.send_keys(Keys.ENTER)
        time.sleep(7)

        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey @{Internet_Provider} ,Why is my internet speed {self.down}down when I pay for {Promised_DOWN}down?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()


bot = InternetSpeedTwitterBot()

bot.tweet_at_provider()
