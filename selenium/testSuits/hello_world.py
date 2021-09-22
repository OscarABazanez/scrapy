import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HelloWorld(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    cls.driver.implicitly_wait(10)


  def test_hello_world(self):
    driver = self.driver
    driver.get('https://www.platzi.com')


  def test_visit_wikipedia(self):
    driver = self.driver
    driver.get('https://www.wikipedia.org')


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))