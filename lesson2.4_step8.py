from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    ) 
	button1 = browser.find_element_by_id("book")
	button1.click()
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	answer = browser.find_element_by_id("answer")
	answer.send_keys(y)
	button2 = browser.find_element_by_id("solve")
	button2.click()

finally:
	time.sleep(10)
	browser.quit()