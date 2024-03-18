from appium. webdriver.common.appiumby import AppiumBy
from locators.masuklog_locator import MasukLogLocator

class MasukLogPage:

    def __init__(self,driver):
        self.driver = driver

    def click_kolom_nama_pengguna(self):    
        self.driver.find_element(AppiumBy.XPATH,MasukLogLocator.input_nama_pengguna).click()

    def input_nama_pengguna(self):    
        self.driver.find_element(AppiumBy.XPATH,MasukLogLocator.input_nama_pengguna).send_keys("Yali Yanto")

    def click_kolom_kata_sandi(self):    
        self.driver.find_element(AppiumBy.XPATH,MasukLogLocator.input_kata_sandi).click()

    def input_kata_sandi(self):    
        self.driver.find_element(AppiumBy.XPATH,MasukLogLocator.input_kata_sandi).send_keys("kompor123")

    def click_button_masuk_log(self):    
        self.driver.find_element(AppiumBy.ID,MasukLogLocator.button_masuk_log).click()

    def validasi_judul(self):
        text = self.driver.find_element(AppiumBy.XPATH,MasukLogLocator.validasi_judul).text

        return text
    