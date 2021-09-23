import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#Herramienta para seleccionar elementos de la web con sus selectores
from selenium.webdriver.common.by import By

#Herramienta para hacer uso de las expected conditions y esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait

#Importar esperar explicitas
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

class CompareProductTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
        driver = cls.driver
        driver.get('http://the-internet.herokuapp.com/disappearing_elements')
        driver.maximize_window()
        # driver.implicitly_wait(10)


    def test_dynamic_elements(self):
        options = []
        # menu = 5 # Cantidad total de elementos del menu
        menu = 1 # Encontrar un elemento
        tries = 1

        while len(options) < 1: # Encontrar un elemento
        # while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    # Encontrar Gallery
                    options_name = self.driver.find_element_by_xpath('//ul//a[contains(text(),"Gallery")]')

                    # options_name = self.driver.find_element_by_xpath(f"//ul//li[{i+1}]//a")
                    options.append(options_name.text)
                    print(options)
                except:
                    print(f"Gallery is not found{options}")
                    tries +1
                    self.driver.refresh()

        print(f"Finished in {tries} tries")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='register-new-user-report'))