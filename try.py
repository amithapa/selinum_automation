from selenium import webdriver
# Open the Google chrome browser and navigate to the page
driver = webdriver.Chrome()
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# Extract lists of buyers and prices based on xpath
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# Print Out all of the buyers and prices on current Page.
num_page_items = len(buyers), len(prices)

for buyers_obj, prices_obj in zip(buyers, prices):
	print(f"{buyers_obj.text} :  {prices_obj.text}")
	
driver.close()
