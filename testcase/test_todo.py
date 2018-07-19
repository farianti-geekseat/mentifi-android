import sys
import time
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
email = 'gamns08+yogya3@gmail.com'
password = 'ZXasqw12'
todo = pages.ToDo()
login = pages.Login()
logout = pages.Logout()

class TestToDo():

    def test_add_todo_self(self):
        login.verified_all_element()
        login.input_email(email)
        login.input_password(password)
        login.tap_sign_in()
        login.select_company(0)
        todo.click_todo()
        time.sleep(3)
        todo.add_todo_self('test1','auto')
        time.sleep(2)
        # logout.logout(2)

    def test_add_todo_mentor(self):
        # login.verified_all_element()
        # login.input_email(email)
        # login.input_password(password)
        # login.tap_sign_in()
        # login.select_company(0)
        todo.click_todo()
        time.sleep(3)
        todo.add_todo_mentor('test1','auto','tif')
        time.sleep(2)
        # logout.logout(2)

    def test_edit_todo_self(self):
        # login.verified_all_element()
        # login.input_email(email)
        # login.input_password(password)
        # login.tap_sign_in()
        # login.select_company(0)
        todo.click_todo()
        time.sleep(5)
        todo.edit_todo_self(0,'automate todo','auto')
        time.sleep(3)
        #todo.click_complete()
        # logout.logout(2)

    def test_edit_todo_mentor(self):
        # login.verified_all_element()
        # login.input_email(email)
        # login.input_password(password)
        # login.tap_sign_in()
        # login.select_company(0)
        todo.click_todo()
        time.sleep(5)
        #todo.click_ongoing()
        #time.sleep(1)
        todo.edit_todo_mentor(0,'automate mentor','tif','auto')
        time.sleep(2)
        #todo.click_complete()
        # logout.logout(2)

    def test_delete_todo_self(self):
        # login.verified_all_element()
        # login.input_email(email)
        # login.input_password(password)
        # login.tap_sign_in()
        # login.select_company(0)
        # todo.click_todo()
        time.sleep(2)
        todo.delete_todo_self(0)
        time.sleep(2)
        # logout.logout(2)

    def test_delete_todo_mentor(self):
        # login.verified_all_element()
        # login.input_email(email)
        # login.input_password(password)
        # login.tap_sign_in()
        # login.select_company(0)
        todo.click_todo()
        time.sleep(5)
        todo.delete_todo_mentor(0,'tif')
        time.sleep(2)
        # logout.logout(2)

    def test_complete_todo_self(self):
        # login.verified_all_element()
        # login.input_email(email)
        # login.input_password(password)
        # login.tap_sign_in()
        # login.select_company(0)
        # todo.click_todo()
        todo.click_ongoing()
        time.sleep(5)
        todo.complete_todo_self(0)
        time.sleep(2)
        # logout.logout(2)

    def test_complete_todo_mentor(self):
        # login.verified_all_element()
        # login.input_email(email)
        # login.input_password(password)
        # login.tap_sign_in()
        # login.select_company(0)
        # todo.click_todo()
        todo.click_ongoing()
        time.sleep(5)
        todo.complete_todo_mentor(0,'tif')
        time.sleep(2)
        # logout.logout(2)


    def test_incomplete_todo_self(self):
        # login.verified_all_element()
        # login.input_email(email)
        # login.input_password(password)
        # login.tap_sign_in()
        # login.select_company(0)
        # todo.click_todo()
        time.sleep(5)
        todo.incomplete_todo_self(0)
        time.sleep(2)
        # logout.logout(2)

    def test_incomplete_todo_mentor(self):
        # login.verified_all_element()
        # login.input_email(email)
        # login.input_password(password)
        # login.tap_sign_in()
        # login.select_company(0)
        todo.click_todo()
        time.sleep(5)
        todo.incomplete_todo_mentor(0,'tif')
        time.sleep(2)
        logout.logout(2)