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
        driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
        driver.maximize_window()
        # driver.implicitly_wait(10)


    def test_add_remove(self):
        elements_added = int(input('How many elements will you add? '))
        elements_removed = int(input('How many elements will you remove? '))
        total_elements = elements_added - elements_removed

        add_button = self.driver.find_element_by_xpath('//div[@class="example"]//button[contains(text(),"Add Element")]')

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                # delete_button = self.driver.find_element_by_xpath('//div[@id="elements"]//button[@class="added-manually"]')
                delete_button = WebDriverWait(self.driver,2).until(EC.element_to_be_clickable((By.CLASS_NAME,'added-manually')))
                delete_button.click()
            except:
                print("You traying to delete more elements the the existen")
        
        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print(f"There are 0 elements on screen")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='register-new-user-report'))