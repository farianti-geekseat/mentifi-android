from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page import Page

import pytest



class Login(Page):

    username_id = (By.ID, 'com.hub.mentifi:id/input_email')
    password_id = (By.ID, 'com.hub.mentifi:id/input_password')
    sign_in_button = (By.ID, 'com.hub.mentifi:id/btn_login')
    forgot_password = (By.ID, "com.hub.mentifi:id/text_forgot")


    def __init__(self):
        super().__init__()


    def verified_all_element(self):
        try:
            self.find_element(self.username_id)
            self.find_element(self.password_id)
        except NoSuchElementException:
            pytest.fail("Element fail")

    def login(self, email, password):
        self.driver.launch_app()
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.username_id))
        except TimeoutException:
            print("element not ready")

        self.find_element(self.username_id).send_keys(email)
        self.find_element(self.password_id).send_keys(password)
        self.find_element(self.sign_in_button).click()

    def input_email(self, email):
        try:
            WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(self.username_id))
        except TimeoutException:
            print("element not ready")
        email_el = self.find_element(self.username_id)
        email_el.send_keys(email)

    def input_password(self, password):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.forgot_password))
        except TimeoutException:
            print("element not ready")
        password_el = self.find_element(self.password_id)
        password_el.send_keys(password)

    def tap_sign_in(self):
        self.find_element(self.sign_in_button).click()

    def is_login_success(self):
        pass

    def tap_forgot_password(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.username_id))
        except TimeoutException:
            print("element not ready")

        forgot_pass =  self.find_element('com.hub.mentifi:id/text_forgot')
        x = forgot_pass.location['x']
        y = forgot_pass.location['y']
        # height = forgot_pass.size['height']
        width = forgot_pass.size['width']

        positions = []
        positions.append((x + width - 20, y))
        positions.append((x + width - 10, y))
        print(positions)
        self.driver.tap(positions)