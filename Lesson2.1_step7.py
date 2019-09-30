import time
import math
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

treasure_value = browser.find_element_by_id('treasure').get_attribute('valuex')
value = calc(treasure_value)

input_answer = browser.find_element_by_id('answer').send_keys(value)

browser.find_element_by_id('robotCheckbox').click()

browser.find_element_by_css_selector("[value='robots']").click()
time.sleep(2)
browser.find_element_by_class_name('btn.btn-default').click()
time.sleep(5)
browser.quit()