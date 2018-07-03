from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page
import time
import numpy


import pytest



class Edit_Profile(Page):
    more = (By.ID, 'com.hub.mentifi:id/tab_profile')
    profile = (By.ID, 'com.hub.mentifi:id/nav_profile')
    option = (By.XPATH, "//*[@class='android.support.v7.widget.LinearLayoutCompat']")
    fname = (By.ID,'com.hub.mentifi:id/input_first_name')
    lname = (By.ID,'com.hub.mentifi:id/input_last_name')
    pname = (By.ID,'com.hub.mentifi:id/input_preferred_name')
    phone = (By.ID,'com.hub.mentifi:id/input_mobile_phone')
    work = (By.ID,'com.hub.mentifi:id/input_work_phone')
    save_button = (By.ID,'com.hub.mentifi:id/btn_save')
    edit_bio = (By.ID,'com.hub.mentifi:id/action_edit')
    about_me = (By.ID,'com.hub.mentifi:id/input_about')
    pro_skill = (By.ID,'com.hub.mentifi:id/input_skill')
    edit_edu = (By.ID,'com.hub.mentifi:id/action_more')
    bio = (By.ID,'com.hub.mentifi:id/input_bio')
    hobby = (By.ID,'com.hub.mentifi:id/input_hobbies')
    degree = (By.ID,'com.hub.mentifi:id/input_degree')
    major = (By.ID,'com.hub.mentifi:id/input_institution_hint')
    institution = (By.ID,'com.hub.mentifi:id/input_institution')
    pic = (By.ID,'com.hub.mentifi:id/text_change_picture')
    crop_ok = (By.ID,'com.hub.mentifi:id/menu_crop')

#com.hub.mentifi:id/image_profile


    def edit_personal_detail_mentee(self,first,last,prefer,gender,tlp):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        self.find_element(self.option).click()
        time.sleep(2)
        test_parent = self.driver.find_element(By.XPATH, "//*[@class='android.widget.FrameLayout']")
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        test[0].click()
        time.sleep(1)
        self.find_element(self.fname).clear()
        self.find_element(self.fname).send_keys(first)
        self.find_element(self.lname).clear()
        self.find_element(self.lname).send_keys(last)
        self.find_element(self.pname).clear()
        self.find_element(self.pname).send_keys(prefer)
        time.sleep(1)
        test_parent2 = self.driver.find_element(By.ID ,'com.hub.mentifi:id/radio_gender')
        test2 = test_parent2.find_elements(By.CLASS_NAME,'android.widget.RadioButton')
        test2[gender].click()
        time.sleep(1)
        self.find_element(self.phone).clear()
        self.find_element(self.phone).send_keys(tlp)
        time.sleep(1)
        self.find_element(self.pic).click()
        time.sleep(1)
        a = self.driver.find_element(By.ID,'com.asus.gallery:id/fab_root')
        a.click()
        time.sleep(2)
        file_base64 = self.driver.pull_file('/sdcard/Pictures/1526805882240.jpg')
        print(file_base64)
        # b = self.driver.find_element(By.ID, 'com.asus.gallery:id/fab_root')
        # b.click()
        # time.sleep(3)
        #self.find_element(self.crop_ok).click()
        #self.driver.push_file('/path/to/device/foo.bar', 'QXJlIHlvdXIgYmVlcnMgb2theT8=')
        #self.driver.push_file('/sdcard/Pictures/1526805882240.jpg')
        # time.sleep(1)
        #self.find_element(self.save_button).click()
        print('profile edited :'+first+','+last+','+prefer+','+tlp)
#com.asus.gallery:id/gl_root_view
    #com.asus.gallery:id/fab_root
    #[0,0][792,1208]
    #[0,0][800,1216]
    #android.widget.RelativeLayout
    #android.view.View

    def edit_biography_mentee(self, about, skill):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        #self.find_element(self.option).click()
        time.sleep(2)
        self.find_element(self.edit_bio).click()
        time.sleep(1)
        self.find_element(self.about_me).clear()
        self.find_element(self.about_me).send_keys(about)
        self.find_element(self.pro_skill).clear()
        self.find_element(self.pro_skill).send_keys(skill)
        self.find_element(self.save_button).click()
        time.sleep(1)
        self.driver.hide_keyboard()
        time.sleep(1)
        print('profile bio edited :' + about + ',' + skill )

    def edit_education_mentee(self, degree, major):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        time.sleep(1)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/tabs')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
        test[2].click()
        time.sleep(4)
        self.find_element(self.edit_edu).click()
        time.sleep(1)
        self.find_element(self.degree).clear()
        self.find_element(self.degree).send_keys(degree)
        self.find_element(self.major).click()
        self.find_element(self.major).clear()
        self.find_element(self.major).send_keys(major)
        time.sleep(1)
        self.find_element(self.save_button).click()
        # test_parent2 = self.driver.find_element(By.ID, 'com.hub.mentifi:id/recycler_view')
        # test2 = test_parent2.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
        # test2[2].click()


    def edit_biography_mentor(self, about, skill):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        #self.find_element(self.option).click()
        time.sleep(2)
        self.find_element(self.edit_bio).click()
        time.sleep(1)
        self.find_element(self.bio).clear()
        self.find_element(self.bio).send_keys(about)
        self.find_element(self.hobby).clear()
        self.find_element(self.hobby).send_keys(skill)
        time.sleep(1)
        # self.driver.hide_keyboard()
        # time.sleep(1)
        self.find_element(self.save_button).click()
        print('profile bio edited :' + about + ',' + skill )

    def edit_personal_detail_mentor(self,first,last,work,gender,tlp):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        self.find_element(self.option).click()
        time.sleep(2)
        test_parent = self.driver.find_element(By.XPATH, "//*[@class='android.widget.FrameLayout']")
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        test[0].click()
        time.sleep(1)
        self.find_element(self.fname).clear()
        self.find_element(self.fname).send_keys(first)
        self.find_element(self.lname).clear()
        self.find_element(self.lname).send_keys(last)
        self.find_element(self.work).clear()
        self.find_element(self.work).send_keys(work)
        time.sleep(1)
        test_parent2 = self.driver.find_element(By.ID ,'com.hub.mentifi:id/radio_gender')
        test2 = test_parent2.find_elements(By.CLASS_NAME,'android.widget.RadioButton')
        test2[gender].click()
        time.sleep(1)
        self.find_element(self.phone).clear()
        self.find_element(self.phone).send_keys(tlp)
        time.sleep(1)
        self.driver.hide_keyboard()
        time.sleep(1)
        self.find_element(self.save_button).click()
        print('profile edited :'+first+','+last+','+work+','+tlp)


    def edit_education_mentor(self, degree, institution):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        time.sleep(1)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/tabs')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
        test[2].click()
        time.sleep(4)
        self.find_element(self.edit_edu).click()
        time.sleep(1)
        self.find_element(self.degree).clear()
        self.find_element(self.degree).send_keys(degree)
        self.find_element(self.institution).click()
        self.find_element(self.institution).clear()
        self.find_element(self.institution).send_keys(institution)
        time.sleep(1)
        self.find_element(self.save_button).click()