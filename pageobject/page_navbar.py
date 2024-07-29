from selenium.webdriver.common.by import By
from locator.navbar_locator import NavbarLocator


class Navbarpage:

    def __init__(self,driver):
        self.driver = driver

    def click_menu_dasboard_navbar(self):    
        self.driver.find_element(By.ID, NavbarLocator.menu_inkuiri).click()

    def click_menu_inkuiri_navbar(self):
        self.driver.find_element(By.ID, NavbarLocator.menu_inkuiri).click()

    def click_menu_management_navbar(self):
        self.driver.find_element(By.ID, NavbarLocator.menu_management).click()

    def click_menu_report_navbar(self):
        self.driver.find_element(By.ID, NavbarLocator.menu_report).click()

    def click_menu_announcement(self):
        self.driver.find_element(By.ID, NavbarLocator.menu_announcement).click()

    def click_menu_schedule_board(self):
        self.driver.find_element(By.ID,NavbarLocator.menu_scheduleboard).click()

    def click_button_later_popup_dashboard(self):
        self.driver.find_element(By.ID,NavbarLocator.button_later_pop_up_dashboard).click()

    def click_button_subscribe_popup_dashboard(self):
        self.driver.find_element(By.ID,NavbarLocator.button_later_subscribe_dashboard).click()