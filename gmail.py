import argparse
from selenium import webdriver
import time


def authenticate(username, password):
	# Open the Google chrome browser and navigate to the page
	driver = webdriver.Chrome()
	driver.get("http://gmail.com")

	#Username
	username_element = driver.find_element_by_name("identifier")
	username_element.send_keys(username) 
	email_next = driver.find_element_by_id("identifierNext")
	email_next.click()
	time.sleep(2)
	password_elment = driver.find_element_by_name("password") 
	password_elment.send_keys(password)
	password_next = driver.find_element_by_id("passwordNext")
	time.sleep(2)
	password_next.click()
	time.sleep(200)
	#driver.close()

def setup_args():
	parser = argparse.ArgumentParser(description="Accepting username and password")
	parser.add_argument("--username", type=str, required=True, help="Gmail Username")
	parser.add_argument("--password", type=str, required=True, help="Gmail Password")
	
	return parser.parse_args()

def main():
	args = setup_args()
	#print(args)
	authenticate(args.username, args.password)

if __name__ == '__main__':
	main()
