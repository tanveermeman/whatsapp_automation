import datetime
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import os

from selenium.webdriver.support.wait import WebDriverWait


class whatsapp:
    def __init__(self):
        print('absdjfbs')
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")
        self.wait = WebDriverWait(self.driver, 600)

        # self.target = ['tanu jio', 'myself', 'mujahid sir data science python', 'papa', 'bhaijan banglore']
        self.target = []
        csv_file = "./MohsinGroups23Sep.csv"
        df = pd.read_csv(csv_file)
        for name in df.First:
            self.target.append(str(name))

    def send_message(self, string):
        x_arg = '//*[@id="side"]/div[2]/div/label/input'
        print(type (self.wait))
        group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))

        for member in self.target:
            group_title.send_keys(member)
            print(member)
            group_title.send_keys(u'\ue007')
            print("group key send done")
            message = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
            print("message is " + str(message))
            message.send_keys(string)
            print("send keys done: " + string)
            # sendbtn = '//*[@id="main"]/footer/div[1]/div[3]/button'
            sendbtn = '/html/body/div/div/div/div[3]/div/footer/div[1]/div[3]/button'
            sendbutton = self.wait.until(EC.presence_of_element_located((By.XPATH, sendbtn)))
            print("send button found" + str(sendbutton))
            sendbutton.click()
            print("button clicked")
        self.driver.close()


string = 'This is an automated test message please ignore it' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

message1 = whatsapp()
message1.send_message(string)

