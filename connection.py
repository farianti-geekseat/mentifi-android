from appium import webdriver

class Connection():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'Meizu M6'
    desired_caps['udid'] = '711H2BSH223RU'
    desired_caps['appPackage'] = "com.hub.mentifi"
    desired_caps['appActivity'] = ".ui.login.LoginActivity"
    desired_caps['noReset'] = False
    desired_caps['automationName'] = 'uiautomator2'
    #desired_caps['appiumVersion'] = '1.6.5'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)