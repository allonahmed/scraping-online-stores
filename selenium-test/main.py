from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# connect instance of Chrome webdriver
driver = webdriver.Chrome(executable_path='../../../Downloads/chromedriver')

# driver will then navigate to the url
URL = "http://www.python.org"
driver.get(URL)

# assertion to confirm the title of the web application
assert "Python" in driver.title

# using the find_element method to find elements. You can search by name, class, etc
# more details: https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
elem = driver.find_element(By.NAME, "q")

# now we can send keys (like entering keys on our keyboard)
# first we will clear any prepoluated text (just in case), then we will pass in the query we want, and then return it
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

#checks if we get any results
assert "No results found." not in driver.page_source

# exit the browser (could use close method to close the single tab that was open)
driver.quit()

