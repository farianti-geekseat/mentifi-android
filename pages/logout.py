from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import Page
from appium.webdriver.common.touch_action import TouchAction


import time




class Logout(Page):
    more = (By.ID, 'com.hub.mentifi:id/tab_profile')
    profile = (By.ID, 'com.hub.mentifi:id/nav_profile')
    option = (By.XPATH, "//*[@class='android.support.v7.widget.LinearLayoutCompat']")
    logout = (By.XPATH,"//*[@class='android.widget.LinearLayout' and ./*[@class='android.widget.RelativeLayout' and ./*[@text='Logout']]]")

    def logout(self,alias):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        self.find_element(self.option).click()
        time.sleep(2)
        test_parent = self.driver.find_element(By.XPATH,"//*[@class='android.widget.FrameLayout']")
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        test[alias].click()
        print('Successfully Logout')
        #self.find_element(self.logout).click()
        # test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        # for i in test:
        #     j = i.class_name
        #     print(j)
#[597,360][1028,414]
#android.widget.LinearLayout

        #self.driver.find_elements_by_accessibility_id('logout')