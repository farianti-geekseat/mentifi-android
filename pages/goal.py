from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page

import pytest



class Goal(Page):
    goaltitle = (By.XPATH,"//*[@id='GoalTitle']")
    progress = (By.XPATH,"//*[@id='progressText']")
    chart = (By.XPATH,"//*[@id='chart']")
    goal=(By.ID,'com.hub.mentifi:id/tab_goals')


    def click_goal(self):
        self.find_element(self.goal).click()