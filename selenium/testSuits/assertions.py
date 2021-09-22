import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)


    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))


    def test_language_option(self):
    	self.assertTrue(self.is_element_present(By.ID, 'select-language'))


    def tearDown(self):
    	self.driver.quit()


	#para saber si está presente el elemento
	#how: tipo de selector
	#what: el valor que tiene
    def	is_element_present(self, how, what):
    	try:  #busca los elementos según el parámetro
    		self.driver.find_element(by = how, value = what) 
    	except NoSuchElementException as variable:
    		return False
    	return True


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))