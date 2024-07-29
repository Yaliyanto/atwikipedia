from selenium.webdriver.common.by import By
from locator.list_inkuiri_locator import *


class ListInkuiriPage:

    def __init__(self,driver):
        self.driver = driver

    def click_kolom_nomor_inkuiri(self):
        self.driver.find_element(By.XPATH,Listinkuiri.kolom_input_nomor_inkuiri).click()

    def click_kolom_nomor_inkuiri_class(self):
        self.driver.find_element(By.CLASS_NAME,Listinkuiri.kolom_input_nomor_inkuiri_class).click()

    def input_kolom_nomor_inkuiri(self):
        self.driver.find_element(By.XPATH,Listinkuiri.kolom_input_nomor_inkuiri).send_keys("00000")

    def verifikasi_subjudul_jadwal(self):
        text = self.driver.find_element(By.XPATH,Listinkuiri.subjudul_jadwal).text

        return text
    
    def verifikasi_subjudul_jadwal_id(self):
        text = self.driver.find_element(By.XPATH,Listinkuiri.subjudul_jadwal_id).text

        return text

