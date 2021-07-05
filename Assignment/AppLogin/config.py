import logging

logging.basicConfig(filename="..\\logger.log", level=logging.DEBUG, filemode='w')
logger = logging.getLogger()

desired_cap_playstore = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "com.android.vending",
    "appActivity": "com.google.android.finsky.activities.MainActivity",
    "appWaitDuration": 40000
}


desired_cap_gametv = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "tv.game",
    "appActivity": "tv.game.MainActivity",
    "appWaitDuration": 40000
}
