from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import Page

import pytest



class Logout(Page):
    more = (By.ID, 'com.hub.mentifi:id/tab_profile')
    profile = (By.ID, 'com.hub.mentifi:id/nav_profile')
    option = (By.XPATH, "//*[@contentDescription='More options']")
    logout = (By.XPATH, "//*[@text='Logout']")


    def logout(self):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        self.find_element(self.option).click()
        self.find_element(self.logout).click()
