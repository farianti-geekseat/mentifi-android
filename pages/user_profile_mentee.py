from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page


class UserProfileMentee(Page):

    '''user basic info'''
    user_image = (By.ID, "com.hub.mentifi:id/image_profile")
    user_name = (By.ID, "com.hub.mentifi:id/text_profile_name")
    user_sex = (By.ID, "com.hub.mentifi:id/text_profile_sex")
    user_mentee_mentor_count = (By.ID, "com.hub.mentifi:id/text_profile_count")
    user_email_address = (By.ID, "com.hub.mentifi:id/text_profile_email")
    user_personal_number = (By.ID, "com.hub.mentifi:id/text_profile_phone")
    user_work_number = (By.ID, "com.hub.mentifi:id/text_profile_phone_work")

    '''mentee extended info'''
    '''tab profile'''
    profile_tab = (By.XPATH, "//*[@bounds='[0,440][144,536]']")
    about_me_text = (By.ID, "com.hub.mentifi:id/text_about_me")
    skill_develop_text = (By.ID, "com.hub.mentifi:id/text_skills")

    '''tab address'''
    mailing_address_tab = (By.XPATH, "//*[@bounds='[144,440][383,536]']")
    address = (By.ID, "com.hub.mentifi:id/text_address")

    '''tab education'''
    education_tab = (By.XPATH, "//*[@bounds='[383,440][554,536]']")
    degree_name = (By.ID, "com.hub.mentifi:id/text_content1")
    institution_name = (By.ID, "com.hub.mentifi:id/text_content2")
    year_completed = (By.ID, "com.hub.mentifi:id/text_year_completition")

    '''tab employment'''
    employment_tab = (By.XPATH, "//*[@bounds='[554,440][720,536]']")
    employer_name = (By.ID, "com.hub.mentifi:id/text_content1")
    employment_description = (By.ID, "com.hub.mentifi:id/text_content2")

    more_button = (By.XPATH, "//*[@bounds='[640,55][720,151]']")
    logout = (By.ID, "com.hub.mentifi:id/title")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.profile_tab))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.mailing_address_tab))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.education_tab))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.employment_tab))
            print("User profile page is completely loaded")
        except TimeoutException:
            print("User profile page is not ready")

    def tap_profile_tab(self):
        self.find_element(self.profile_tab).click()

    def tap_mailing_address_tab(self):
        self.find_element(self.mailing_address_tab).click()

    def tap_education_tab(self):
        self.find_element(self.education_tab).click()

    def tap_employment_tab(self):
        self.find_element(self.employment_tab).click()

    def tap_logout(self):
        self.find_element(self.more_button).click()
        self.find_element(self.logout).click()