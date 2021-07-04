from appium import webdriver


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


def download_app(desired_cap):
    try:
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_cap)
        driver.implicitly_wait(15)
        txt_search = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView")
        txt_search.click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText").send_keys(
            "game.tv")
        driver.keyevent(66)
        driver.implicitly_wait(10)
        open_or_install_btn = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget."
            "FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget."
            "FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/"
            "android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view."
            "ViewGroup/android.widget.Button")
        if open_or_install_btn.text == "Install":
            open_or_install_btn.click()
            driver.implicitly_wait(120)
            open_btn = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android."
                "widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget"
                ".FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android."
                "widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget."
                "LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/"
                "android.view.ViewGroup/android.widget.Button")
            if open_btn.is_enabled():
                driver.quit()
            else:
                print("App still not installed")
        else:
            print("App Already installed")
            driver.quit()
    except Exception as e:
        print(e)


def launch_login(dc):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=dc)
    driver.implicitly_wait(40)
    twitter_btn = driver.find_element_by_accessibility_id("AuthoriseWithTwitter_593")
    assert twitter_btn.is_displayed()
    twitter_btn.click()
    username = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
        "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view."
        "View[3]/android.view.View[1]/android.view.View[1]/android.widget.EditText")
    username.send_keys("tes1.auto1@gmail.com")
    password = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
        "android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]"
        "/android.view.View[1]/android.view.View[2]/android.widget.EditText")
    password.send_keys("game@twitter")
    authorize_btn = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
        "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]"
        "/android.view.View[2]/android.widget.Button[1]")
    assert authorize_btn.click()
    authorize_btn.click()
    driver.quit()


def login_app(driver):
    username = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
        "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view."
        "View[3]/android.view.View[1]/android.view.View[1]/android.widget.EditText")
    username.send_keys("tes1.auto1@gmail.com")
    password = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
        "android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]"
        "/android.view.View[1]/android.view.View[2]/android.widget.EditText")
    password.send_keys("game@twitter")
    authorize_btn = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
        "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]"
        "/android.view.View[2]/android.widget.Button[1]")
    authorize_btn.click()