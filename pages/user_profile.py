from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page


class UserProfile(Page):

    '''user basic info'''
    user_image = (By.ID, "com.hub.mentifi:id/image_profile")
    user_name = (By.ID, "com.hub.mentifi:id/text_profile_name")
    user_sex = (By.ID, "com.hub.mentifi:id/text_profile_sex")
    user_mentee_mentor_count = (By.ID, "com.hub.mentifi:id/text_profile_count")
    user_email_address = (By.ID, "com.hub.mentifi:id/text_profile_email")
    user_personal_number = (By.ID, "com.hub.mentifi:id/text_profile_phone")
    user_work_number = (By.ID, "com.hub.mentifi:id/text_profile_phone_work")

    '''mentor extended info'''
    '''tab biography'''
    biography_tab = (By.XPATH, "//*[@bounds='[0,431][144,527]']")
    biography_text = (By.ID, "com.hub.mentifi:id/text_bio")

    '''tab address'''
    mailing_address_tab = (By.XPATH, "//*[@bounds='[144,431][356,527]']")
    address = (By.ID, "com.hub.mentifi:id/text_address")

    ''' tab education'''
    education_tab = (By.XPATH, "//*[@bounds='[356,431][527,527]']")
    degree_name = (By.ID, "com.hub.mentifi:id/text_content1")
    institution_name = (By.ID, "com.hub.mentifi:id/text_content2")

    '''tab experience'''
    experience_tab = (By.XPATH, "//*[@bounds='[527,431][706,527]']")
    title_experience = (By.ID, "com.hub.mentifi:id/text_title_experience")
    experience = (By.ID, "com.hub.mentifi:id/text_experience")
    experience_description = (By.ID, "com.hub.mentifi:id/text_experience_description")

    '''tab preferences'''
    preferences_tab = (By.XPATH, "//*[@text='Preferences']")
    mentor_preferences = (By.ID, "com.hub.mentifi:id/text_like")
    mentor_preferability = (By.ID, "com.hub.mentifi:id/text_mentor_preferability")


    more_button = (By.XPATH, "//*[@bounds='[640,55][720,151]']")
    logout = (By.ID, "com.hub.mentifi:id/title")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.biography_tab))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.mailing_address_tab))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.education_tab))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.experience_tab))
            print("User profile page is completely loaded")
        except TimeoutException:
            print("User profile page is not ready")

    def tap_profile_tab(self):
        self.find_element(self.biography_tab).click()

    def tap_mailing_address_tab(self):
        self.find_element(self.mailing_address_tab).click()

    def tap_education_tab(self):
        self.find_element(self.education_tab).click()

    def tap_employment_tab(self):
        self.find_element(self.experience_tab).click()

    def tap_preferences_tab(self):
        self.find_element(self.preferences_tab).click()

    def tap_logout(self):
        self.find_element(self.logout).click()