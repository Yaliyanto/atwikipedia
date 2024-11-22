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


def test_button_mengerti_dashboard(setup):
    halaman_onboarding = OnboardingPage(setup)
    halaman_jelajahi =  JelajahiPage(setup)


    halaman_onboarding.click_button_lewati()
    halaman_jelajahi.click_button_mengerti()

    