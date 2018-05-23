from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page import Page

class Feature(Page):

    network = (By.ID, "")
    project = (By.ID, "")
    profile_picture = (By.ID, "")
    header = (By.ID, "")
    arrow_nav = (By.ID, "")
    cancel = (By.ID, "")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def tap_network(self):
        pass

    def tap_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.project))
            self.find_element(self.project).click()
        except TimeoutException:
            print("Project module not found")

    def tap_header(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.profile_picture))
            self.find_element(self.profile_picture).click()
        except TimeoutException:
            print("element not ready")

    def tap_arrow_nav(self):
        pass

    def tap_cancel(self):
        pass



''' alternative locator '''

# au.geekseat.com.hub3candroid:id/sideProject
# au.geekseat.com.hub3candroid:id/imageProject
# au.geekseat.com.hub3candroid:id/sideNavBusiness
# au.geekseat.com.hub3candroid:id/imageBusinessNetwork