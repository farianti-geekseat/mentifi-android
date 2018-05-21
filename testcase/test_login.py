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

login = pages.Login()
#dashboard = pages.Dashboard(driver)
#navbar = page.Navbar(driver)
#feature_menu = pages.Feature(driver)
#user_profile = pages.UserProfile(driver)


#@pytest.mark.usefixtures("reset_app")
class TestLogin():

    def test_login_wrong_password(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya2@gmail.com")
        login.input_password("ZXas12")
        login.tap_sign_in()
        login.invalid_userpass()
        login.tap_sign_in()
        login.invalid_userpass()
        login.tap_sign_in()
        login.invalid_userpass()
        #login.error_message()
        #login.verify_login_is_failed()