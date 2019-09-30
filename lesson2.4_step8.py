from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
from selenium import webdriver

import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
	WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
	
	button = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.ID,'book')))
	button.click()
	x_variable = browser.find_element_by_css_selector('#input_value')
	answer_text_field = browser.find_element_by_css_selector('#answer')
	submit_btn = browser.find_element_by_css_selector('[type="submit"]')

	# получаем переменную х
	x = int(x_variable.text)

	# решаем пример
	answer = log((abs(12*sin(x))))

	# вводим данные в поле ввода
	answer_text_field.send_keys(str(answer))

	# отправляем форму
	submit_btn.click()
	time.sleep(5)
	
except Exception as error:
	print(f'{error}')
finally:
	browser.quit()
	print('gff')

