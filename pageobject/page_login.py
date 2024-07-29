from selenium.webdriver.common.by import By
from locator.login_locator import LoginLocator


class Loginpage:

    def __init__(self,driver):
        self.driver = driver

    def input_email(self):    
        self.driver.find_element(By.ID, LoginLocator.input_email).send_keys("staffdemo@bamms.co")

    def input_email_salah(self):    
        self.driver.find_element(By.ID, LoginLocator.input_email).send_keys("staffdsdsemo@bamms.co")

    def input_password(self):    
        self.driver.find_element(By.ID, LoginLocator.input_password).send_keys("password")

    def input_password_salah(self):    
        self.driver.find_element(By.ID, LoginLocator.input_password).send_keys("passwsord")

    def click_tick_box_term_condition(self):    
        self.driver.find_element(By.ID, LoginLocator.click_tick_box_term_condition).click()

    def click_button_agree_term_condition(self):    
        self.driver.find_element(By.XPATH, LoginLocator.click_button_agree_term_condition).click()

    def click_tick_box_privacy_policy(self):    
        self.driver.find_element(By.XPATH, LoginLocator.click_tick_box_privacy_policy).click()

    def click_button_agree_privacy_policy(self):    
        self.driver.find_element(By.XPATH, LoginLocator.click_button_agree_privacy_policy).click()

    def click_button_login(self):
        self.driver.find_element(By.XPATH,LoginLocator.click_button_login).click()

    def validasi_allert_login(self):
        text = self.driver.find_element(By.XPATH,LoginLocator.allert_user_account_not_found).text

        return text
    
    def validasi_berikut_aktivitas_anda_hari_ini (self):
        text = self.driver.find_element(By.XPATH,LoginLocator.teks_berikut_aktivitas_anda_hari_ini).text

        return text
    




    # def validasi_teks_john_wick(self):
    #     text = self.driver.find_element(By.XPATH,LoginLocator.teks_dashboard_hi_john_wick).text

    #     return text