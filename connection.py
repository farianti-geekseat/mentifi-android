from appium import webdriver

class Connection():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0'
    desired_caps['deviceName'] = 'Samsung'
    desired_caps['udid'] = '420006e8ec161300'
    desired_caps['appPackage'] = "com.hub.mentifi"
    desired_caps['appActivity'] = ".activities.SplashActivity"
    desired_caps['noReset'] = False
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['appiumVersion'] = '1.6.5'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)