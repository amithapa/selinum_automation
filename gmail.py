from selenium import webdriver
import time
# Open the Google chrome browser and navigate to the page
driver = webdriver.Chrome()
driver.get("http://gmail.com")

#Username
username_element = driver.find_element_by_name("identifier")
username_element.send_keys("**************") 
email_next = driver.find_element_by_id("identifierNext")
email_next.click()
time.sleep(2)
password_elment = driver.find_element_by_name("password") 
password_elment.send_keys("*********")
password_next = driver.find_element_by_id("passwordNext")
password_next.click()
#driver.close()
