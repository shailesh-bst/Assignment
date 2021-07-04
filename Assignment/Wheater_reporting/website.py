from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_temp_site1(loc_list):
    ''' TO get the temperature openweather webelements '''
    try:
        temperature_list = []
        driver = webdriver.Chrome(executable_path="C:\Driver\chrome_driver\chromedriver.exe")
        driver.get("https://weather.com/")
        driver.maximize_window()
        time.sleep(3)
        for i in range(0, len(loc_list)):
            input_city = driver.find_element_by_id("LocationSearch_input")
            input_city.click()
            time.sleep(3)
            input_city.send_keys(loc_list[i])
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id='LocationSearch_listbox-0']").click()
            time.sleep(3)
            temp = driver.find_element_by_xpath("//*[@id='WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034']/div/section/div/div[2]/div[1]/span").text
            temperature_list.append(int(temp[:2]))
            driver.back()
            time.sleep(2)

        return temperature_list

    except Exception as e:
        print(e)

    finally:
        driver.quit()