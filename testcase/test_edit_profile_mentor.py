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

class TestEditProfileMentor():


    def test_edit_profile_mentor(self):
        login.verified_all_element()
        login.input_email(mentor)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(0)
        edit_profile.edit_personal_detail_mentor('Yogie','Basuki','08322552763',0,'332232323')
        time.sleep(2)
        logout.logout(2)

    def test_edit_bio_mentor(self):
            login.verified_all_element()
            login.input_email(mentor)
            login.input_password(password)
            login.tap_sign_in()
            login.select_company(0)
            edit_profile.edit_biography_mentor('cool man Mentor','Slayer','gama@linkedin.com')
            time.sleep(2)
            logout.logout(2)

    def test_edit_education_mentor(self):
            login.verified_all_element()
            login.input_email(mentor)
            login.input_password(password)
            login.tap_sign_in()
            login.select_company(0)
            edit_profile.edit_education_mentor('Full Timer','ITHB','May 2018','September 2018')
            time.sleep(2)
            logout.logout(2)

    def test_edit_experience_mentor(self):
        login.verified_all_element()
        login.input_email(mentor)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(0)
        edit_profile.edit_current_experience_mentor('Chef','Kitchen','u','February 2018')
        time.sleep(2)
        edit_profile.edit_previous_experience_mentor('Priest', 'Church', 'June 2018','October 2019')
        time.sleep(3)
        edit_profile.edit_non_work_experience_mentor(0,4)
        logout.logout(2)

    def test_edit_mentor_preference(self):
            login.verified_all_element()
            login.input_email(mentor)
            login.input_password(password)
            login.tap_sign_in()
            login.select_company(0)
            edit_profile.edit_mentor_preference('a',0,1)
            time.sleep(2)
            logout.logout(2)