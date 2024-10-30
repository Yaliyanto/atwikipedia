from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
import pytest
from pageobject.pagebuatakunbaru import *
from pageobject.pagemasuklog import *
from pageobject.pagenavbar import *
from pageobject.pageonboaring import *
from pageobject.pagejelajahi import *

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

def test_search_box(setup):
    halamanonboarding = OnboardingPage(setup)
    halamanjelajahi = JelajahiPage(setup)
    scroll = Aksi_Scroll(setup)

    halamanonboarding.click_button_lewati()
    halamanjelajahi.click_kolom_search()
    halamanjelajahi.input_kolom_search()
    sleep(3)
    scroll.test_scroll_davidbayu()
    halamanjelajahi.click_list_nama_david_bayu()
    
    text = halamanjelajahi.validasi_keyword_davidbayu()

#     assert text == 'David Bayu'
    
# # def test_search_box(setup):
# #     halamanonboarding = OnboardingPage(setup)
# #     halamanjelajahi = JelajahiPage(setup)


# #     halamanonboarding.click_button_lewati()
# #     halamanjelajahi.click_kolom_search()
# #     halamanjelajahi.input_kolom_search()
    
# #     text = halamanjelajahi.validasi_keyword_automation()

# #     assert text == 'Automaton'

