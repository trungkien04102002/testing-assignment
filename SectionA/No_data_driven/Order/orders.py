import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class TestOrder(unittest.TestCase):
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

#Equivalent class partitioning technique
    def test_1(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')
        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        addToCartBtn = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn.click()

        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_2(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')
        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        quantityBtn = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn.clear()
        quantityBtn.send_keys("-1")

        addToCartBtn = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn.click()

        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/span')
        assert errorNotification.text == "Test case failed"
        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_3(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')
        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        quantityBtn = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn.clear()
        quantityBtn.send_keys("a")

        addToCartBtn = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn.click()

        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/span')
        assert errorNotification.text == "Test case failed"

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_4(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')
        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        quantityBtn = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn.clear()
        quantityBtn.send_keys("0")

        addToCartBtn = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn.click()

        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/span')
        assert errorNotification.text == "Test case failed"

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

# #Use case testing technique
    def test_5(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')
        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        # quantityBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]').clear()
        # quantityBtn1.send_keys("1")

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()

        # quantityBtn2 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[2]/div/div[2]/input[1]').clear()
        # quantityBtn2.send_keys("1")

        addToCartBtn2 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[2]/div/div[2]/input[2]')
        addToCartBtn2.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_6(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants1 = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[8]/div/div/a")
        restaurants1.click()

        retaurantPage = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[2]/a')
        retaurantPage.click()

        restaurants2 = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants2.click()

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()

        addToCartBtn2 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[2]/div/div[2]/input[2]')
        addToCartBtn2.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_7(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()

        deleteBtn = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div/div[1]/a/i')
        deleteBtn.click()

        addToCartBtn2 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[2]/div/div[2]/input[2]')
        addToCartBtn2.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_8(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()

        addToCartBtn2 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[2]/div/div[2]/input[2]')
        addToCartBtn2.click()
        
        deleteBtn = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div/div[1]/a/i')
        deleteBtn.click()

        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_9(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_10(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()
        
        deleteBtn = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div/div[1]/a/i')
        deleteBtn.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_11(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()
        
        quantityBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn1.clear()
        quantityBtn1.send_keys("-1")
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/span')
        assert errorNotification.text == "Test case failed"

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_12(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()
        
        quantityBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn1.clear()
        quantityBtn1.send_keys("0")
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/span')
        assert errorNotification.text == "Test case failed"

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_13(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()
        
        quantityBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn1.clear()
        quantityBtn1.send_keys("a")
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/span')
        assert errorNotification.text == "Test case failed"

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_14(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')
        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()

        addToCartBtn2 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[2]/div/div[2]/input[2]')
        addToCartBtn2.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

#Boundary value analysis technique
    def test_15(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()
        
        quantityBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn1.clear()
        quantityBtn1.send_keys("0")
        time.sleep(1)

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        errorNotification = self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/span')
        assert errorNotification.text == "Test case failed"

        time.sleep(1)

        assert self.driver.current_url == 'http://localhost:8000/index.php'
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_16(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()
        
        quantityBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn1.clear()
        quantityBtn1.send_keys("1")
        time.sleep(1)

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        assert self.driver.current_url == 'http://localhost:8000/index.php'
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_17(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()
        
        quantityBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn1.clear()
        quantityBtn1.send_keys("2")
        time.sleep(1)

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        assert self.driver.current_url == 'http://localhost:8000/index.php'
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()

    def test_18(self):
        self.driver.get('http://localhost:8000/login.php')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("trungkien")
        password.send_keys("123456")
        submitBtn.click()

        #restaurant page
        self.driver.get('http://localhost:8000/restaurants.php')

        restaurants = self.driver.find_element(By.XPATH,"/html/body/div/section/div/div/div[2]/div/div/div[2]/div/div/a")
        restaurants.click()
        
        quantityBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[1]')
        quantityBtn1.clear()
        quantityBtn1.send_keys("50")
        time.sleep(1)

        addToCartBtn1 = self.driver.find_element(By.XPATH,'//*[@id="popular2"]/div[1]/div/div[2]/input[2]')
        addToCartBtn1.click()
        
        checkOutBtn = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/div[3]/div/a")
        checkOutBtn.click()
        
        orderBtn= self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/form/div/div/div/div/div[2]/p/input")
        orderBtn.click()
        alert = self.driver.switch_to.alert

        #sleep for a second
        time.sleep(1)

        #accept the alert
        alert.accept()

        time.sleep(2)

        assert self.driver.current_url == 'http://localhost:8000/index.php'
        logoutBtn = self.driver.find_element(By.XPATH,'//*[@id="mainNavbarCollapse"]/ul/li[4]/a')
        logoutBtn.click()





if __name__ == '__main__':
    unittest.main()