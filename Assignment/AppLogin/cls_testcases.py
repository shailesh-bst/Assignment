from appium import webdriver
import unittest
import gametv_download
import HtmlTestRunner


class App(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.desired_cap = config.desired_cap_playstore
        # gametv_download.download_app(cls.desired_cap)
        cls.desired_cap = config.desired_cap_gametv
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=cls.desired_cap)
        cls.driver.implicitly_wait(40)

    def test_launch_app(self):
        self.login_twitter_btn = self.driver.find_element_by_accessibility_id("AuthoriseWithTwitter_593")
        assert self.login_twitter_btn.is_enabled()

    def test_twitter_btn(self):
        self.login_twitter_btn = self.driver.find_element_by_accessibility_id("AuthoriseWithTwitter_593").click()
        self.driver.implicitly_wait(10)
        assert self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view."
            "View[3]/android.view.View[1]/android.view.View[1]/android.widget.EditText").is_displayed()

    def test_login(self):
        username = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view."
            "View[3]/android.view.View[1]/android.view.View[1]/android.widget.EditText")
        username.send_keys("tes1.auto1@gmail.com")
        password = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]"
            "/android.view.View[1]/android.view.View[2]/android.widget.EditText")
        password.send_keys("game@twitter")
        authorize_btn = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]"
            "/android.view.View[2]/android.widget.Button[1]")
        authorize_btn.click()
        assert not self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
        "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[3]"
        "/android.view.View[2]/android.widget.Button[1]")
    
     def test_home_page(self):
         gametv_download.login_app(self.driver)
         self.driver.implicitly_wait(10)
         assert self.driver.find_element_by_xpath(
             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
             "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view."
             "View[3]/android.view.View[1]/android.view.View[1]/android.widget.EditText").is_displayed() is False

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\'))
