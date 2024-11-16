from appium. webdriver.common.appiumby import AppiumBy
from locators.cari_locator import CariLocator

class PageCari:

    def __init__(self,driver):
        self.driver = driver

    def click_kolom_cari_wikipedia(self):    
        self.driver.find_element(AppiumBy.ID,CariLocator.click_kolom_cari).click()

    def input_kolom_cari_wikipedia(self):    
        self.driver.find_element(AppiumBy.ID,CariLocator.input_kolom_cari).send_keys("John Wick")

    def click_film_john_wick(self):
        self.driver.find_element(AppiumBy.XPATH,CariLocator.list_nama_john_wick).click()

    