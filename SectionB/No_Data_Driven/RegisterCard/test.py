import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select



class TestRegisterWithDraw(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://mybk.hcmut.edu.vn/my/logoutSSO.action")
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")  
        submitBtn = self.driver.find_element(By.NAME,"submit")  
        #----Submit---#
        username.send_keys("huy.dangquang")
        password.send_keys("0854001109")
        submitBtn.click()

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    
    def test_12(self): #done fali
        self.driver.get('https://mybk.hcmut.edu.vn/app')
        self.driver.get('https://mybk.hcmut.edu.vn/app/sinh-vien/in-the-sinh-vien/dang-ky')
        selectAdd = self.driver.find_element(By.ID,'select2-cboNoiNhan-container')
        selectAdd.click()
        addSelect = self.driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li[1]')
        addSelect.click()
        time.sleep(1)
        receiver = self.driver.find_element(By.ID,'txtTenNguoiNhan')
        receiver.send_keys('Đặng Quang Huy')
        time.sleep(1)
        numberphone = self.driver.find_element(By.ID,'txtSoDienThoai')
        numberphone.send_keys('05338616018')
        time.sleep(1)
        address = self.driver.find_element(By.ID,'txtDiaChi')
        address.send_keys('12 Nguyên Thị Lý, khu phố 1')
        time.sleep(1)
        valiate = self.driver.find_element(By.XPATH,'//*[@id="chkCamKet"]')
        valiate.click()
        submitbtn = self.driver.find_element(By.XPATH,'//*[@id="btnDangKy"]')
        submitbtn.click()
        time.sleep(1)
        resubmit = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/button[1]')
        resubmit.click()
        time.sleep(1)
        annoucetext = self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')
        assert annoucetext.text=="Số điện thoại không được xác thực"
   
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()