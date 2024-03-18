from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
import pytest
from pageobject.pagebuatakunbaru import *
from pageobject.pagemasuklog import *
from pageobject.pagenavbar import *
from pageobject.pageonboaring import *
from pageobject.pagejelajahi import *

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

    text = halamanmasuklog.validasi_judul()
    assert text == 'Bergabunglah dengan Wikipedia'
    

def test_login_positive(setup):
    halamanonboarding = OnboardingPage(setup)
    buttonnavbar = NavbarButton(setup)
    buatakunbaru = BuatAkunbarupage(setup)
    halamanmasuklog = MasukLogPage(setup)
    halamanjelajahi = JelajahiPage(setup)
    
    
    halamanonboarding.click_button_lewati()
    buttonnavbar.click_button_selebihnya()
    buttonnavbar.click_button_masuk_log()
    buatakunbaru.click_button_masuk_log_buat_akun_baru()
    halamanmasuklog.click_kolom_nama_pengguna()
    halamanmasuklog.input_nama_pengguna()
    halamanmasuklog.click_kolom_kata_sandi()
    halamanmasuklog.input_kata_sandi()
    halamanmasuklog.click_button_masuk_log()
    halamanjelajahi.validasi_button_mengerti()
    
    text = halamanjelajahi.validasi_button_mengerti()
    assert text == 'Mengerti'


