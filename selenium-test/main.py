from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

# instantiate options to be passed to chrome web driver
options = Options()
options.headless = False # setting this to true to avoid opening browser gui
options.add_argument("--window-size=1900,1200") # additional arguments 
options.add_argument("--auto-open-devtools-for-tabs");

# connect instance of Chrome webdriver
driver = webdriver.Chrome(options = options, executable_path = '../../../Downloads/chromedriver')

# driver will then navigate to the url
URL = "https://www.gymshark.com/collections/all-products/mens"
driver.get(URL)
# access the webpage html document
def display_page_source():
  assert driver.page_source, 'No results found'
  return driver.page_source
print('page source: ', display_page_source())
# access the website title
print('page title: ', driver.title)
# acces the current URL (could be useful in the case of redirects)
print('page current URL: ', driver.current_url)

#to add delay (useful for waiting for server/api loading)
time.sleep(3)

# using the find_element method to find elements. You can search by name, class, etc
# more details: https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
elem = driver.find_elements(By.ID, "product-schema")
for i in elem: 
  print(i.get_attribute('innerHTML'))

print('amount of items:', len(elem))

# now we can send keys (like entering keys on our keyboard)
# first we will clear any prepoluated text (just in case), then we will pass in the query we want, and then return it
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)

# exit the browser (could use close method to close the single tab that was open)
driver.quit()

