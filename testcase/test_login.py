import sys
import os
import pytest
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import pages

directory = '%s/' % os.getcwd()

login = pages.login()
dashboard = pages.Dashboard()
navbar = pages.Navbar()
feature_menu = pages.Feature()
user_profile = pages.UserProfile()
switch_account = pages.SwitchAccount()
forgot_pass = pages.ForgotPassword()


@pytest.mark.usefixtures("reset_app")
class TestLogin():

    def test_login_wrong_password(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya2@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        login.verify_login_is_failed()