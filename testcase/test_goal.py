import sys
import os
import pytest
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import pages
from connection import Connection
import time

directory = '%s/' % os.getcwd()

driver = Connection.driver

goal = pages.Goal()
login = pages.Login()
logout = pages.Logout()
email ="gamns08+yogya3@gmail.com"
password = "ZXasqw12"

class TestGoal():


    def test_add_goal_self(self):
        login.verified_all_element()
        login.input_email(email)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(0)
        goal.click_goal()
        time.sleep(2)
        goal.add_goal('test goal1',2)
        time.sleep(1)
        logout.logout(2)

    def test_remove_goal_self(self):
        login.verified_all_element()
        login.input_email(email)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(0)
        goal.click_goal()
        time.sleep(2)
        goal.remove_goal(2)
        time.sleep(1)
        logout.logout(2)


    def test_edit_goal(self):
        login.verified_all_element()
        login.input_email(email)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(1)
        goal.click_goal()
        time.sleep(3)
        goal.edit_goal(1,'set automation')
        time.sleep(1)
        logout.logout(2)