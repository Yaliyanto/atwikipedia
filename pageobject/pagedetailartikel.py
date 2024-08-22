from appium. webdriver.common.appiumby import AppiumBy
from locators.navbar_articlelocator import NavbarArticle

class NavabarDetailArticle:

    def __init__(self,driver):
        self.driver = driver

    def click_button_simpan(self):
        self.driver.find_element(AppiumBy.ID,NavbarArticle.button_simpan).click()

    def click_button_bahasa(self):
        self.driver.find_element(AppiumBy.ID,NavbarArticle.button_bahasa).click()

    def click_button_cari_di_artikel(self):
        self.driver.find_element(AppiumBy.ID,NavbarArticle.button_cari_di_artikel).click()

    def click_button_tema(self):
        self.driver.find_element(AppiumBy.ID,NavbarArticle.button_tema).click()

    def click_button_daftar_isi(self):
        self.driver.find_element(AppiumBy.ID,NavbarArticle.button_daftar_isi).click()

    def validasi_subjudul_maudy_effrosina(self):
        text = self.driver.find_element(AppiumBy.XPATH,NavbarArticle.Maudy_Effrosina_xpath).text

        return text
    
    def validasi_pop_up_tersimpan_article(self):
        text = self.driver.find_element(AppiumBy.ID,NavbarArticle.pop_up_tersimpan).text

        return text
    
    def validasi_pop_up_tersimpan_article_xpath(self):
        text = self.driver.find_element(AppiumBy.XPATH,NavbarArticle.pop_up_tersimpan_xpath).text

        return text
    
    def validasi_pop_up_tersimpan_article_class(self):
        text = self.driver.find_element(AppiumBy.XPATH,NavbarArticle.pop_up_tersimpan_class).text

        return text
    
    def validasi_pop_up_tambah_ke_daftar(self):
        text = self.driver.find_element(AppiumBy.CLASS_NAME,NavbarArticle.pop_up_tambah_ke_daftar).text

        return text
    
    def validasi_pop_up_tambah_ke_daftar_id(self):
        text = self.driver.find_element(AppiumBy.ID,NavbarArticle.pop_up_tambah_ke_daftar_id).text

        return text