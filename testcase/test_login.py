import sys
import os
import pytest
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import page

directory = '%s/' % os.getcwd()

login = page.Login()
dashboard = page.Dashboard()
navbar = page.Navbar()
feature_menu = page.Feature()
user_profile = page.UserProfile()
switch_account = page.SwitchAccount()
forgt_pass = page.ForgotPassword()


@pytest.mark.usefixtures("reset_app")
class TestLogin():

    def test_login_wrong_password(self):
        login.verified_all_element()
        login.input_email("gamns08+yogya2@gmail.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        login.verify_login_is_failed()