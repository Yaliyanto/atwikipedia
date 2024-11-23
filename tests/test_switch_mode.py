from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
import pytest
from pageobject.pagenavbar import *
from pageobject.pageonboaring import *
from pageobject.pagecari import *
from pageobject.pagepengaturan import *
from pageobject.pagedetailartikel import *
from appium import webdriver
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



def test_switch_mode_gelap(setup):
    halaman_onboarding = OnboardingPage(setup)
    button_navbar =  NavbarButton(setup)
    halaman_pengaturan = PengaturanPage(setup)
    

    halaman_onboarding.click_button_lewati()
    button_navbar.click_button_selebihnya()
    button_navbar.click_button_pengaturan()
    halaman_pengaturan.click_tema_aplikasi()
    halaman_pengaturan.click_pilih_tema_aplikasi_hitam()
    sleep(3)
    halaman_pengaturan.click_pilih_tema_aplikasi_sepia()
    sleep(3)
    halaman_pengaturan.click_pilih_tema_aplikasi_gelap()
    sleep(3)
    halaman_pengaturan.click_pilih_tema_aplikasi_putih()
    sleep(3)

