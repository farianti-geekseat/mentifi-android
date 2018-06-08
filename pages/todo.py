from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from pages import Page

import time



class ToDo(Page):
    ongoing =(By.XPATH,"//*[@class='android.support.v7.app.ActionBar$Tab' and ./*[@text='Ongoing']]")
    complete =(By.XPATH,"//*[@class='android.support.v7.app.ActionBar$Tab' and ./*[@text='Complete']]")
    taskname =(By.XPATH,"//*[@text='testing 2']")
    todo =(By.ID,'com.hub.mentifi:id/tab_tasks')
    save =(By.ID,'com.hub.mentifi:id/btn_save')
    set_title = (By.ID,'com.hub.mentifi:id/input_task')
    priority = (By.ID,'com.hub.mentifi:id/spinner_priority')
    assign = (By.ID,'com.hub.mentifi:id/spinner_assign_to')
    tag_goal = (By.ID,'com.hub.mentifi:id/tags_edit')

    def click_todo(self):
        self.find_element(self.todo).click()

    def click_ongoing(self):
        self.find_element(self.ongoing).click()
        print("List todo ongoing: ")
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            j = i.text
            print(j)


    def click_complete(self):
        self.find_element(self.complete).click()
        print("List todo complete : ")
        test_parent = self.driver.find_element(By.ID, 'com.hub.mentifi:id/viewpager')
        test = test_parent.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        for i in test:
            k = i.text
            print(k)

    def edit_todo(self,alias,title):
        click_todo_parent = self.driver.find_element(By.ID,'com.hub.mentifi:id/list')
        click_todo = click_todo_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        click_todo[alias].click()
        time.sleep(2)
        edit_parent = self.driver.find_element(By.XPATH,"//*[@class='android.widget.FrameLayout' and ./*[@class='android.widget.ListView']]")
        #print(edit_parent.text)
        edit = edit_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        edit[0].click()
        print('edit todo')
        self.find_element(self.set_title).clear()
        self.find_element(self.set_title).send_keys(title)
        self.find_element(self.priority).click()
        time.sleep(2)
        test_parent = self.driver.find_element(By.XPATH,"//*[@class='android.widget.FrameLayout'and ./*[@class='android.widget.ListView']]")
        tests = test_parent.find_elements(By.CLASS_NAME,'android.widget.CheckedTextView')
        time.sleep(1)
        tests[2].click()
        self.find_element(self.assign).click()
        time.sleep(1)
        todo_parent = self.driver.find_element(By.XPATH,"//*[@class='android.widget.FrameLayout']")
        todo_assign = todo_parent.find_elements(By.CLASS_NAME,'android.widget.CheckedTextView')
        todo_assign[2].click()
        self.find_element(self.tag_goal).click()
        self.find_element(self.tag_goal).send_keys('set')
        time.sleep(2)

        # TouchAction().tap(element=None,x=[60,334],y=[180,360],int=1)
        #Page.tap_first_result_auto_complete(self.find_element(self.tag_goal))
        # todo_parent2 = self.driver.find_element(By.XPATH,"//*[@class='android.widget.ListView']]")
        # todo_assign2 = todo_parent2.find_elements(By.CLASS_NAME,'android.widget.TextView')
        # for i in todo_assign2:
        #     k = i.text
        #     print(k)
        #todo_assign2[1].click()
        #self.find_element(self.save).click()

#com.hub.mentifi:id/text_title
    #//*[@class='android.widget.ListView']
    #android.widget.RelativeLayout
    #[60,334][180,360], [60,470][161,496]
    #[60,402][180,428]


    def delete_todo(self,alias,title):
        click_todo_parent = self.driver.find_element(By.ID,'com.hub.mentifi:id/list')
        click_todo = click_todo_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        click_todo[alias].click()
        time.sleep(2)
        edit_parent = self.driver.find_element(By.XPATH,"//*[@class='android.widget.FrameLayout' and ./*[@class='android.widget.ListView']]")
        #print(edit_parent.text)
        edit = edit_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        edit[2].click()
        print('delete todo')

    def complete_todo(self,alias,title):
        click_todo_parent = self.driver.find_element(By.ID,'com.hub.mentifi:id/list')
        click_todo = click_todo_parent.find_elements(By.CLASS_NAME, 'android.widget.ImageButton')
        click_todo[alias].click()
        time.sleep(2)
        edit_parent = self.driver.find_element(By.XPATH,"//*[@class='android.widget.FrameLayout' and ./*[@class='android.widget.ListView']]")
        #print(edit_parent.text)
        edit = edit_parent.find_elements(By.CLASS_NAME, 'android.widget.LinearLayout')
        edit[1].click()
        print('mark as complete todo')