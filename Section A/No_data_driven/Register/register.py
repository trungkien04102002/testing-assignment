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
    
    def test_1(self): # done
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
        username.send_keys("kiendeptrai0410")
        fname.send_keys("Kien")
        lname.send_keys("Trung")
        email.send_keys("kien123456@gmail.com")
        phone.send_keys("0979719585")
        password.send_keys("Kien1234")
        rpassword.send_keys("Kien1234")
        address.send_keys("Viet Nam")
        submitBtn.click()
        time.sleep(6)
        assert self.driver.current_url == 'http://localhost:8000/login.php'
        createAccountBtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/a')
        createAccountBtn.click()
    
    def test_2(self): # done
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
        username.send_keys("hatrungkien")
        fname.send_keys("Kien")
        lname.send_keys("Trung")
        email.send_keys("kien")
        phone.send_keys("0979719585")
        password.send_keys("Kien1234")
        rpassword.send_keys("Kien1234")
        address.send_keys("Viet Nam")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "Invalid email address please type a valid email!"
    def test_3(self): # done
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
        username.send_keys("trungkien")
        fname.send_keys("Kien")
        lname.send_keys("Trung")
        email.send_keys("ns949405@gmail.com")
        phone.send_keys("0979719585")
        password.send_keys("Kien1234")
        rpassword.send_keys("Kien1234")
        address.send_keys("Viet Nam")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "Email Already exists!"    
    def test_4(self): # Done
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
        username.send_keys("hatrungkien1")
        fname.send_keys("Kien")
        lname.send_keys("Trung")
        email.send_keys("")
        phone.send_keys("0979719585")
        password.send_keys("Kien1234")
        rpassword.send_keys("Kien1234")
        address.send_keys("VietNam")
        submitBtn.click()
        time.sleep(2) 
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "All fields must be Required!"  
    def test_5(self): # Done
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
        username.send_keys("navjot789")
        fname.send_keys("Taylor")
        lname.send_keys("Switf")
        email.send_keys("iamsad@gmail.com")
        phone.send_keys("0979719585")
        password.send_keys("123456")
        rpassword.send_keys("123456")
        address.send_keys("KTX Khu A")
        submitBtn.click()
        time.sleep(2) 
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "username Already exists!"    

    def test_6(self): # Done
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
        username.send_keys("")
        fname.send_keys("Taylor")
        lname.send_keys("Swift")
        email.send_keys("iamsad@gmail.com")
        phone.send_keys("0979719585")
        password.send_keys("123456")
        rpassword.send_keys("123456")
        address.send_keys("KTX Khu A")
        submitBtn.click()
        time.sleep(2) 
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "All fields must be Required!"  

    def test_7(self): # Done
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
        username.send_keys("luongdat")
        fname.send_keys("")
        lname.send_keys("Swift")
        email.send_keys("iamsad@gmail.com")
        phone.send_keys("0979719585")
        password.send_keys("123456")
        rpassword.send_keys("123456")
        address.send_keys("KTX Khu A")
        submitBtn.click()
        time.sleep(2) 
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "All fields must be Required!"   

    def test_8(self): # Done
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
        username.send_keys("thienphu1")
        fname.send_keys("Thien")
        lname.send_keys("")
        email.send_keys("kien1234567@gmail.com")
        phone.send_keys("0979719585")
        password.send_keys("Kien1234")
        rpassword.send_keys("Kien1234")
        address.send_keys("Viet Nam")
        submitBtn.click()
        time.sleep(2) 
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "All fields must be Required!"    

    def test_9(self): # Done
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
        username.send_keys("thienphu1")
        fname.send_keys("Thien")
        lname.send_keys("Phu")
        email.send_keys("kien1234567@gmail.com")
        phone.send_keys("")
        password.send_keys("Kien1234")
        rpassword.send_keys("Kien1234")
        address.send_keys("Viet Nam")
        submitBtn.click()
        time.sleep(2) 
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "All fields must be Required!"    

    
    def test_10(self): # Done
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
        username.send_keys("thienphu1")
        fname.send_keys("Thien")
        lname.send_keys("Phu")
        email.send_keys("kien1234567@gmail.com")
        phone.send_keys("0979719")
        password.send_keys("Kien1234")
        rpassword.send_keys("Kien1234")
        address.send_keys("Viet Nam")
        submitBtn.click()
        time.sleep(2) 
        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div/ul/li/a/span[1]')
        assert errorNotification.text == "invalid phone number!"    
        
        
   
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()