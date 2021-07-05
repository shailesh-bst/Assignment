from selenium import webdriver
import time
import config


def get_temp_site1(loc_list):
    ''' TO get the temperature openweather webelements '''
    try:
        # Final list of temperatures of cities to be returned
        temperature_list = []
        driver = webdriver.Chrome(executable_path="C:\Driver\chrome_driver\chromedriver.exe")
        driver.get("https://weather.com/")
        if driver.find_element_by_id("LocationSearch_input").is_displayed():
            config.logger.info("Website is up and working")
            driver.maximize_window()

            time.sleep(3)
            # Calculating temperatures
            for i in range(0, len(loc_list)):
                input_city = driver.find_element_by_id("LocationSearch_input")
                input_city.click()
                time.sleep(2)
                input_city.send_keys(loc_list[i])
                time.sleep(3)
                driver.find_element_by_xpath("//*[@id='LocationSearch_listbox-0']").click()
                time.sleep(3)
                temp = driver.find_element_by_xpath(
                    "//*[@id='WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034']/div/section/div/div[2]/div[1]/span").text
                temperature_list.append(int(temp[:2]))
                driver.back()
                time.sleep(2)
                config.logger.info(str(i) + " temperature is captured")

            if len(temperature_list) > 0:
                return temperature_list
            else:
                return None

        else:
            config.logger.info("Website down")
            return None

    except Exception as e:
        print(e)

    finally:
        driver.quit()
