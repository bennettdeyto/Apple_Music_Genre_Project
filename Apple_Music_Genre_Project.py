from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from tkinter import *
from tkinter import ttk
import time

#Initialization of Chrome Driver
PATH = "/Users/bennettdeyto/Desktop/Python Projects/Apple_Music_Genre_Project/Chrome_Driver/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://rateyourmusic.com")

#global variables
#prompts user to ask for album name and artist
album_name = input("Album Title: ")
artist_name = input("Album Artist's name: ")

genres = []


#checks if element exists within current opened HTML
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

#def input_album(event):
def input_album():
    search = driver.find_element(By.XPATH, "//*[@id='ui_search_input_main_search']")
    search.send_keys(album_name + " " + artist_name)
    search.send_keys(Keys.RETURN)

#navigates to & pulls genres into a list
#navigates to artist genres
#should be able to search for any album (MAKE SURE TO INCLUDE EPS AND SINGLES !!!! !!!  !!!!!)
def pull_genres():
    click_artist = driver.find_element(By.XPATH, "//*[@id='column_container_left']/div[1]/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody/tr/td[1]/b/a")
    click_artist.click()
    i = 0

    time.sleep(5)

    while True:
        
        #//*[@id="column_container_left"]/div/div[3]/div[2]/div[1]/div[8]/a[1]
        xpath = "//*[@id='column_container_left']/div/div[3]/div[2]/div[1]/div[8]/a["
        xpath += str(i + 1)
        xpath += "]"

        if not check_exists_by_xpath(xpath):  
            break
        print(i)
        print(xpath)

        genres.append(driver.find_element(By.XPATH, xpath).get_attribute("innerHTML"))
        i += 1
        

    for i in range(len(genres)):
        print(genres[i])
        



time.sleep(5)

input_album()

time.sleep(5)

pull_genres()

print(driver.title)
print(driver.current_url)

driver.quit()