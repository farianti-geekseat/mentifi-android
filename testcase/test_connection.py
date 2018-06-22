import sys
import os
import pytest
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import pages
import time
from connection import Connection

directory = '%s/' % os.getcwd()

driver = Connection.driver

connection_dash = pages.Connection()
login = pages.Login()
password = 'ZXasqw12'
mentor = "gamns08+yogya2@gmail.com"
mentee = "gamns08+yogya3@gmail.com"
class TestConnection():

    # def test_connection_connected_view(self):
    #     login.verified_all_element()
    #     login.input_email(mentee)
    #     login.input_password(password)
    #     login.tap_sign_in()
    #     login.select_company(0)
    #     connection_dash.click_connection()
    #     connection_dash.click_connected()
    #     time.sleep(2)
    #     connection_dash.view_profile(1)

    def test_connection_pending_view(self):
        login.verified_all_element()
        login.input_email(mentee)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(0)
        connection_dash.click_connection()
        connection_dash.click_pending()
        time.sleep(2)
        connection_dash.pending_view_profile(0)

    # def test_connection_pending_remove_connection(self):
    #     login.verified_all_element()
    #     login.input_email(mentee)
    #     login.input_password(password)
    #     login.tap_sign_in()
    #     login.select_company(0)
    #     connection_dash.click_connection()
    #     connection_dash.click_pending()
    #     time.sleep(2)
    #     connection_dash.pending_remove_connection(0)