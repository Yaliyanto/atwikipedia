from appium. webdriver.common.appiumby import AppiumBy
from locators.onboarding_locator import OnboardingLocator

class OnboardingPage:

    def __init__(self,driver):
        self.driver = driver

    def click_button_lewati(self):    
        self.driver.find_element(AppiumBy.ID,OnboardingLocator.button_lewati).click()

    def click_button_lanjutkan(self):    
        self.driver.find_element(AppiumBy.ID,OnboardingLocator.button_lanjutkan).click()

    def click_button_sunting(self):    
        self.driver.find_element(AppiumBy.ID,OnboardingLocator.button_tambah_atau_sunting_bahasa).click()

