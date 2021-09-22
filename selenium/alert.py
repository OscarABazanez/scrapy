import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



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



    def test_compare_products_removal_alert(self):
	    driver = self.driver
	    search_field = driver.find_element_by_name('q')
	    #como buena práctica se recomienda limpiar los campos
	    search_field.clear()    
	    search_field.send_keys('tee')
	    search_field.submit()   
	    driver.find_element_by_class_name('link-compare').click()
	    driver.find_element_by_link_text('Clear All').click()
    
	    #creamos una variable para interactuar con el pop-up
	    alert = driver.switch_to_alert()
	    #vamos a extraer el texto que muestra
	    alert_text = alert.text 
	    #vamos a verificar el texto de la alerta
	    self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
		
	    alert.accept()
      
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='register-new-user-report'))