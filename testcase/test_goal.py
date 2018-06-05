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

class TestGoal():

    def test_edit_goal(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya3@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        login.select_company(1)
        goal.click_goal()
        time.sleep(2)
        goal.check_goal()
        goal.edit_goal(1,'set automation')
        logout.logout(2)

    def test_remove_goal(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya3@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        login.select_company(1)
        goal.click_goal()
        time.sleep(2)
        goal.check_goal()
        goal.remove_goal(0)