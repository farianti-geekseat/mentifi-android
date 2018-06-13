from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages import Page

import time



class Goal(Page):
    goaltitle = (By.XPATH,"//*[@id='GoalTitle']")
    progress = (By.XPATH,"//*[@id='progressText']")
    chart = (By.XPATH,"//*[@id='chart']")
    goal=(By.ID,'com.hub.mentifi:id/tab_goals')
    add_goal=(By.ID,'com.hub.mentifi:id/fab_new_goal')
    edit_button = (By.XPATH,"//*[@id='ib_action_more' and (./preceding-sibling::* | ./following-sibling::*)[@text='hard']]")
    set_goal = (By.ID,'com.hub.mentifi:id/input_goal')
    probability = (By.ID,'com.hub.mentifi:id/spinner_probability')
    ok_button = (By.XPATH,"//*[@text='OK']")
    prob = (By.XPATH,"//*[@text='Impossible']")
    save = (By.ID,'com.hub.mentifi:id/btn_save')
    tag = (By.ID,'com.hub.mentifi:id/tags_edit')
    tag_todo = (By.ID,'com.hub.mentifi:id/recycler_view_task')
    done = (By.ID,'com.hub.mentifi:id/done')
    cancel = (By.ID,'com.hub.mentifi:id/btn_cancel')
    determine = (By.ID,'com.hub.mentifi:id/determinateBar')
    def click_goal(self):
        self.find_element(self.goal).click()

    def check_goal(self):
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/recycler_view_goal')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            j = i.text
            print(j)
#//*[@class='android.widget.FrameLayout']
    def edit_goal(self,alias,title):
        edit_parent = self.driver.find_element(By.ID,'com.hub.mentifi:id/recycler_view_goal')
        edit = edit_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        edit[alias].click()
        time.sleep(2)
        print('button clicked')
        test_parent = self.driver.find_element(By.XPATH, "//*[@class='android.widget.FrameLayout' and ./*[@class='android.widget.ListView']]")
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        test[0].click()
        print('edit clicked')
        self.find_element(self.set_goal).clear()
        self.find_element(self.set_goal).send_keys(title)
        self.find_element(self.probability).click()
        time.sleep(2)
        self.find_element(self.cancel).click()
        #[693,1013][800,1136]
        self.find_element(self.save).click()
        time.sleep(2)
        self.find_element(self.tag).click()
        time.sleep(2)
        test_tag_parent = self.find_element(self.tag_todo)
        test_tag = test_tag_parent.find_elements(By.CLASS_NAME, 'android.widget.CheckBox')
        test_tag[alias].click()
        time.sleep(2)
        self.find_element(self.done).click()
        time.sleep(2)
        print('successfully add tag')
        self.find_element(self.save).click()
        print('successfully edit goal')
#By.XPATH,"//*[@class='android.widget.FrameLayout']"
#android.widget.ImageButton
#//*[@id='fab_new_goal']
#com.hub.mentifi:id/fab_new_goal
    def remove_goal(self, alias):
        edit_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/recycler_view_goal')
        edit = edit_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        edit[alias].click()
        time.sleep(2)
        print('button clicked')
        test_parent = self.driver.find_element(By.XPATH,"//*[@class='android.widget.FrameLayout' and ./*[@class='android.widget.ListView']]")
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        test[2].click()
        self.find_element(self.ok_button).click()
        print('goal removed')


    def add_goal(self,title,alias):
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/mainContainer')
        tests = test_parent.find_element(By.ID, 'com.hub.mentifi:id/fab_new_goal')
        tests.click()
        time.sleep(2)
        self.find_element(self.set_goal).send_keys(title)
        self.find_element(self.probability).click()
        time.sleep(2)
        self.find_element(self.cancel).click()
        time.sleep(1)
        self.find_element(self.tag).click()
        time.sleep(1)
        test_tag_parent = self.find_element(self.tag_todo)
        test_tag = test_tag_parent.find_elements(By.CLASS_NAME,'android.widget.CheckBox')
        test_tag[alias].click()
        time.sleep(1)
        self.find_element(self.done).click()
        print('successfully add tag')
        self.find_element(self.save).click()
        print('successfully add goal')
        # self.find_element(self.probability).click()
        # time.sleep(2)
        # test_parent = self.driver.find_element(By.XPATH,"//*[@class='android.widget.FrameLayout' and ./*[@id='spinner_probability']]")
        # #self.driver.tap([(42,652),(758,737)],1)
        # test = self.driver.find_elements(By.ID, 'android:id/text1')
        # print(test)

#android.widget.TextView
#//*[@class='android.widget.FrameLayout' and ./*[@id='spinner_probability']]
#//*[@class='android.widget.FrameLayout']
#android:id/text1

# [42,312][758,397]
# [42,397][758,482]
# [42,482][758,567]
# [42,567][758,652]
# [42,652][758,737]