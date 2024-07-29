from selenium.webdriver.common.by import By
from locator.login_locator import LoginLocator
from selenium.common.exceptions import NoSuchElementException

class AllertLogin :

    def __init__(self,driver):
        self.driver = driver

    def get_validation_message_login(self):
        try:
            #pesan user account not found
            allert = self.driver.find_element(By.XPATH, LoginLocator.allert_user_account_not_found ).text
            return allert
        except NoSuchElementException:
            pass

        try:
            #pesan user berhasil login - Berikut aktivitas anda hari ini
            allert= self.driver.find_element(By.XPATH, LoginLocator.teks_berikut_aktivitas_anda_hari_ini).text
            return allert
        except NoSuchElementException:
            pass

        try:
            #pesan user salah input password
            allert = self.driver.find_element(By.XPATH, LoginLocator.allert_incorrect_userORpassword).text
            return allert
        except NoSuchElementException:
            pass

        return "Gak ada pesan yang cocok"






