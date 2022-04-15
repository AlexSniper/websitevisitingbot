from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
# Array of videos which will be played
videos = [
     'https://www.yourwebsiteishere.com',
     'https://www.yourwebsiteishere.com'
   
     
]


#for loop with numbers of time program will be played
for i in range(1000):
     # Printing number of time video already played
    print("Running the Video for {} time" .format(i))
    #Random sequence of Video
    random_video =random.randint(0, 7)
    #Choosing video in Random Sequence
    driver.get(videos[random_video])
    #Video Plays range first number from, second number too
    sleep_time = random.randint(10, 399)
    
    sleep(sleep_time)

driver.quit()



