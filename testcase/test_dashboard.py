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
dashboard = pages.Dashboard()
logout = pages.Logout()
#dashboard = pages.Dashboard(driver)
#navbar = page.Navbar(driver)
#feature_menu = pages.Feature(driver)
#user_profile = pages.UserProfile(driver)
password = 'ZXasqw12'
wpass = 'ZXas12'
mentor = "gamns04+menti1@gmail.com"
mentee = "gamns08+yogya2@gmail.com"

#@pytest.mark.usefixtures("reset_app")
class TestDashboard():


    def test_dashboard_mentor(self):
        login.verified_all_element()
        login.input_email(mentor)
        login.input_password(password)
        login.tap_sign_in()
        time.sleep(5)
        print('Successfully login')
        dashboard.check_mentor_dashboard()
        dashboard.check_mentor_pen_dashboard()
        logout.logout(1)

    def test_dashboard_mentee(self):
        login.verified_all_element()
        login.input_email(mentee)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company()
        time.sleep(5)
        print('Successfully login')
        dashboard.check_mentee_dashboard()
        dashboard.check_mentee_pen_dashboard()
        logout.logout(2)