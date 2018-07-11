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

switch = pages.Switch_Account()
login = pages.Login()
logout = pages.Logout()
password = 'ZXasqw12'
single_id = "gamns04+menti1@gmail.com"
multi_id = "gamns08+yogya2@gmail.com"

class TestSwitch():

    def test_switch_account(self):
        login.verified_all_element()
        login.input_email(multi_id)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(0)
        switch.switch_account(2)
        print('Successfully switch account')
        logout.logout(2)