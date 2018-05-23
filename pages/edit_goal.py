from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page


class EditGoal(Page):
    page_title = (By.XPATH, "//*[@text='Edit Goal']")
    goal_title = (By.ID, "com.hub.mentifi:id/input_goal")
    goal_probability = (By.ID, "com.hub.mentifi:id/spinner_probability")
    goal_save_button = (By.ID, "com.hub.mentifi:id/btn_save")
    goal_cancel_button = (By.ID, "com.hub.mentifi:id/btn_cancel")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verify_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.page_title))
            print("Edit Goal page is completely loaded")
        except TimeoutException:
            print("Edit Goal page is not ready")

    def fill_goal_title(self):
        self.find_element(self.goal_title).click()

    def fill_goal_probability(self):
        self.find_element(self.goal_probability).click()

    def tap_save_button(self):
        self.find_element(self.goal_save_button).click()

    def tap_cancel_button(self):
        self.find_element(self.goal_cancel_button).click()