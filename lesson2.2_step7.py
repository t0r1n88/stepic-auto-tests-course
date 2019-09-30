import math
import os
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:

	browser.find_element_by_name('firstname').send_keys('Oleg')
	browser.find_element_by_name('lastname').send_keys('Budaev')
	browser.find_element_by_name('email').send_keys('t0r1n88@mail.ru')
	
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir,'test.txt')
	
	browser.find_element_by_css_selector("[type='file']").send_keys(file_path)
	browser.find_element_by_class_name('btn.btn-primary').click()
	time.sleep(5)
except Exception as error:
		print(f'Произошла ошибка {error}')

finally:
	browser.quit()


