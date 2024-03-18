from appium. webdriver.common.appiumby import AppiumBy
from locators.navbar_locator import NavbarLocator

class NavbarButton:

    def __init__(self,driver):
        self.driver = driver

    def click_button_jelajahi(self):    
        self.driver.find_element(AppiumBy.ID,NavbarLocator.button_jelajahi).click()

    def click_button_tersimpan(self):    
        self.driver.find_element(AppiumBy.ID,NavbarLocator.button_tersimpan).click()

    def click_button_cari(self):    
        self.driver.find_element(AppiumBy.ID,NavbarLocator.button_cari).click()

    def click_button_suntingan(self):    
        self.driver.find_element(AppiumBy.ID,NavbarLocator.button_suntingan).click()

    def click_button_selebihnya(self):    
        self.driver.find_element(AppiumBy.ID,NavbarLocator.button_selebihnya).click()

    def click_button_masuk_log(self):    
        self.driver.find_element(AppiumBy.ID,NavbarLocator.button_masuk_log).click()

    def click_button_pengaturan(self):    
        self.driver.find_element(AppiumBy.ID,NavbarLocator.button_pengaturan).click()
        
    def click_button_menyumbang(self):    
        self.driver.find_element(AppiumBy.ID,NavbarLocator.button_menyumbang).click()