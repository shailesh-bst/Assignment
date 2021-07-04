from appium import webdriver
import unittest
import config
import gametv_download
import HtmlTestRunner
unittest.TestLoader.sortTestMethodsUsing = None


class App(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.desired_cap = config.desired_cap_playstore
        gametv_download.download_app(cls.desired_cap)
        cls.desired_cap = config.desired_cap_gametv
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=cls.desired_cap)
        cls.driver.implicitly_wait(40)

    def test_1_launch_app(self):
        self.login_twitter_btn = self.driver.find_element_by_accessibility_id("AuthoriseWithTwitter_593")
        assert self.login_twitter_btn.is_enabled()

    def test_2_twitter_btn(self):
        self.login_twitter_btn = self.driver.find_element_by_accessibility_id("AuthoriseWithTwitter_593").click()
        self.driver.implicitly_wait(10)
        assert self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view."
            "View[3]/android.view.View[1]/android.view.View[1]/android.widget.EditText").is_displayed()

    def test_3_login(self):
        result = gametv_download.login_app(self.driver)
        assert result == "Successful"

    def test_4_home_page(self):
        self.driver.implicitly_wait(10)
        # As I am getting the page to verify OTP send to credentials
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\'))
