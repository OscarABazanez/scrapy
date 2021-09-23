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


class CompareProductTest(unittest.TestCase):

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
        # driver.implicitly_wait(10)

    
    def test_account_link(self): #Cuentas del sitio

        #Esperar 10 segundos hasta que se cumpla la funcion
        WebDriverWait(self.driver, 3).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        #Hacer referencia al enlace donde estan las cuentas
        account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()


    def test_create_new_customer(self): #Creacion de nuevo usuario

        #Encontrar el elemento por el texto del enlace
        self.driver.find_element_by_link_text('ACCOUNT').click()

        #Hacer referencia a la cuenta
        my_account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        #Referencia a crear una cuenta
        create_account = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account.click()

        #Verificacion de estado de pagina web
        WebDriverWait(self.driver, 3).until(EC.title_contains('Create New Customer Account'))



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='register-new-user-report'))