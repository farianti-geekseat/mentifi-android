from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page


class AddConnection(Page):
    page_title = (By.XPATH, "//*[@text='Mentee']")
    search_title = (By.XPATH, "//*[@text='Search for Mentee']")
    search_name = (By.ID, "com.hub.mentifi:id/edit_name")
    search_preferences = (By.ID, "")
    search_button = (By.ID, "com.hub.mentifi:id/button_search")
    connection_name = (By.ID, "com.hub.mentifi:id/button_search")
    connection_status = (By.ID, "com.hub.mentifi:id/text_status")

    '''confirmation pop-up'''
    confirmation_message = (By.XPATH, "//*[@bounds='[50,310][670,1018]']")
    request_message = (By.ID, "com.hub.mentifi:id/edit_message")
    connect_button= (By.ID, "com.hub.mentifi:id/btn_positive")
    cancel_button= (By.ID, "com.hub.mentifi:id/btn_negative")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.page_title))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.search_title))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.connection_name))
            print("Add Connection page is completely loaded")
        except TimeoutException:
            print("Add Connection page is not ready")

    def type_search_keyword(self):
        self.find_element(self.search_name).send_keys("Test")

    def tap_connection(self):
        self.find_element(self.connection_name).click()

    def verifiy_connect_confirmation(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.confirmation_message))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.request_message))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.connect_button))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.cancel_button))
            print("Connection Confirmation pop-up is completely loaded")
        except TimeoutException:
            print("Connection Confirmation pop-up is not ready")

    def tap_connect_button(self):
        self.find_element(self.connect_button).click()

    def tap_cancel_button(self):
        self.find_element(self.cancel_button).click()
