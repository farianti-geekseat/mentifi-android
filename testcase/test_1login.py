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

login = pages.Login()
logout = pages.Logout()
#dashboard = pages.Dashboard(driver)
#navbar = page.Navbar(driver)
#feature_menu = pages.Feature(driver)
#user_profile = pages.UserProfile(driver)
password = 'ZXasqw12'
wpass = 'ZXas12'
single_id = "gamns04+menti1@gmail.com"
multi_id = "gamns08+yogya2@gmail.com"

#@pytest.mark.usefixtures("reset_app")
class TestLogin():


    def test_single_login(self):
        login.verified_all_element()
        login.input_email(single_id)
        login.input_password(password)
        login.tap_sign_in()
        print('Successfully login')
        time.sleep(5)
        logout.logout(1)

    def test_multiple_account_login(self):
        login.verified_all_element()
        login.input_email(multi_id)
        login.input_password(password)
        login.tap_sign_in()
        time.sleep(2)
        login.select_company(0)
        print('Successfully login multiple account')
        logout.logout(2)


    def test_invalid_login3x(self):
        login.verified_all_element()
        login.input_email(multi_id)
        login.input_password(wpass)
        login.tap_sign_in()
        login.invalid_userpass()
        login.tap_sign_in()
        login.invalid_userpass()
        login.tap_sign_in()
        login.invalid_userpass()
        login.error_message()
        time.sleep(16)
        print('test_invalid_login3x')

    # def test_invalid_login(self):
    #     login.verified_all_element()
    #     login.input_email(single_id)
    #     login.input_password(wpass)
    #     login.tap_sign_in()
    #     login.invalid_userpass()
    #     print('test_invalid_login')
    #     driver.quit()
    #     #login.error_message()
    #     #login.verify_login_is_failed()
# buat case untuk invalid login 3x + verify countdown
# buat case untuk user yang single & multiple account