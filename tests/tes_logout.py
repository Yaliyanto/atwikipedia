from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
import pytest
from pageobject.pagebuatakunbaru import *
from pageobject.pagemasuklog import *
from pageobject.pagenavbar import *
from pageobject.pageonboaring import *
from pageobject.pagejelajahi import *
from pageobject.pagepengaturan import *


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

def test_logout(setup):
    halamanonboarding = OnboardingPage(setup)
    buttonnavbar = NavbarButton(setup)
    aksiswipe = SwipeBawah(setup)
    halamanpengaturan = PengaturanPage(setup)
    halamanjelajahi = JelajahiPage(setup)
    
    
    halamanonboarding.click_button_lewati()
    buttonnavbar.click_button_selebihnya()
    buttonnavbar.click_button_pengaturan()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    aksiswipe.scroll_atas()
    halamanpengaturan.click_button_logout()
    halamanpengaturan.click_button_logout_popup()

    text = halamanjelajahi.validasi_button_mengerti()
    assert text == 'Mengerto'
    

def test_logout_no_hardcode(setup):
    halamanonboarding = OnboardingPage(setup)
    buttonnavbar = NavbarButton(setup)
    # askiscroll = Aksi_Scroll(setup)
    halamanpengaturan = PengaturanPage(setup)
    halamanjelajahi = JelajahiPage(setup)
    
    
    halamanonboarding.click_button_lewati()
    buttonnavbar.click_button_selebihnya()
    buttonnavbar.click_button_pengaturan()
    # askiscroll.test_scroll()
    halamanpengaturan.click_button_logout()
    halamanpengaturan.click_button_logout_popup()
   

    text = halamanjelajahi.validasi_button_mengerti()
    assert text == 'Mengerti'