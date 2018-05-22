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

connection_dash = pages.Connection()
login = pages.Login()

class TestConnection():

    def test_connection(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya2@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        login.select_company()
        connection_dash.click_connection()
        connection_dash.click_connected()
        connection_dash.click_pending()
        connection_dash.click_request()
