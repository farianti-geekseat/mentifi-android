from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page

import pytest



class Connection(Page):
    connected =(By.XPATH,"//*[@text='Connected']")
    pending =(By.XPATH,"//*[@text='Pending']")
    request =(By.XPATH,"//*[@text='Request']")
    search =(By.XPATH,"//*[@id='search_button' and @width>0]")
    view_connect =(By.XPATH,"//*[@id='recycler_view' and @width>0]")
    add_mentor =(By.XPATH,"//*[@id='floating_action']")
    con_dash =(By.ID,'com.hub.mentifi:id/tab_network')

    def click_connection(self):
        self.find_element(self.con_dash).click()

    def click_connected(self):
        self.find_element(self.connected).click()

    def click_pending(self):
        self.find_element(self.pending).click()

    def click_request(self):
        self.find_element(self.request).click()

    def click_search(self):
        self.find_element(self.search).click()