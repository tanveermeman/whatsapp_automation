from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import datetime

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

#target= ['tanu jio', 'jio home', 'myself', 'papa', 'omkar trinity','bhaijan banglore']
target = []
csv_file="./MohsinGroups23Sep.csv"
df = pd.read_csv(csv_file)
for name in df.First:
	target.append(str(name))

# string ="Assalam alaikum Time is: "+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
string = 'This is an automated test message please ignore it'

x_arg='//*[@id="side"]/div[2]/div/label/input'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
for member in target:
    group_title.send_keys(member)
    print(member)
    group_title.send_keys(u'\ue007')
    print("group key send done")
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    print("message is "+str(message))
    message.send_keys(string)
    print("send keys done: "+string)
    sendbtn='//*[@id="main"]/footer/div[1]/div[3]/button'
    sendbutton = wait.until(EC.presence_of_element_located((By.XPATH,sendbtn)))
    print("send button found"+str(sendbutton))
    sendbutton.click()
    print("button clicked")
driver.close()
