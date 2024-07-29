from selenium.webdriver.common.by import By
from locator.submenu_inkuiri_locator import *

class SubMenuPage:

    def __init__(self,driver):
        self.driver = driver

    def click_submenu_inkuiri_engineering(self):    
        self.driver.find_element(By.ID, SubMenu.Submenu_engineering).click()

    def click_submenu_inkuiri_housekeeping(self):
        self.driver.find_element(By.ID, SubMenu.Submenu_housekeeping).click()

    def click_submenu_inkuiri_IWO(self):
        self.driver.find_element(By.ID, SubMenu.Submenu_IWO).click()

    def validasi_teks_daftar_permintaan(self):
        text = self.driver.find_element(By.XPATH,SubMenu.Teks_Daftar_permintaan).text

        return text
    
    def validasi_teks_daftar_permintaan_class(self):
        text = self.driver.find_element(By.CLASS_NAME,SubMenu.Teks_Daftar_permintaan_class).text

        return text
    
    def validasi_teks_button_tambah_inkuiri_baru(self):
        text = self.driver.find_element(By.XPATH,SubMenu.teks_button_tambah_inkuiry_baru).text

        return text
    
    def validasi_teks_button_tambah_IWO_baru(self):
        text = self.driver.find_element(By.XPATH,SubMenu.teks_button_tambah_iwo_baru).text

        return text