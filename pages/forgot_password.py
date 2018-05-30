from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page
import time
import pytest



class Forgot_Password(Page):

    for_password = (By.XPATH, "//*[@text='Forgot your password?']")
    email_forgot_pass = (By.ID,'com.hub.mentifi:id/input_email')
    send_reset_link = (By.XPATH,"//*[@text='Get reset link']")
    success_click =(By.XPATH,"//*[@text='OK']")
    def __init__(self):
        super().__init__()

    def click_forgot_password(self):
        self.find_element(self.for_password).click()


    def fill_email_password(self,femail):
        self.find_element(self.email_forgot_pass).click()
        try:
            WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(self.email_forgot_pass))
        except TimeoutException:
            print("element not ready")
        email_for = self.find_element(self.email_forgot_pass)
        email_for.send_keys(femail)


    def click_reset_link(self,femail):
        self.find_element(self.send_reset_link).click()
        time.sleep(5)
        self.find_element(self.success_click).click()
        print('verify email has been send to : ' + femail)