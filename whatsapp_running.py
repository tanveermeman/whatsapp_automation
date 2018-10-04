from webwhatsapi import WhatsAPIDriver
import datetime
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import os

from selenium.webdriver.support.wait import WebDriverWait


class WhatsAppBot:
    def __init__(self):
        try:
            self.driver = WhatsAPIDriver(username="TANVEER")

            # self.driver = webdriver.Chrome()
        except:
            print('There was an error in loading the chrome driver.')
        #     try:
        #         self.driver = webdriver.Firefox()
        #
        #     except:
        #         print('There was an error in loading firefox driver.')
        #         try:
        #             self.driver = webdriver.Safari()
        #
        #         except:
        #             print('There was an error in loading Safari driver.')
        #
        # # self.driver = webdriver.Firefox()
        # self.driver.get("https://web.whatsapp.com/")
        # self.wait = WebDriverWait(self.driver, 600)

    def prepareContacts(self):
        print('prepare contacts called ')

        # self.target = ['tanu jio', 'myself', 'mujahid sir data science python', 'papa', 'bhaijan banglore']
        # self.target = []
        # csv_file = "./MohsinGroups23Sep.csv"
        # df = pd.read_csv(csv_file)
        # for name in df.First:
        #     self.target.append(str(name))

        # In future we will read from google contacts
        #         self.target = []
        #         csv_file = "./MohsinGroups23Sep.csv"		#instead of csv file
        #         df = pd.read_csv(csv_file)
        #         for name in df.First:
        #             self.target.append(str(name))

        # self.target = ['918830804832@c.us', '918971759065@c.us', '919673133084@c.us', '919226267595@c.us',
        #                '918329058624@c.us', '919021601089@c.us']
        self.target = ['918971759065@c.us']
        # ''918380810361-1516203429@g.us', '919881109889-1534153347@g.us', '919960187333-1534163293@g.us']
        # '918888577262-1515673500@g.us', '919028248548-1429982179@g.us', '918446132128-1432323294@g.us', '917776890404-1434522845@g.us', '918087711556-1462169945@g.us', '917057860121-1488042437@g.us', '919011958752-1391142156@g.us', '919764756456-1536510311@g.us', '918149741787-1529392536@g.us', '919096759569-1419861656@g.us', '919823772862-1469711670@g.us', '919021601089-1534311110@g.us', '919028248548-1534171088@g.us', '917709985919-1412448116@g.us', '919730728263-1496767975@g.us', '919168484010-1454573473@g.us', '917083673327-1530361404@g.us', '919175873692-1446218165@g.us', '918149885364-1484657309@g.us', '918805730333-1416678548@g.us', '919422350285-1531316811@g.us', '918552094386-1509970709@g.us', '919762129154-1431323680@g.us', '918698905550-1526741217@g.us', '919762918754-1506187240@g.us', '919028248548-1517305544@g.us', '919421061408-1503915938@g.us', '917020297922-1517429677@g.us', '918055437884-1394895478@g.us', '918087711556-1505931212@g.us', '919421061408-1440403160@g.us', '918087711556-1498749600@g.us', '918007979366-1495605975@g.us', '917030766889-1457106884@g.us', '918308641960-1484817962@g.us', '918087637977-1455534420@g.us', '919960544209-1443619369@g.us', '919923105491-1464248295@g.us', '919763650965-1440568028@g.us', '917709068468-1437115087@g.us', '918149705408-1421236717@g.us', '919028248548-1389637673@g.us']

    def send_message(self, string):
        for member in self.target:
            self.driver.send_message_to_id(member, string)

    #     x_arg = '//*[@id="side"]/div[2]/div/label/input'
    #     print(type (self.wait))
    #     group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    #
    #     for member in self.target:
    #         group_title.send_keys(member)
    #         print(member)
    #         group_title.send_keys(u'\ue007')
    #         print("group key send done")
    #         message = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    #         print("message is " + str(message))
    #         message.send_keys(string)
    #         print("send keys done: " + string)
    #         # sendbtn = '//*[@id="main"]/footer/div[1]/div[3]/button'
    #         sendbtn = '/html/body/div/div/div/div[3]/div/footer/div[1]/div[3]/button'
    #         sendbutton = self.wait.until(EC.presence_of_element_located((By.XPATH, sendbtn)))
    #         print("send button found" + str(sendbutton))
    #         sendbutton.click()
    #         print("button clicked")
    #     self.driver.close()

    def fetch_group_participants(self):
        print('fetch_group_participants called')
        participants_chat_ids = []
        participants = self.driver.group_get_participants_ids('919881109889-1534153347@g.us')
        print(participants)
        for members in participants:
            participants_chat_ids.append(participants[0]['_serialized'])
            # print(participants[0]['_serialized'])
            # print(type(participants))

        print(participants_chat_ids)
        print(len(participants_chat_ids))
        return participants_chat_ids # This is our target list which will have chat ids of all the participants in the group


# string = 'This is an automated test message please ignore it' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
# message_obj = open('message.txt', 'r')
# string = message_obj.read()
objWhatsAppBot = WhatsAppBot()
print('instance created of bot')
objWhatsAppBot.prepareContacts()
# objWhatsAppBot.send_message("{0}{1}".format(string, datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")))
# participants = objWhatsAppBot.driver.group_get_participants_ids('919881109889-1534153347@g.us')
# print(participants)
objWhatsAppBot.fetch_group_participants()

