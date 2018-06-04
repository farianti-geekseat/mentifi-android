from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page

import pytest



class Dashboard(Page):
    con_mentee = (By.ID,'com.hub.mentifi:id/connectedCard')
    pend_mentee = (By.ID,'com.hub.mentifi:id/pendingCard')
    whatshap_mentee = (By.ID,'com.hub.mentifi:id/recycler_view')

    con_mentor = (By.ID,'com.hub.mentifi:id/connectedCard')
    pend_mentor = (By.ID,'com.hub.mentifi:id/pendingCard')
    whatshap_mentor = (By.ID,'com.hub.mentifi:id/recycler_view')

    def check_mentee_dashboard(self):
        mentee_parent = self.find_element(self.con_mentee)
        test = mentee_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            j = i.text
            print(j)

    def check_mentee_pen_dashboard(self):
        mentee_parent = self.find_element(self.pend_mentee)
        test = mentee_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            z = i.text
            print(z)

    def check_mentor_dashboard(self):
        mentor_parent = self.find_element(self.con_mentor)
        test = mentor_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            j = i.text
            print(j)

    def check_mentor_pen_dashboard(self):
        mentor_parent = self.find_element(self.pend_mentor)
        test = mentor_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            z = i.text
            print(z)

    def check_mentor_whatshap(self):
        mentor_parent = self.find_element(self.whatshap_mentor)
        test = mentor_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            j = i.text
            print(j)

    def check_mentee_whatshap(self):
        mentee_parent = self.find_element(self.whatshap_mentee)
        test = mentee_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            j = i.text
            print(j)