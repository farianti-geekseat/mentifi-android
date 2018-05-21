from appium import webdriver

class Connection():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0'
    desired_caps['deviceName'] = 'K016'
    desired_caps['udid'] = 'EBOKCX210776'
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