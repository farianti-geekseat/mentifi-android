from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page
from connection import Connection
import time

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
    major = (By.ID,'com.hub.mentifi:id/input_institution')
    institution = (By.ID,'com.hub.mentifi:id/input_institution')
    pic = (By.ID,'com.hub.mentifi:id/text_change_picture')
    crop_ok = (By.ID,'com.hub.mentifi:id/menu_crop')
    allow = (By.ID,'com.android.packageinstaller:id/permission_allow_button')
    job_title = (By.ID,'com.hub.mentifi:id/input_job_position')
    employer = (By.ID,'com.hub.mentifi:id/input_company')
    start_date = (By.ID,'com.hub.mentifi:id/input_start_date')
    end_date = (By.ID,'com.hub.mentifi:id/input_end_date')
    upload_file = (By.ID,'com.hub.mentifi:id/input_upload_file')
    area = (By.ID,'com.hub.mentifi:id/tags_edit')
    other = (By.ID,'com.hub.mentifi:id/input_other')
    edit_preferences = (By.ID,'com.hub.mentifi:id/action_edit')

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
        time.sleep(3)
        self.driver.hide_keyboard()
        test_parent2 = self.driver.find_element(By.ID ,'com.hub.mentifi:id/radio_gender')
        test2 = test_parent2.find_elements(By.CLASS_NAME,'android.widget.RadioButton')
        test2[gender].click()
        time.sleep(1)
        self.find_element(self.phone).clear()
        self.find_element(self.phone).send_keys(tlp)
        time.sleep(2)
        # self.find_element(self.pic).click()
        # self.find_element(self.allow).click()
        # self.find_element(self.pic).click()
        # time.sleep(2)
        # # self.driver.pull_file('/root/Internal storage/DCIM/Camera/20180705_090252.jpg')
        # #self.driver.tap([(0,190),(520,300)])
        # self.swipe_to_bottom()
        # time.sleep(3)
        #a = self.driver.find_element_by_id('com.sec.android.gallery3d:id/main_relativelayout')
        #self.driver.switch_to_frame(self.driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and ./*[@id='decor_content_parent']]"))
        #self.driver.tap([(395, 347), (684, 636)], 2)
        # test_parent4 = self.driver.find_element(By.ID, 'com.sec.android.gallery3d:id/tabHost')
        # test4 = test_parent4.find_elements(By.CLASS_NAME,'android.widget.LinearLayout')
        # test4[0].click()
        # time.sleep(3)
        #self.driver.start_activity("com.sec.android.gallery3d","app.GalleryActivity")
        # time.sleep(1)
        # self.driver.tap([(395, 347), (792,1208)], 2)
        # self.driver.start_activity("com.hub.mentifi",
        #                            "com.hub.mentifi.ui.splash.SplashActivity")
        # self.driver.switch_to_window('com.sec.samsung.gallery.glview.composeView.PositionControllerBase$ThumbObject')
        #self.driver.start_activity("com.sec.android.gallery3d",'id/gl_root_view')
        # time.sleep(2)
        # b = self.driver.find_element(By.ID, 'com.asus.gallery:id/fab_root')
        #print(b)
        #b.click()
        # time.sleep(3)
        # time.sleep(1)
        self.find_element(self.save_button).click()
        print('profile edited :'+first+','+last+','+prefer+','+tlp)
