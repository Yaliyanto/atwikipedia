from selenium import webdriver
from pageobject.page_login import *
from locator.login_locator import *
from locator.navbar_locator import *
from pageobject.page_allert import *
from pageobject.page_navbar import *
from pageobject.page_submenu_inkuiri import *
from pageobject.page_listinkuir import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep

kunci = [
    ("staffdemo@bamms.co", "password", 'Berikut aktivitas anda hari ini'), # username & password yang valid
    ("staffdemo@bamms.co", "paswordddd", "Incorrect user / password"), #id valid namun password invalid
    ("staffdemoo@bamms.co", "password", "User account not found"), #id invalid namun password valid
    ("usergakjelas@yahoo.com", "password", "User account not found"), #id invalid & password invalid
    ("","","Incorrect user / password") #gak ada input data
]


@pytest.mark.parametrize ('a,b,c ',kunci)
def test_module_login(a,b,c):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try: 
        driver.get("https://staging-propel.bamms.co/")
        halamanlogin = Loginpage(driver)
        allertlogin = AllertLogin(driver)
        sleep(3)
        halamanlogin.driver.find_element(By.ID, LoginLocator.input_email).send_keys(a)
        sleep(2)
        halamanlogin.driver.find_element(By.ID, LoginLocator.input_password).send_keys(b)
        sleep(2)
        halamanlogin.click_tick_box_term_condition()
        sleep(2)
        halamanlogin.click_button_agree_term_condition()
        sleep(2)
        halamanlogin.click_tick_box_privacy_policy()
        sleep(2)
        halamanlogin.click_button_agree_privacy_policy()
        sleep(2)
        halamanlogin.click_button_login()
        sleep(5)
        text = allertlogin.get_validation_message_login()
        sleep(10)
        assert text == c
    finally:
        driver.quit()
