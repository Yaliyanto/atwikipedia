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
from helper.common2 import *
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


def test_login_negative(setup):
    halamanonboarding = OnboardingPage(setup)
    buttonnavbar = NavbarButton(setup)
    buatakunbaru = BuatAkunbarupage(setup)
    halamanmasuklog = MasukLogPage(setup)
    
    
    halamanonboarding.click_button_lewati()
    buttonnavbar.click_button_selebihnya()
    buttonnavbar.click_button_masuk_log()
    buatakunbaru.click_button_masuk_log_buat_akun_baru()
    halamanmasuklog.click_kolom_nama_pengguna()
    halamanmasuklog.input_nama_pengguna()
    halamanmasuklog.click_kolom_kata_sandi()
    halamanmasuklog.input_kata_sandi()
    halamanmasuklog.click_button_masuk_log()
    try:
        WebDriverWait(setup, 20).until(EC.presence_of_element_located((AppiumBy.ID, 'org.wikipedia:id/snackbar_text')))
        pop_up_kata_sandi_salah = setup.find_element(AppiumBy.ID, 'org.wikipedia:id/snackbar_text').text
        
    except TimeoutException:
        print('element gak muncul')

    assert pop_up_kata_sandi_salah == 'Kata sandi yang Anda masukkan salah.\nSilakan coba lagi.'









    

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

# def test_login_positive_lalu_logout(setup):
#     halamanonboarding = OnboardingPage(setup)
#     buttonnavbar = NavbarButton(setup)
#     buatakunbaru = BuatAkunbarupage(setup)
#     halamanmasuklog = MasukLogPage(setup)
#     halamanjelajahi = JelajahiPage(setup)
#     halamanpengaturan = PengaturanPage(setup)
    
    
#     halamanonboarding.click_button_lewati()
#     buttonnavbar.click_button_selebihnya()
#     buttonnavbar.click_button_masuk_log()
#     buatakunbaru.click_button_masuk_log_buat_akun_baru()
#     halamanmasuklog.click_kolom_nama_pengguna()
#     halamanmasuklog.input_nama_pengguna()
#     halamanmasuklog.click_kolom_kata_sandi()
#     halamanmasuklog.input_kata_sandi()
#     halamanmasuklog.click_button_masuk_log()
#     buttonnavbar.click_button_selebihnya()
#     buttonnavbar.click_button_pengaturan()

#     driver = setup.driver  # Assuming 'driver' is the WebDriver instance
#     swipe_up(driver)
#     halamanpengaturan.click_button_logout()
#     halamanpengaturan.click_button_logout_popup()
    
#     text = halamanjelajahi.validasi_button_mengerti()
#     assert text == 'Mengerti'

    
# def test_login_positive_lalu_logout(setup):
#     halamanonboarding = OnboardingPage(setup)
#     buttonnavbar = NavbarButton(setup)
#     buatakunbaru = BuatAkunbarupage(setup)
#     halamanmasuklog = MasukLogPage(setup)
#     halamanjelajahi = JelajahiPage(setup)
#     aksiswipe= Aksi_Scroll(setup)
#     halamanpengaturan = PengaturanPage(setup)
    
    
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
#     buttonnavbar.click_button_selebihnya()
#     buttonnavbar.click_button_pengaturan()
#     aksiswipe.test_scroll()
#     halamanpengaturan.click_button_logout()
#     halamanpengaturan.click_button_logout_popup()
    
#     text = halamanjelajahi.validasi_button_mengerti()
#     assert text == 'Mengerti'



#assert pop_up_kata_sandi_salah == r'Kata sandi yang Anda masukkan salah.\nSilakan coba lagi'
    # assert pop_up_kata_sandi_salah == 'Kata sandi yang Anda masukkan salah.Silakan coba lagi'
# assert pop_up_kata_sandi_salah == '''Kata sandi yang Anda masukkan salah.
#     Silakan coba lagi'''


#  try:
#         WebDriverWait(setup, 20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia:id/snackbar_text"]')))
#         pop_up_kata_sandi_salah = setup.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia:id/snackbar_text"]').text
        
#     except TimeoutException:
#         print('element gak muncul')

#     assert pop_up_kata_sandi_salah == '''Kata sandi yang Anda masukkan salah.
#     Silakan coba lagi'''