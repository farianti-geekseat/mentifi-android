from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page


class AddProgress(Page):
    page_title = (By.XPATH, "//*[@text='New Goal Progress']")
    goal_title = (By.ID, "com.hub.mentifi:id/GoalTitle")
    goal_progress = (By.ID, "com.hub.mentifi:id/determinateBar")
    progress_reason = (By.ID, "com.hub.mentifi:id/input_reason")
    progress_save_button = (By.ID, "com.hub.mentifi:id/btn_save")
    progress_cancel_button = (By.ID, "com.hub.mentifi:id/btn_cancel")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verify_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.page_title))
            print("Add progress page is completely loaded")
        except TimeoutException:
            print("Add progress page is not ready")

    def fill_goal_progress(self):
        self.find_element(self.goal_progress).click()

    def tap_save_button(self):
        self.find_element(self.progress_save_button).click()

    def tap_cancel_button(self):
        self.find_element(self.progress_cancel_button).click()