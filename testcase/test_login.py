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
logout = pages.Logout()
#dashboard = pages.Dashboard(driver)
#navbar = page.Navbar(driver)
#feature_menu = pages.Feature(driver)
#user_profile = pages.UserProfile(driver)


#@pytest.mark.usefixtures("reset_app")
class TestLogin():

    def test_invalid_login3x(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya2@gmail.com")
        login.input_password("ZXas12")
        login.tap_sign_in()
        login.invalid_userpass()
        login.tap_sign_in()
        login.invalid_userpass()
        login.tap_sign_in()
        login.invalid_userpass()
        logout.logout()
        #login.error_message()
        #login.verify_login_is_failed()

    def test_multiple_account_login(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya2@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        login.select_company()
        logout.logout()

    def test_single_login(self):
        login.verified_all_element()
        login.input_email("gamns04+menti1@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        logout.logout()

    def test_invalid_login(self):
        login.verified_all_element()
        login.input_email("gamns04+menti1@gmail")
        login.input_password("ZXqw12")
        login.tap_sign_in()
        logout.logout()

# buat case untuk invalid login 3x + verify countdown
# buat case untuk user yang single & multiple account