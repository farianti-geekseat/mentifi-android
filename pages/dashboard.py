from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page

import pytest



class Dashboard(Page):
    con_mentee = (By.XPATH,"//*[@id='connectedCard']")
    pend_mentee = (By.XPATH,"//*[@id='pendingCard']")
    whatshap_mentee = (By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@id='appbar_layout']]")

    con_mentor = (By.XPATH,"//*[@id='connectedCard']")
    pend_mentor = (By.XPATH,"//*[@id='pendingCard']")
    whatshap_mentor = (By.XPATH,"//*[@id='recycler_view']")