from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page


import time



class Switch_Account(Page):
    more = (By.ID, 'com.hub.mentifi:id/tab_profile')
    profile = (By.ID, 'com.hub.mentifi:id/nav_profile')
    option = (By.XPATH, "//*[@class='android.support.v7.widget.LinearLayoutCompat']")

    def switch_account(self,alias):
        self.find_element(self.more).click()
        self.find_element(self.profile).click()
        self.find_element(self.option).click()
        time.sleep(2)
        test_parent = self.driver.find_element(By.XPATH, "//*[@class='android.widget.FrameLayout']")
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        test[1].click()
        time.sleep(3)
        profile_parent = self.driver.find_element(By.XPATH,"//*[@class='android.support.v7.widget.RecyclerView']")
        profiles = profile_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        profiles[alias].click()



        #//*[@id='list']