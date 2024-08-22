from appium. webdriver.common.appiumby import AppiumBy
from locators.jelajahi_locator import JelajahiLocator

class JelajahiPage:

    def __init__(self,driver):
        self.driver = driver

    def click_kolom_search(self):
        self.driver.find_element(AppiumBy.ID,JelajahiLocator.search_box).click()

    def input_kolom_search(self):
        self.driver.find_element(AppiumBy.ID,JelajahiLocator.input_search_box).send_keys('David')

    def click_button_sesuaikan(self):
        self.driver.find_element(AppiumBy.ID,JelajahiLocator.button_sesuaikan).click()

    def click_button_mengerti(self):
        self.driver.find_element(AppiumBy.ID,JelajahiLocator.button_mengerti).click()

    def validasi_button_mengerti(self):
        text = self.driver.find_element(AppiumBy.XPATH,JelajahiLocator.validasi_tulisan_button_mengerti).text

        return text
    
    def validasi_keyword_automation(self):
        text = self.driver.find_element(AppiumBy.XPATH,JelajahiLocator.validasi_automation_search_box).text

        return text
    
    def click_list_nama_david_bayu (self):
        self.driver.find_element(AppiumBy.XPATH,JelajahiLocator.list_search_david_bayu).click()

    def validasi_keyword_davidbayu(self):
        text = self.driver.find_element(AppiumBy.CLASS_NAME,JelajahiLocator.david_bayu_class).text

        return text
    
    def validasi_subjudul_feautured_article(self):
        text = self.driver.find_element(AppiumBy.ID,JelajahiLocator.subjudul_Feautured_article).text

        return text
    