import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)
try:
	element = browser.find_element(By.ID,'input_value')
	x = element.text
	answer = calc(x)
	print(x)
	input_answer = browser.find_element(By.ID,'answer')
	input_answer.send_keys(answer)
	checkbox_element = browser.find_element(By.ID,'robotCheckbox')
	checkbox_element.click()
	#radio_btn_element = browser.find_element(By.CSS.SELECTOR, "[value='robots']")
	radio_btn_element = browser.find_element_by_css_selector("[value='robots']")
	radio_btn_element.click()
	
	submit_btn = browser.find_element(By.CLASS_NAME,'btn.btn-default')
	submit_btn.click()
	
	
	
	
except:
	time.sleep(5)
	print('Error')
	browser.quit()

finally:
	time.sleep(5)
	browser.quit()
	




