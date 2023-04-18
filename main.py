# This is a sample Python script.
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import json


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_element_wait(wb, xpath):
    cur_element = WebDriverWait(wb, 20, 0.5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, xpath))
    )
    return cur_element


def init_config():
    with open('config.json', 'r', encoding='utf-8') as fp:
        config_data = json.load(fp)
    fp.close()
    return config_data


def get_account_from_config_by_app(app):
    data = init_config()
    for info in data:
        if info['app'] == app:
            return info


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app_info = get_account_from_config_by_app("test")
    driver = webdriver.Chrome()
    driver.get("https://console.firebase.google.com/project/cool-f80ef/notification/compose?hl=zh-cn")
    username = get_element_wait(driver, '//*[@id="identifierId"]')
    username.send_keys(app_info['account'])
    next1 = get_element_wait(driver, '//*[@id="identifierNext"]/div/button')
    next1.click()
    pwd = get_element_wait(driver, '//*[@id="password"]/div[1]/div/div[1]/input')
    pwd.send_keys(app_info['password'])
    next2 = get_element_wait(driver, '//*[@id="passwordNext"]/div/button')
    next2.click()
    push_title = get_element_wait(driver, '//*[@id="cdk-step-content-0-0"]/div/compose-message-step/div/div['
                                          '1]/form/div[1]/input')
    push_title.send_keys('hello')

    push_text = get_element_wait(driver, '//*[@id="cdk-step-content-0-0"]/div/compose-message-step/div/div['
                                         '1]/form/div[2]/textarea')
    push_text.send_keys('hello world')

    push_img = get_element_wait(driver, '//*[@id="cdk-step-content-0-0"]/div/compose-message-step/div/div['
                                        '1]/form/div[3]/div/input')
    push_img.send_keys('https://cdn.kikakeyboard.com/image/2019022154565455.png')

    push_name = get_element_wait(driver, '//*[@id="cdk-step-content-0-0"]/div/compose-message-step/div/div['
                                         '1]/form/div[4]/input')
    push_name.send_keys("one push")

    next3 = get_element_wait(driver, '//*[@id="cdk-step-content-0-0"]/div/button')
    next3.click()

    time.sleep(100)
