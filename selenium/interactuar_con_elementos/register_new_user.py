import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class RegisterNewUserTest(unittest.TestCase):

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



    def test_new_user(self):
        self.driver.find_element_by_xpath('//div[@class="account-cart-wrapper"]//span[@class="label"]').click()
        self.driver.find_element_by_xpath('//div[@class="links"]//ul//li[@class=" last"]/a').click()

        create_account_button = self.driver.find_element_by_xpath('//a[@title="Create an Account"]//span//span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', self.driver.title)

        first_name = self.driver.find_element_by_id("firstname")
        middle_name = self.driver.find_element_by_id("middlename")
        last_name = self.driver.find_element_by_id("lastname")
        email_address = self.driver.find_element_by_id("email_address")
        news_letter_subscription = self.driver.find_element_by_id("is_subscribed")
        passwords = self.driver.find_element_by_id("password")
        confirm_passwords = self.driver.find_element_by_id("confirmation")
        submit_button = self.driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        # Validamos si los campons estan habilitados
        self.assertTrue(
            first_name.is_enabled() and
            middle_name.is_enabled() and
            last_name.is_enabled() and
            email_address.is_enabled() and
            news_letter_subscription.is_enabled() and
            passwords.is_enabled() and
            confirm_passwords.is_enabled() and
            submit_button.is_enabled()
        )
        
        # Completamos los campos e interactuamos
        first_name.send_keys('test')
        middle_name.send_keys('test')
        last_name.send_keys('test')
        email_address.send_keys('te312321st@dsadashotmail.com')
        news_letter_subscription.send_keys('test')
        passwords.send_keys('dsadsASDAS-sada3112312')
        confirm_passwords.send_keys('dsadsASDAS-sada3112312')
        submit_button.click()

        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='register-new-user-report'))