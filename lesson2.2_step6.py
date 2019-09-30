from math import log, sin
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
	return log(abs(12*sin(x)))
try:
	value = browser.find_element_by_id('input_value').text
	print(value)
	output_value = calc(int(value))
	
	button = browser.find_element_by_tag_name("button")
	browser.execute_script("window.scrollBy(0, 120);")
	
	browser.find_element_by_id('answer').send_keys(str(output_value))
	browser.find_element_by_id('robotCheckbox').click()
	browser.find_element_by_css_selector("[for='robotsRule']").click()
	button.click()
	time.sleep(5)
		
except Exception as error:
	print(f'Произошла ошибка. Омниссия недоволен тобой, вот его послание{error}')
	

finally:
	browser.quit()

