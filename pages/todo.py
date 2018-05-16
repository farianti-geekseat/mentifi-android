from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page import Page

import pytest



class ToDo(Page):
    ongoing =(By.XPATH,"//*[@class='android.support.v7.app.ActionBar$Tab' and ./*[@text='Ongoing']]")
    complete =(By.XPATH,"//*[@class='android.support.v7.app.ActionBar$Tab' and ./*[@text='Complete']]")
    taskname =(By.XPATH,"//*[@text='testing 2']")
