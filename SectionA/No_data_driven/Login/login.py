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

    def test_1(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()
        time.sleep(2)
        assert self.driver.current_url == 'http://localhost:8000/index.php'
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()
        

    def test_2(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("kien1111")
        password.send_keys("23134123")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"

    def test_3(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("23134123")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"


    def test_4(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"

    def test_5(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien1")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"


    def test_6(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        password.send_keys("123456")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"

    def test_7(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        password.send_keys("321321")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"


    def test_8(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"

    def test_9(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()
        time.sleep(2)
        assert self.driver.current_url == 'http://localhost:8000/index.php'
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()


    def test_10(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("abcdef")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"
        
    def test_11(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("testing12345")
        password.send_keys("abcdef")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"



    def test_12(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("")
        password.send_keys("abcdef")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"

    def test_13(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"



    def test_14(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()
        time.sleep(2)
        assert self.driver.current_url == 'http://localhost:8000/index.php'
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_15(self):
        self.driver.get('http://localhost:8000/login.php')
        # username = self.driver.find_element(By.NAME,"username")
        # password = self.driver.find_element(By.NAME,"password")
        # submitBtn = self.driver.find_element(By.NAME,"submit")
        signUpBtn = self.driver.find_element(By.XPATH,("/html/body/div[2]/div[3]/a"))
        signUpBtn.click()
        time.sleep(2)

        
    def test_16(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("abcdef")
        password.send_keys("123456")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/span[1]')
        assert errorNotification.text == "Invalid Username or Password!"
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()