import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_16(self): # Done
        self.driver.get('http://localhost:8000/registration.php')
        username = self.driver.find_element(By.NAME,"username")
        fname = self.driver.find_element(By.NAME,"firstname")
        lname = self.driver.find_element(By.NAME,"lastname")
        email = self.driver.find_element(By.NAME,"email")
        phone = self.driver.find_element(By.NAME,"phone")
        password = self.driver.find_element(By.NAME,"password")
        rpassword = self.driver.find_element(By.NAME,"cpassword")
        address = self.driver.find_element(By.NAME,"address")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("hoangnguyen")
        fname.send_keys("Hoang")
        lname.send_keys("Nguyen")
        email.send_keys("hoang123456@gmail.com")
        phone.send_keys("0979719586")
        password.send_keys("abcdef")
        rpassword.send_keys("abcdef")
        address.send_keys("")
        submitBtn.click()
        time.sleep(2) 
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "All fields must be Required!"
        
        
   
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()