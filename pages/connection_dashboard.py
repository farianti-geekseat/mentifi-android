from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page
import time

import pytest



class Connection(Page):
    connected =(By.XPATH,"//*[@text='Connected']")
    pending =(By.XPATH,"//*[@text='Pending']")
    request =(By.XPATH,"//*[@text='Request']")
    search =(By.XPATH,"//*[@id='search_button' and @width>0]")
    view_connect =(By.XPATH,"//*[@id='recycler_view' and @width>0]")
    add_mentor =(By.XPATH,"//*[@id='floating_action']")
    con_dash =(By.ID,'com.hub.mentifi:id/tab_network')
    list_profile = (By.ID,'com.hub.mentifi:id/recycler_view')
    yes_button = (By.ID,'com.hub.mentifi:id/btn_positive_accept')

    def click_connection(self):
        self.find_element(self.con_dash).click()

    def click_connected(self):
        self.find_element(self.connected).click()
        print("List connected: ")
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            l = i.text
            print(l)

    def click_pending(self):
        self.find_element(self.pending).click()
        print("List pending: ")
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            m = i.text
            print(m)

    def click_request(self):
        self.find_element(self.request).click()
        print("List request: ")
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            n = i.text
            print(n)
    def view_profile(self,alias):
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        test[alias].click()
        time.sleep(2)
        profile = self.driver.find_elements(By.ID, 'android:id/title')
        profile[0].click()
        time.sleep(5)
        test_parent2 = self.driver.find_element(By.ID, 'com.hub.mentifi:id/layout_header')
        test2 = self.driver.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            z = i.text
            print(z)

    def pending_view_profile(self,alias):
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        test[alias].click()
        time.sleep(2)
        # test_profile = self.driver.find_element(By.XPATH, "//*[@class='android.widget.FrameLayout' and ./*[@class='android.widget.ListView']]")
        profile = self.driver.find_elements(By.ID, 'android:id/title')
        profile[0].click()
        time.sleep(5)
        # profile[0].click()
        test_parent2 = self.driver.find_element(By.ID, 'com.hub.mentifi:id/layout_header')
        test2 = self.driver.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            g = i.text
            print(g)
#com.hub.mentifi:id/collapsing_toolbar
    #com.hub.mentifi:id/layout_header
    def pending_remove_connection(self,alias):
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        test[alias].click()
        time.sleep(2)
        profile = self.driver.find_elements(By.ID, 'android:id/title')
        profile[2].click()
        self.find_element(self.yes_button).click()
        print('connection removed')

#android.widget.RelativeLayout
    def click_search(self):
        self.find_element(self.search).click()