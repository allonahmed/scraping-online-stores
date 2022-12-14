from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.common.action_chains import ActionChains     
import time 



def gym_shark_scrape():
  # instantiate options to be passed to chrome web driver
  options = Options()
  options.headless = True # setting this to true to avoid opening browser gui
  options.add_argument("--window-size=1900,1200") # additional arguments 
  options.add_argument("--auto-open-devtools-for-tabs");

  # connect instance of Chrome webdriver
  driver = webdriver.Chrome(options = options, executable_path = '../../Downloads/chromedriver')

  # driver will then navigate to the url
  SITE_URL = "https://www.gymshark.com/collections/all-products/mens"

  driver.get(SITE_URL)

  # for adding action commands to driver
  actions = ActionChains(driver)

  # access the webpage html document
  def display_page_source():
    assert driver.page_source, 'No results found'
    return driver.page_source
  # using web driver wait to wait for when the popup becomes visible, then stores it
  iframe = WebDriverWait(driver, 60).until(ec.visibility_of_element_located(('xpath',
  '//*[@id="attentive_creative"]')))

  # needs to switch driver to frame to be able to acces the document information
  driver.switch_to.frame(iframe)

  # click the close popup button
  driver.find_element('xpath', '/html/body/div[2]/div/main/div/div/div/div[1]/div/form/div[2]/button[2]').click()
  print('closed popup')
  # switch back to our default driver
  driver.switch_to.default_content()

  # boolean that checks for a xpath's existence
  def does_element_exists(xpath):
    try:
      driver.find_element('xpath', xpath)
    except NoSuchElementException:
      return False
    return True

  # accessing load button so we can reach end of page before getting all of our data
  # and continously clicking it while it exists
  while(does_element_exists('//*[@id="portal-collection"]/section/button')):
    time.sleep(3)
    load_button = driver.find_element('xpath' ,'//*[@id="portal-collection"]/section/button')
    time.sleep(2)
    # scrolls to location of element
    driver.execute_script("arguments[0].scrollIntoView();", load_button)
    # clicks button
    load_button.click()
    
  # using the find_element method to find elements. You can search by name, class, etc
  # more details: https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
  elem = driver.find_elements(By.ID, "product-schema")
  results = []
  for i in elem: 
    # print(i.get_attribute('innerHTML'))
    results.append(i.get_attribute('innerHTML'))

  print('amount of items:', len(elem))
  driver.quit()

  return results



