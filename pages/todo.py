from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page

import pytest



class ToDo(Page):
    ongoing =(By.XPATH,"//*[@class='android.support.v7.app.ActionBar$Tab' and ./*[@text='Ongoing']]")
    complete =(By.XPATH,"//*[@class='android.support.v7.app.ActionBar$Tab' and ./*[@text='Complete']]")
    taskname =(By.XPATH,"//*[@text='testing 2']")
    todo =(By.ID,'com.hub.mentifi:id/tab_tasks')

    def click_todo(self):
        self.find_element(self.todo).click()

    def click_ongoing(self):
        self.find_element(self.ongoing).click()
        print("List todo ongoing: ")
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            j = i.text
            print(j)

    def click_complete(self):
        self.find_element(self.complete).click()
        print("List todo complete : ")
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            k = i.text
            print(k)