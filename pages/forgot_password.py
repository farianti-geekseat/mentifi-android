from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page import Page

import pytest



class Forgot_Password(Page):

    forgot_password = (By.ID, "com.hub.mentifi:id/text_forgot")

    def click_forgot_password(self):
        self.find_element(self.forgot_password).click()
