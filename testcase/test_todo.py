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

class TestToDo():

    def test_todo(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya2@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        login.select_company()
        todo.click_todo()
        time.sleep(3)
        todo.click_ongoing()
        #todo.click_complete()
