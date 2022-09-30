from selenium import webdriver


driver = webdriver.Chrome(executable_path='../../../Downloads/chromedriver')

driver.get("http://selenium.dev")

driver.quit()