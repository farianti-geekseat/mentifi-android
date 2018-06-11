import sys
import time
import os
import pytest
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import pages
from connection import Connection

directory = '%s/' % os.getcwd()

driver = Connection.driver

todo = pages.ToDo()
login = pages.Login()
logout = pages.Logout()

class TestToDo():

    def test_todo_self(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya3@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        login.select_company(0)
        todo.click_todo()
        time.sleep(1)
        todo.click_ongoing()
        time.sleep(1)
        todo.edit_todo_self(0,'automate todo')
        time.sleep(3)
        #todo.click_complete()
        logout.logout(2)

    def test_todo_mentor(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya3@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        login.select_company(0)
        todo.click_todo()
        time.sleep(5)
        #todo.click_ongoing()
        #time.sleep(1)
        todo.edit_todo_mentor(0,'automate mentor','agat')
        #todo.click_complete()
        logout.logout()