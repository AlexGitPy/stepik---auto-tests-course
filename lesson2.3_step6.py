from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button1 = browser.find_element_by_tag_name("button")
	button1.click()
	time.sleep(1)
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	answer = browser.find_element_by_id("answer")
	answer.send_keys(y)
	button2 = browser.find_element_by_tag_name("button")
	button2.click()

finally:
	time.sleep(10)
	browser.quit()