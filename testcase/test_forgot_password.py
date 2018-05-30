import sys
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

forgt_pass = pages.Forgot_Password()
login = pages.Login()

class TestFPass():

    femail = "gamns08+yogya2@gmail.com"
    def test_forgot_password(self):
        login.verified_all_element()
        forgt_pass.click_forgot_password()
        forgt_pass.fill_email_password(self.femail)
        forgt_pass.click_reset_link(self.femail)
        # bisa ditambah verify muncul success message
