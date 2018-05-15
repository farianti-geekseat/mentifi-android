from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page import Page

import pytest



class Register(Page):

    register = (By.XPATH, "//*[@text='Register personal account']")
    fname = (By.XPATH,"//*[@contentDescription='First Name']")
    lname = (By.XPATH,"//*[@contentDescription='Last Name']")
    salutation = (By.XPATH,"//*[@contentDescription='']")
    remail = (By.XPATH,"//*[@contentDescription='Email' and (./preceding-sibling::* | ./following-sibling::*)[./*[@contentDescription='You are registering as ']]]")
    rpass = (By.XPATH,"((//*[@contentDescription=concat('Welcome to Mentifi - Let', ''', 's create your account')]/*[@class='android.view.View'])[2]/*[@class='android.widget.EditText'])[5]")
    rrpass = (By.XPATH,"((//*[@contentDescription=concat('Welcome to Mentifi - Let', ''', 's create your account')]/*[@class='android.view.View'])[2]/*[@class='android.widget.EditText'])[6]")
    tnc = (By.XPATH,"//*[@contentDescription=' I have read and accept Mentifi ']")
    create_but = (By.XPATH,"//*[@contentDescription='Create Mentifi account']")

    email = (By.XPATH,"//*[@contentDescription='Email' and (./preceding-sibling::* | ./following-sibling::*)[@contentDescription='Already a member?']]")
    password = (By.XPATH,"((//*[@contentDescription=concat('Welcome to Mentifi - Let', ''', 's create your account')]/*/*[@class='android.view.View' and ./parent::*[@class='android.view.View']])[4]/*[@class='android.widget.EditText'])[2]")
    fgt_pass = (By.XPATH,"//*[@contentDescription='I forgot my password']")
    login_but = (By.XPATH,"//*[@contentDescription='Login']")






