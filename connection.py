from appium import webdriver

class Connection():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'SM-J730G'
    desired_caps['udid'] = '520002bd4abf3541'
    desired_caps['appPackage'] = "com.hub.mentifi"
    desired_caps['appActivity'] = "com.hub.mentifi.ui.splash.SplashActivity"
    desired_caps['noReset'] = False
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['appiumVersion'] = '1.6.5'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    #EBOKCX210776
    #K016
    #5.0

    #711H2BSH223RU
    #Meizu 6
    #7.0

    #520002bd4abf3541
    #SM-J730G
    #7.0
