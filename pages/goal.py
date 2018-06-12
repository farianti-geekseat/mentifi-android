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
    add_goal=(By.CLASS_NAME,'android.widget.FloatingActionButton')
    edit_button = (By.XPATH,"//*[@id='ib_action_more' and (./preceding-sibling::* | ./following-sibling::*)[@text='hard']]")
    set_goal = (By.XPATH,"//*[@id='fab_new_goal']")
    probability = (By.ID,'com.hub.mentifi:id/spinner_probability')
    ok_button = (By.XPATH,"//*[@text='OK']")
    prob = (By.XPATH,"//*[@text='Impossible']")
    save = (By.XPATH,"//*[@text='Save']")
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
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.set_goal))
        except TimeoutException:
            print("element not ready")

        self.find_element(self.set_goal).clear()
        self.find_element(self.set_goal).send_keys(title)
        self.find_element(self.probability).click()
        # test_parent = self.driver.find_element(By.ID,'com.hub.mentifi:id/spinner_probability')
        # tests = test_parent.find_elements(By.XPATH,'android.widget.ListView')
        # print(tests)
        a = self.find_element(By.ID,'android:id/text1')
        print(a)
        #[693,1013][800,1136]
        self.find_element(self.save).click()
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
        print(self.add_goal)
        self.driver.tap((693,1013),(800,1136),1)
        #self.find_element(self.add_goal).click()
        # time.sleep(2)
        #
        # self.find_element(self.set_goal).send_keys(title)
        # self.find_element(self.probability).click()
        # time.sleep(5)
        # test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/spinner_probability')
        # tests = test_parent.find_elements(By.XPATH,'android.widget.TextView')
        # tests[alias].click()