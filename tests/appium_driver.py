from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_appium_driver():
    # Настройки для подключения к Appium серверу
    options = UiAutomator2Options()
    options.platformVersion = '12'
    options.udid = 'emulator-5554'

    # Создание драйвера Appium
    driver = webdriver.Remote('http://26.177.237.19:4723', options=options)
    return driver