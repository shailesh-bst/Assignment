from appium import webdriver


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

