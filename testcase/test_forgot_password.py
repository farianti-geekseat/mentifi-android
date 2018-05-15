import sys
import os
import pytest
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import Page

forgt_pass = Page.ForgotPassword()

class TestForgotPassword():

    def forgot_password(self):
        forgt_pass.click_forgot_password()

