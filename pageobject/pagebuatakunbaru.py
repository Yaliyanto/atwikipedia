from appium. webdriver.common.appiumby import AppiumBy
from locators.akunbaru_locator import AkunBaruLocator

class BuatAkunbarupage:

    def __init__(self,driver):
        self.driver = driver

    def input_nama_pengguna(self):    
        self.driver.find_element(AppiumBy.XPATH,AkunBaruLocator.input_nama_pengguna).send_keys("yamto")

    def input_kata_sandi(self):    
        self.driver.find_element(AppiumBy.XPATH,AkunBaruLocator.input_kata_sandi).send_keys("yamto")

    def input_ulangi_kata_sandi(self):    
        self.driver.find_element(AppiumBy.XPATH,AkunBaruLocator.input_ulangi_kata_sandi).send_keys("yamto")

    def input_surel(self):    
        self.driver.find_element(AppiumBy.XPATH,AkunBaruLocator.input_surel).send_keys("yamto")

    def click_button_selanjutnya(self):    
        self.driver.find_element(AppiumBy.ID,AkunBaruLocator.button_selanjutnya).click()

    def click_button_masuk_log_buat_akun_baru(self):    
        self.driver.find_element(AppiumBy.ID,AkunBaruLocator.button_masuk_log).click()