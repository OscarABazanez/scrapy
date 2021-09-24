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
        driver.get('http://the-internet.herokuapp.com/dynamic_controls')
        driver.maximize_window()
        # driver.implicitly_wait(10)

    # find_element_by_xpath('//input[@type="checkbox"]')

    def test_addRemoveCheckBox(self):
        driver = self.driver

        # Conseguir los elemetos con selectores
        # check_box = driver.find_element_by_css_selector('#checkbox')
        # add_remove_button = driver.find_element_by_css_selector('#checkbox-example > button')

        # Conseguir los elemetos con Xpath
        check_box = driver.find_element_by_xpath('//input[@type="checkbox"]')
        add_remove_button = driver.find_element_by_xpath('//button[contains(text(),"Remove")]')

        #Interactuar con los elementos
        check_box.click()
        add_remove_button.click()

        # Conseguir los elemetos con selectores
        # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox')))

        # Conseguir los elemetos con Xpath
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Add")]')))
        
        add_remove_button.click()


    def test_write_in_input_field(self):
        driver = self.driver

        # Conseguir los elemetos con selectores
        # enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        # input_field = driver.find_element_by_css_selector('#input-example > input[type=text]')
        
        # Conseguir los elemetos con Xpath
        enable_disable_button = driver.find_element_by_xpath('//button[contains(text(),"Enable")]')
        input_field = driver.find_element_by_xpath('//form[@id="input-example"]//input[@type="text"]')

        

        #Interactuar con los elementos
        enable_disable_button.click()
        # Conseguir los elemetos con selectores
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))
        # Conseguir los elemetos con Xpath
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Disable")]')))
        input_field.clear() #En caso de que tenga texto escrito
        input_field.send_keys('Platzi')
        enable_disable_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='register-new-user-report'))