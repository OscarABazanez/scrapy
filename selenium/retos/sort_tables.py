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


class OrderTableTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
        driver = cls.driver
        driver.get('http://the-internet.herokuapp.com/tables')
        driver.maximize_window()
        # driver.implicitly_wait(10)


    def test_sort_table(self):
        driver = self.driver
        # Total elementos del header a capturar
        header_data_size = len(driver.find_elements_by_css_selector('#table1 > thead > tr > th')) -1

        # total elementos del body a capturar.
        body_data_size = len(driver.find_elements_by_css_selector('#table1 > tbody > tr'))

        # Se crea una lista de sublistas
        table_data = [[] for i in range(body_data_size)]

        # Se capturan los datos
        for i in range(body_data_size):
            for j in range(header_data_size):
                header_data = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{j+1}]/span').text

                cell_data = driver.find_element_by_xpath(f'//*[@id="table2"]/tbody/tr[{i+1}]/td[{j+1}]').text
                
                table_data[i].append({header_data : cell_data})

        print(table_data)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='register-new-user-report'))