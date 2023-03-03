from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = r"https://jobs.homesteadstudio.co/data-engineer/assessment/download/"

#options to keep webdriver open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #keep window open

#initialize webdriver
driver = webdriver.Chrome(options = options)
driver.get(link)

#locate the download link and download it
download_button = driver.find_element(By.CLASS_NAME, "wp-block-button")
time.sleep(3)

download_button.click()
time.sleep(5) #time provided to chrome in finishing download

#close webdriver
driver.quit()

print("Download completed!")