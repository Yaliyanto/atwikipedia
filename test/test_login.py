from selenium import webdriver
from pageobject.page_login import *
from locator.login_locator import *
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    # Inisialisasi webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login_dengan_password_invalid(driver):

    driver.get("https://staging-propel.bamms.co/")
    halamanlogin = Loginpage(driver)
    sleep(3)
    halamanlogin.input_email()
    sleep(2)
    halamanlogin.input_password_salah()
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
    sleep(2)
    text = halamanlogin.validasi_allert_login()
    sleep(10)
    assert text == 'Incorrect user / password'

def test_login_dengan_data_valid(driver):
   
    driver.get("https://staging-propel.bamms.co/")
    halamanlogin = Loginpage(driver)
    sleep(3)
    halamanlogin.input_email()
    sleep(2)
    halamanlogin.input_password()
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
    text = halamanlogin.validasi_berikut_aktivitas_anda_hari_ini()
    sleep(10)
    assert text == 'Berikut aktivitas anda hari ini' 

def test_login_tanpa_email(driver):

    driver.get("https://staging-propel.bamms.co/")
    halamanlogin = Loginpage(driver)
    sleep(3)
    halamanlogin.input_password()
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
    sleep(2)
    text = halamanlogin.validasi_allert_login()
    sleep(10)
    assert text == 'Incorrect user / password'

def test_login_tanpa_password (driver):

    driver.get("https://staging-propel.bamms.co/")
    halamanlogin = Loginpage(driver)
    sleep(3)
    halamanlogin.input_email()
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
    sleep(2)
    text = halamanlogin.validasi_allert_login()
    sleep(10)
    assert text == 'Incorrect user / password'
    
def test_login_tanpa_password_email (driver):

    driver.get("https://staging-propel.bamms.co/")
    halamanlogin = Loginpage(driver)
    sleep(3)
    halamanlogin.click_tick_box_term_condition()
    sleep(2)
    halamanlogin.click_button_agree_term_condition()
    sleep(2)
    halamanlogin.click_tick_box_privacy_policy()
    sleep(2)
    halamanlogin.click_button_agree_privacy_policy()
    sleep(2)
    halamanlogin.click_button_login()
    sleep(2)

def test_login_tanpa_tickbox_privacy_policy(driver):

    driver.get("https://staging-propel.bamms.co/")
    halamanlogin= Loginpage(driver)
    sleep(3)
    halamanlogin.input_email()
    sleep(3)
    halamanlogin.input_password()
    sleep(3)
    halamanlogin.click_tick_box_term_condition()
    sleep(2)
    halamanlogin.click_button_agree_term_condition()
    sleep(2)
    halamanlogin.click_button_login()

def test_login_tanpa_tickbox_term_condition(driver):

    driver.get("https://staging-propel.bamms.co/")
    halamanlogin= Loginpage(driver)
    sleep(3)
    halamanlogin.input_email()
    sleep(3)
    halamanlogin.input_password()
    sleep(3)
    halamanlogin.click_tick_box_term_condition()
    sleep(2)
    halamanlogin.click_button_agree_term_condition()
    sleep(2)
    halamanlogin.click_button_login()

def test_login_tanpa_tickbox(driver):

    driver.get("https://staging-propel.bamms.co/")
    halamanlogin= Loginpage(driver)
    sleep(3)
    halamanlogin.input_email()
    sleep(3)
    halamanlogin.input_password()
    sleep(3)
    halamanlogin.click_button_login()
    sleep(3)

def test_login_tanpa_isi_data(driver):

    driver.get("https://staging-propel.bamms.co/")
    halamanlogin=Loginpage(driver)
    sleep(3)
    halamanlogin.click_tick_box_term_condition()
    sleep(3)
    halamanlogin.click_button_agree_term_condition()
    sleep(3)
    halamanlogin.click_tick_box_privacy_policy()
    sleep(3)
    halamanlogin.click_button_agree_privacy_policy()
    sleep(3)
    halamanlogin.click_button_login

# def test_login_tanpa_isi_data_dan_tickbox(driver):


    driver.get("https://staging-propel.bamms.co/")
    halamanlogin=Loginpage(driver)
    sleep(3)
    halamanlogin.click_button_login()

def test_login_dengan_swipe_di_privacy_policy(driver):


    driver.get("http://propel.bamms.co/#!/")
    halamanlogin = Loginpage(driver)
    sleep(3)
    halamanlogin.input_email()
    sleep(2)
    halamanlogin.input_password_salah()
    sleep(2)
    halamanlogin.click_tick_box_term_condition()
    sleep(2)
    driver.find_element(By.XPATH, 'id("pdf_container').send_keys(Keys.PAGE_DOWN)
    sleep(10)

    # XPATH : //*[@id="pdf_container"]/div[15]



