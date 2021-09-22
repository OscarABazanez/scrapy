import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class HomePageTest(unittest.TestCase):

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



    def test_search_tee(self):
        search_field = self.driver.find_element_by_xpath('//input[@id="search"]')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

    
    def test_serch_salt_shaker(self):
        search_field = self.driver.find_element_by_xpath('//input[@id="search"]')
        search_field.send_keys('salt shaker')
        search_field.submit()
        
        products = self.driver.find_elements_by_xpath('//h2[@class="product-name"]//a')
        self.assertEqual(1, len(products))
        

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))