from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
import pytest
from pageobject.pagebuatakunbaru import *
from pageobject.pagemasuklog import *
from pageobject.pagenavbar import *
from pageobject.pageonboaring import *
from pageobject.pagejelajahi import *
from pageobject.pagepengaturan import *
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium. webdriver.common.appiumby import AppiumBy
from time import sleep
from pageobject.actionscrollswipe import *

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

# Use valid data to login to Wikipedia
# def test_login_positive(setup):
#     halamanonboarding = OnboardingPage(setup)
#     buttonnavbar = NavbarButton(setup)
#     buatakunbaru = BuatAkunbarupage(setup)
#     halamanmasuklog = MasukLogPage(setup)
#     halamanjelajahi = JelajahiPage(setup)
    
    
#     halamanonboarding.click_button_lewati()
#     buttonnavbar.click_button_selebihnya()
#     buttonnavbar.click_button_masuk_log()
#     buatakunbaru.click_button_masuk_log_buat_akun_baru()
#     halamanmasuklog.click_kolom_nama_pengguna()
#     halamanmasuklog.input_nama_pengguna()
#     halamanmasuklog.click_kolom_kata_sandi()
#     halamanmasuklog.input_kata_sandi()
#     halamanmasuklog.click_button_masuk_log()
#     halamanjelajahi.validasi_button_mengerti()
    
#     text = halamanjelajahi.validasi_button_mengerti()
#     assert text == 'Mengerti'

#use invalid data to login to Wikipedia
# def test_login_negative(setup):
#     halamanonboarding = OnboardingPage(setup)
#     buttonnavbar = NavbarButton(setup)
#     buatakunbaru = BuatAkunbarupage(setup)
#     halamanmasuklog = MasukLogPage(setup)
    
    
#     halamanonboarding.click_button_lewati()
#     buttonnavbar.click_button_selebihnya()
#     buttonnavbar.click_button_masuk_log()
#     buatakunbaru.click_button_masuk_log_buat_akun_baru()
#     halamanmasuklog.click_kolom_nama_pengguna()
#     halamanmasuklog.input_nama_pengguna_salah()
#     halamanmasuklog.click_kolom_kata_sandi()
#     halamanmasuklog.input_kata_sandi()
#     halamanmasuklog.click_button_masuk_log()
#     try:
#         WebDriverWait(setup, 20).until(EC.presence_of_element_located((AppiumBy.ID, 'org.wikipedia:id/snackbar_text')))
#         pop_up_kata_sandi_salah = setup.find_element(AppiumBy.ID, 'org.wikipedia:id/snackbar_text').text
        
#     except TimeoutException:
#         print('element gak muncul')

#     assert pop_up_kata_sandi_salah == 'Kata sandi yang Anda masukkan salah.\nSilakan coba lagi.'

# Login with valid data then logout from application
def test_login_positive_then_logout(setup):
    halaman_onboarding = OnboardingPage(setup)
    button_navbar = NavbarButton(setup)
    buat_akun_baru = BuatAkunbarupage(setup)
    halaman_masuk_log = MasukLogPage(setup)
    halaman_jelajahi = JelajahiPage(setup)
    halaman_pengaturan = PengaturanPage(setup)
    aksi_scroll = AksiSwipe(setup)
    
    
    halaman_onboarding.click_button_lewati()
    button_navbar.click_button_selebihnya()
    button_navbar.click_button_masuk_log()
    buat_akun_baru.click_button_masuk_log_buat_akun_baru()
    halaman_masuk_log.click_kolom_nama_pengguna()
    halaman_masuk_log.input_nama_pengguna()
    halaman_masuk_log.click_kolom_kata_sandi()
    halaman_masuk_log.input_kata_sandi()
    halaman_masuk_log.click_button_masuk_log()
    button_navbar.click_button_selebihnya() 
    button_navbar.click_button_pengaturan()
    element_locator = (AppiumBy.ID, PengaturanLocator.list_keluar_logout)
    aksi_scroll.scroll_using_adb_until_element_found(element_locator)
    halaman_pengaturan.click_button_logout()
    halaman_pengaturan.click_button_logout_popup()
    
    text = halaman_jelajahi.validasi_button_mengerti()
    assert text == 'Mengerti'
