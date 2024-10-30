from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
import pytest
from pageobject.pagenavbar import *
from pageobject.pageonboaring import *
from pageobject.pagejelajahi import *
from pageobject.pagecari import *
from pageobject.pagedetailartikel import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium. webdriver.common.appiumby import AppiumBy
from time import sleep

def init_driver():
    options = UiAutomator2Options()

    options.udid = '127.0.0.1:62001'
    options.platform_name = 'Android'
    options.app_package = 'org.wikipedia'
    options.app_activity = '.main.MainActivity'
    options.no_reset = False

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)

    return driver 


@pytest.fixture
def setup():
    driver = init_driver()
    yield driver



def test_page_cari_popup_panjang(setup):
    halamanonboarding = OnboardingPage(setup)
    buttonnavbar =  NavbarButton(setup)
    halamancari = PageCari(setup)
    detailarticle = NavabarDetailArticle(setup)

    halamanonboarding.click_button_lewati()
    buttonnavbar.click_button_cari()
    halamancari.click_kolom_cari_wikipedia()
    halamancari.input_kolom_cari_wikipedia()
    halamancari.click_nama_maudy_efforsina()
    detailarticle.click_button_simpan()
    try:
        WebDriverWait(setup, 10).until(EC.presence_of_element_located((AppiumBy.ID,'org.wikipedia:id/snackbar_text')))
        pop_up_panjang_text = setup.find_element(AppiumBy.ID, 'org.wikipedia:id/snackbar_text').text
        
    except TimeoutException:
        print('element gak muncul')

    assert pop_up_panjang_text == 'Maudy Effrosina disimpan. Apakah anda mau menambahkannya ke daftar?'













# def test_page_cari(setup):
#     halamanonboarding = OnboardingPage(setup)
#     buttonnavbar =  NavbarButton(setup)
#     halamancari = PageCari(setup)
#     detailarticle = NavabarDetailArticle(setup)

#     halamanonboarding.click_button_lewati()
#     buttonnavbar.click_button_cari()
#     halamancari.click_kolom_cari_wikipedia()
#     halamancari.input_kolom_cari_wikipedia()
#     halamancari.click_nama_maudy_efforsina()
#     detailarticle.click_button_simpan()
#     try:
#         WebDriverWait(setup, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'org.wikipedia:id/snackbar_action')))
#         pop_up_tambah_ke_daftar_text = setup.find_element(AppiumBy.ID, 'org.wikipedia:id/snackbar_action').text
        
#     except TimeoutException:
#         print('element gak muncul')

#     assert pop_up_tambah_ke_daftar_text == 'Tambah ke daftar'



