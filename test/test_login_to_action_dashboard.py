from selenium import webdriver
from pageobject.page_login import *
from locator.login_locator import *
from locator.navbar_locator import *
from pageobject.page_navbar import *
from pageobject.page_submenu_inkuiri import *
from pageobject.page_listinkuir import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    # Inisialisasi webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_to_engineering(driver):


    driver.get("https://staging-propel.bamms.co/")
    halamanlogin = Loginpage(driver)
    menunavbar = Navbarpage(driver)
    submenu =  SubMenuPage(driver)
    pagelistinkuiri = ListInkuiriPage(driver)

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
    sleep(10)
    text = halamanlogin.validasi_berikut_aktivitas_anda_hari_ini()
    sleep(10)
    assert text == 'Berikut aktivitas anda hari ini'
    sleep(9) 
    menunavbar.click_button_later_popup_dashboard()
    sleep(3)
    menunavbar.click_menu_inkuiri_navbar()
    sleep(8)
    submenu.click_submenu_inkuiri_engineering()
    sleep(9)
    text = submenu.validasi_teks_button_tambah_inkuiri_baru()
    sleep(10)
    assert text == "TAMBAH INQUIRY BARU"
    sleep(5)
    try:
        verfify_subjudul_judul = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, 'id("app")/div[@class="layout-main"]/div[@class="layout-content"]/div[@class="layout-content-body"]/div[@class="row default-content"]/div[@class="col-md-12 vuetable-wrapper-top"]/div[@class="vuetable-wrapper"]/div[@class="top-panel-inq"]/div[@class="table-responsive"]/table[@class="vuetable table table-striped table-border-top table-wf3 table-hover"]/thead[1]/tr[1]/th[@id="_statusArr"]'))
        )
        subjudul = verfify_subjudul_judul.text
    except TimeoutException:
        subjudul = None

        
    assert subjudul==  'Jadwal'  

# def test_login_iwo_list(driver): #hanya menverifikasi dari button tambah IWO di page list inkuiri IWO

#     driver.get("https://staging-propel.bamms.co/")
#     halamanlogin= Loginpage(driver)
#     menunavbar = Navbarpage(driver)
#     submenu = SubMenuPage(driver)
    

#     halamanlogin.input_email()
#     sleep(2)
#     halamanlogin.input_password()
#     sleep(2)
#     halamanlogin.click_tick_box_privacy_policy()
#     sleep(3)
#     halamanlogin.click_button_agree_privacy_policy()
#     sleep(4)
#     halamanlogin.click_tick_box_term_condition()
#     sleep(3)
#     halamanlogin.click_button_agree_term_condition()
#     sleep(3)
#     halamanlogin.click_button_login()
#     sleep(5)
#     text = halamanlogin.validasi_berikut_aktivitas_anda_hari_ini()
#     sleep(10)
#     assert text == 'Berikut aktivitas anda hari ini'
#     sleep(10)
#     menunavbar.click_button_later_popup_dashboard()
#     sleep(9)
#     menunavbar.click_menu_inkuiri_navbar()
#     sleep(3)
#     submenu.click_submenu_inkuiri_IWO()
#     sleep(3)
#     text = submenu.validasi_teks_button_tambah_IWO_baru()
#     sleep(9)
#     assert text == "TAMBAH INQUIRY BARU INTERNAL WORK ORDER"
#     sleep(5)


def test_login_iwo_list_inputdata(driver):

    driver.get("https://staging-propel.bamms.co/")
    halamanlogin= Loginpage(driver)
    menunavbar = Navbarpage(driver)
    submenu = SubMenuPage(driver)
    pagelistinkuiri = ListInkuiriPage(driver)
    

    halamanlogin.input_email()
    sleep(2)
    halamanlogin.input_password()
    sleep(2)
    halamanlogin.click_tick_box_privacy_policy()
    sleep(3)
    halamanlogin.click_button_agree_privacy_policy()
    sleep(4)
    halamanlogin.click_tick_box_term_condition()
    sleep(3)
    halamanlogin.click_button_agree_term_condition()
    sleep(3)
    halamanlogin.click_button_login()
    sleep(5)
    text = halamanlogin.validasi_berikut_aktivitas_anda_hari_ini()
    sleep(10)
    assert text == 'Berikut aktivitas anda hari ini'
    sleep(10)
    menunavbar.click_button_later_popup_dashboard()
    sleep(9)
    menunavbar.click_menu_inkuiri_navbar()
    sleep(3)
    submenu.click_submenu_inkuiri_IWO()
    sleep(3)
    text = submenu.validasi_teks_button_tambah_IWO_baru()
    sleep(9)
    assert text == "TAMBAH INQUIRY BARU INTERNAL WORK ORDER"
    sleep(5)
    pagelistinkuiri.click_kolom_nomor_inkuiri_class()
    sleep(5)
    pagelistinkuiri.input_kolom_nomor_inkuiri()
    sleep(5)
