from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page import Page

import pytest



class Forgot_Password(Page):

    forgot_password = (By.ID, "com.hub.mentifi:id/text_forgot")
    email_forgot_pass = (By.XPATH,"//*[@id='input_email']")
    send_reset_link = (By.XPATH,"//*[@text='Get reset link']")

    def click_forgot_password(self):
        self.find_element(self.forgot_password).click()

    def fill_email_password(self,femail):
        self.find_element(self.email_forgot_pass).send_keys(femail)

    def click_reset_link(self):
        self.find_element(self.send_reset_link).click()