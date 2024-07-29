from appium. webdriver.common.appiumby import AppiumBy
from locators.pengaturan_locator import PengaturanLocator

class PengaturanPage:

    def __init__(self,driver):
        self.driver = driver

    def click_button_logout(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.button_keluar_logout).click()

    def click_button_logout_xpath(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.button_keluar_logout_xpath).click()

    def click_button_logout_popup(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.button_keluar_log_popup).click()

    def click_button_logout_popup_xpath(self):    
        self.driver.find_element(AppiumBy.XPATH,PengaturanLocator.button_keluar_log_popup_xpath).click()

