from appium. webdriver.common.appiumby import AppiumBy
from locators.pengaturan_locator import PengaturanLocator

class PengaturanPage:

    def __init__(self,driver):
        self.driver = driver

    def click_button_logout(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.list_keluar_logout).click()

    def click_button_logout_xpath(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.list_keluar_logout_xpath).click()

    def click_button_logout_popup(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.button_keluar_log_popup).click()

    def click_button_logout_popup_xpath(self):    
        self.driver.find_element(AppiumBy.XPATH,PengaturanLocator.button_keluar_log_popup_xpath).click()

    def click_tema_aplikasi(self):    
        self.driver.find_element(AppiumBy.XPATH,PengaturanLocator.list_tema_aplikasi).click()

    def click_pilih_tema_aplikasi_hitam(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.tema_aplikasi_hitam).click()

    def click_pilih_tema_aplikasi_putih(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.tema_aplikasi_putih).click()

    def click_pilih_tema_aplikasi_gelap(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.tema_aplikasi_gelap).click()

    def click_pilih_tema_aplikasi_sepia(self):    
        self.driver.find_element(AppiumBy.ID,PengaturanLocator.tema_aplikasi_sepia).click()
