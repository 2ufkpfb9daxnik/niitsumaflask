from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="./geckodriver") #ここのパスは I_Driveの適当な場所に変更することもできる
driver.get('https://www.google.com/')


time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('geckodriver')
search_box.submit()
time.sleep(5)
driver.quit()