#com.sec.android.gallery3d:id/gl_root_view
    #com.asus.gallery:id/fab_root
    #[395,347][684,636]
    #[0,0][792,1208]
    #[0,0][800,1216]

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

    def edit_education_mentee(self, degree, major,grade,mode):
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
        test_parent2 = self.driver.find_element(By.ID, 'com.hub.mentifi:id/input_grade')
        test2 = test_parent2.find_elements(By.CLASS_NAME, 'android.widget.RadioButton')
        test2[grade].click()
        test_parent3 = self.driver.find_element(By.ID, 'com.hub.mentifi:id/input_mode')
        test3 = test_parent3.find_elements(By.CLASS_NAME, 'android.widget.RadioButton')
        test3[mode].click()
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
        time.sleep(2)
        # self.find_element(self.pic).click()
        # self.find_element(self.allow).click()
        # self.find_element(self.pic).click()
        # time.sleep(1)
        self.find_element(self.save_button).click()
        print('profile edited :'+first+','+last+','+work+','+tlp)


    def edit_education_mentor(self, degree, institution,start_date,end_date):
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
        self.find_element(self.start_date).clear()
        self.find_element(self.start_date).send_keys(start_date)
        self.find_element(self.end_date).clear()
        self.find_element(self.end_date).send_keys(end_date)
        self.find_element(self.save_button).click()

    def edit_current_experience_mentee(self,job,employer,start_date,attach):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        time.sleep(1)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/tabs')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
        test[3].click()
        time.sleep(4)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/recycler_view')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        test[0].click()
        time.sleep(1)
        # self.find_element(self.job_title).clear()
        # self.find_element(self.job_title).send_keys(job)
        # self.find_element(self.employer).clear()
        # self.find_element(self.employer).send_keys(employer)
        # self.find_element(self.start_date).clear()
        # self.find_element(self.start_date).send_keys(start_date)
        # self.driver.hide_keyboard()
        # time.sleep(1)
        self.find_element(self.upload_file).click()
        self.find_element(self.allow).click()
        self.find_element(self.upload_file).click()
        time.sleep(3)
        # test_parent3 = self.driver.find_element(By.ID, 'com.android.documentsui:id/toolbar')
        # test3 = test_parent3.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        # test3[0].click()
        # time.sleep(1)
        # test_parent4 = self.driver.find_element(By.ID, 'com.android.documentsui:id/toolbar')
        # test4 = test_parent4.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        # test4[1].click()
        # print('list1')
        # time.sleep(1)
        # test_parent5 = self.driver.find_element(By.ID, 'com.android.documentsui:id/dir_list')
        # test5 = test_parent5.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        # test5[3].click()
        # print('list2')
        # time.sleep(1)
        # test_parent5 = self.driver.find_element(By.ID, 'com.android.documentsui:id/dir_list')
        # test5 = test_parent5.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        # test5[5].click()
        #com.android.documentsui:id/dir_list
        test_parent = self.driver.find_element(By.ID, 'com.android.documentsui:id/dir_list')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.RelativeLayout')
        test[attach].click()
        self.find_element(self.save_button).click()
        print('previous experience mentee edited')


    def edit_previous_experience_mentee(self,job,employer,start_date,end_date):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        time.sleep(1)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/tabs')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
        test[3].click()
        time.sleep(4)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/recycler_view')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        test[1].click()
        time.sleep(1)
        self.find_element(self.job_title).clear()
        self.find_element(self.job_title).send_keys(job)
        self.find_element(self.employer).clear()
        self.find_element(self.employer).send_keys(employer)
        self.find_element(self.start_date).clear()
        self.find_element(self.start_date).send_keys(start_date)
        self.find_element(self.end_date).clear()
        self.find_element(self.end_date).send_keys(end_date)
        self.driver.hide_keyboard()
        self.find_element(self.save_button).click()
        print('current experience mentee edited')

    def edit_current_experience_mentor(self, job, employer,area, start_date):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        time.sleep(1)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/tabs')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
        test[3].click()
        time.sleep(4)
        test_parent2 = self.driver.find_element(By.ID, 'com.hub.mentifi:id/recycler_view')
        test2 = test_parent2.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        test2[0].click()
        time.sleep(1)
        self.find_element(self.job_title).clear()
        self.find_element(self.job_title).send_keys(job)
        self.find_element(self.employer).clear()
        self.find_element(self.employer).send_keys(employer)
        self.find_element(self.area).click()
        self.find_element(self.area).send_keys(area)
        time.sleep(3)
        self.tap_first_result_auto_complete(self.find_element(self.area))
        # test3 = self.driver.find_element(By.XPATH, "//*[@class='android.widget.FrameLayout' and ./*[@class='android.widget.ListView']]")
        # print(test3)
        #test3[0].click()
        time.sleep(1)
        self.find_element(self.start_date).clear()
        self.find_element(self.start_date).send_keys(start_date)
        # self.driver.hide_keyboard()
        time.sleep(1)
        # self.find_element(self.upload_file).click()
        self.find_element(self.save_button).click()
        print('previous experience mentor edited')
#android.widget.RelativeLayout
#//*[@class='android.widget.ListView']
#com.hub.mentifi:id/text_title
    #//*[@class='android.widget.FrameLayout' and ./*[@class='android.widget.ListView']]
    def edit_previous_experience_mentor(self, job, employer, start_date, end_date):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        time.sleep(1)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/tabs')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
        test[3].click()
        time.sleep(4)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/recycler_view')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        test[1].click()
        time.sleep(1)
        self.find_element(self.job_title).clear()
        self.find_element(self.job_title).send_keys(job)
        self.find_element(self.employer).clear()
        self.find_element(self.employer).send_keys(employer)
        self.find_element(self.start_date).clear()
        self.find_element(self.start_date).send_keys(start_date)
        self.find_element(self.end_date).clear()
        self.find_element(self.end_date).send_keys(end_date)
        self.driver.hide_keyboard()
        self.find_element(self.save_button).click()
        print('current experience mentor edited')

    def edit_non_work_experience_mentor(self, alias1, alias2):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        time.sleep(1)
        self.driver.swipe(65,1533,65,1187)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/tabs')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
        test[3].click()
        time.sleep(3)
        test_parent2 = self.driver.find_element(By.ID, 'com.hub.mentifi:id/linear_non_formal')
        test2 = test_parent2.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        # print(test2)
        test2[0].click()
        time.sleep(1)
        test3 = self.driver.find_elements(By.CLASS_NAME, 'android.widget.CheckBox')
        test3[alias1].click()
        test3[alias2].click()
        self.find_element(self.save_button).click()
        print('current experience mentor edited')
        #[65,1533][387,1574]
        #[65, 1187][246, 1228]

    def edit_mentor_preference(self,area,prefer):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        time.sleep(1)
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/tabs')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')
        test[4].click()
        time.sleep(2)
        self.find_element(self.edit_preferences).click()
        time.sleep(1)
        self.find_element(self.area).click()
        self.find_element(self.area).send_keys(area)
        time.sleep(2)
        # test_parent = self.driver.find_element(By.XPATH,"//*[@class='android.widget.ListView']")
        # test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        self.tap_first_result_auto_complete(self.find_element(self.area))
        # test_parent2 = self.driver.find_element(By.ID, 'com.hub.mentifi:id/input_grade')
        # test2 = test_parent2.find_elements(By.CLASS_NAME, 'android.widget.RadioButton')
        # test2[prefer].click()
        time.sleep(1)
        test_parent2 = self.driver.find_element(By.ID, 'com.hub.mentifi:id/input_grade')
        test2 = test_parent2.find_elements(By.CLASS_NAME, 'android.widget.RadioButton')
        test2[prefer].click()
        time.sleep(1)
        #self.find_element(self.employer).clear()
        #self.driver.hide_keyboard()
        self.find_element(self.save_button).click()
        print('current experience mentee edited')