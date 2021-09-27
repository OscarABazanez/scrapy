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

class TyposTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
        driver = cls.driver
        driver.get('http://the-internet.herokuapp.com/typos')
        driver.maximize_window()
        # driver.implicitly_wait(10)


    def test_addRemoveCheckBox(self):
        driver = self.driver

        # Conseguir los elemetos con Xpath
        paragraph_to_check = driver.find_element_by_xpath('//div[@class="example"]/p[2]')
        text_to_check = paragraph_to_check.text
        print(text_to_check)
        
        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_xpath('//div[@class="example"]/p[2]')
            text_to_check = paragraph_to_check.text
            driver.refresh()

        while not found:
            if text_to_check == correct_text:
                tries +=1
                driver.refresh()
                found = True
        
        self.assertEqual(found, True)
        print(f"It took {tries} tries to find the typo")




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='register-new-user-report'))