import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import Select


class SelectLenguageTest(unittest.TestCase):

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



    def test_select_lenguage(self):
        exp_options = ['English', 'French', 'German']
        act_options = []
        # Accedemos las opciones del Select
        select_lenguage = Select(self.driver.find_element_by_xpath('//select[@id="select-language"]'))

        # Comprueba si las opciones tienen la mismas cantidad de opciones
        self.assertEqual(3,len(select_lenguage.options))
        for option in select_lenguage.options:
            act_options.append(option.text)

        # Verifica si contienen las mismas opciones
        self.assertListEqual(exp_options, act_options)

        # Vamos a verificar la palabra "English" sea la primera opción seleccionada del dropdown
        self.assertEqual('English', select_lenguage.first_selected_option.text)

        # Seleccionamos "German" por el texto visible
        select_lenguage.select_by_visible_text('German')

        # Verificamos que el sitio cambio a German
        # Preguntamos a selenium si la url del sitio contiene esas palabras
        self.assertTrue('store=german' in self.driver.current_url)

        # Accedemos las opciones y seleccionamos el indice 0
        select_lenguage = Select(self.driver.find_element_by_xpath('//select[@id="select-language"]'))
        select_lenguage.select_by_index(0)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='register-new-user-report'))