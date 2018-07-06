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
logout = pages.Logout()
edit_profile = pages.Edit_Profile()
password = 'ZXasqw12'
mentor = "gamns08+yogya2@gmail.com"
mentee = "gamns08+yogya3@gmail.com"

class TestEditProfile():

    def test_edit_profile_mentee(self):
        login.verified_all_element()
        login.input_email(mentee)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(0)
        edit_profile.edit_personal_detail_mentee('Eremes','Gultom','EG',0,'0838214377')
        time.sleep(2)
        logout.logout(2)

    def test_edit_bio_mentee(self):
            login.verified_all_element()
            login.input_email(mentee)
            login.input_password(password)
            login.tap_sign_in()
            login.select_company(0)
            edit_profile.edit_biography_mentee('cool man Mentee','Priest')
            time.sleep(2)
            logout.logout(2)

    def test_edit_education_mentee(self):
            login.verified_all_element()
            login.input_email(mentee)
            login.input_password(password)
            login.tap_sign_in()
            login.select_company(0)
            edit_profile.edit_education_mentee('Architect','Interior',1,1)
            time.sleep(2)
            logout.logout(2)

    def test_edit_experience_mentee(self):
        login.verified_all_element()
        login.input_email(mentee)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(0)
        edit_profile.edit_current_experience_mentee('Pilot','Aircraft','March 2018',5)
        time.sleep(2)
        edit_profile.edit_previous_experience_mentee('Soldier', 'Holy War', 'July 2018','December 2019')
        logout.logout(2)

