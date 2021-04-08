from  appium  import  webdriver

class  Driver :
    def  __init__ ( self, **kwargs ):
        self.android_device = {}
        #android_device["platformVersion"] = "11"
        self.android_device["platformName"] = "Android"
        self.android_device["fullReset"] = False
        self.android_device["noReset"] = True
        self.android_device["deviceName"] = "emulator-5554"
        self.android_device["app"] = "/Users/qubilearnd/Work/apks/Calculator.apk"
    
        # set device properties if they are given as kwargs
        for key, value in kwargs.items():
            self.android_device[str(key)] = value
            print(str(key) + " changed to " + value)

        self.instance  =  webdriver.Remote("http://localhost:4723/wd/hub", self.android_device)
