import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

id_of_div = [element.get_attribute("id") for element in driver.find_elements(By.CSS_SELECTOR, "#store div")]

time_on = True
time_out = time.time() + 5
while time_on:
    try:
        cookie.click()
        if time.time() > time_out:
            life_line = driver.find_elements(By.CSS_SELECTOR, "#store div b")
            life_prices = []
            try:
                for life in life_line:
                    life_price = life.text.split("-")[1]
                    life_prices.append(int(life_price.strip(" ").replace(",", "")))
            except IndexError:
                pass
            coupon = int(driver.find_element(By.ID, "money").text.replace(",", ""))
            lives_less_than_coupon = [x for x in life_prices if x < coupon]
            print(lives_less_than_coupon)
            if not lives_less_than_coupon:
                pass
            else:
                price_index = life_prices.index(max(lives_less_than_coupon))
                print(price_index)
                available_lifelines = driver.find_elements(By.CSS_SELECTOR, "#store div")
                available_lifelines[price_index].click()
            time_out += 5
        if time.time() > time.time() + 60*5:
            time_on = False
            click_per_sec = driver.find_element(By.XPATH, '//*[@id="cps"]').text.split(":")[1]
            print(click_per_sec.strip(" "))

    except StaleElementReferenceException as e:
        pass










#print(life_prices)



