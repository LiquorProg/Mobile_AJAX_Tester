import time
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def appium_driver():
    # Настройки для подключения к Appium серверу
    options = UiAutomator2Options()
    options.platformVersion = '12'
    options.udid = 'emulator-5554'

    # Создание драйвера Appium
    driver = webdriver.Remote('http://26.177.237.19:4723', options=options)

    # # Выполнить авторизацию перед выполнением теста
    # login(driver)

    yield driver  # Возвращает драйвер тесту

    # Завершить сеанс после выполнения теста
    driver.quit()


# Параметры для тестов
@pytest.mark.parametrize("username, password, expected_result", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", "Add Hub"),  # Позитивный тест
    ("qa.ajax.app.automation@gmail.com", "fdgdfgdfg", "Wrong login or password"),  # Негативный тест
    ("fdgdfdfgdfghl", "fgdfgdfgdf", "Invalid email format"),  # Негативный тест
])
def test_user_application_login(username, password, expected_result, appium_driver):
    # wait = WebDriverWait(appium_driver, 10)  # Максимальное время ожидания в секундах
    #
    # application = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@text="Ajax"]')))

    # Открытие приложения
    application = appium_driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Ajax"]')
    application.click()

    # Нажатия кнопки для перехода на страницу авторизации
    time.sleep(1)
    first_login_button = appium_driver.find_elements(by=AppiumBy.XPATH, value='//*[@class="android.widget.Button"]')
    first_login_button[0].click()

    # Ввод логина и пароля в поля авторизации
    time.sleep(1)
    text_fields = appium_driver.find_elements(by=AppiumBy.XPATH, value='//*[@class="android.widget.EditText"]')
    if text_fields[0].text:
        text_fields[0].clear()
    text_fields[0].send_keys(username)
    text_fields[1].send_keys(password)

    # Нажатия кнопки логина
    time.sleep(1)
    second_login_button = appium_driver.find_elements(by=AppiumBy.XPATH, value='//*[@class="android.widget.Button"]')
    second_login_button[1].click()

    time.sleep(3)
    result_message = appium_driver.find_elements(by=AppiumBy.XPATH, value='//*[@resource-id="com.ajaxsystems:id/text"]')

    if result_message[0].text == "Add Hub":
        print(result_message[0].text)
        # Успешный сценарий
        assert result_message[0].text == expected_result

        menu_button = appium_driver.find_element(by=AppiumBy.XPATH,
                                                 value='//*[@resource-id="com.ajaxsystems:id/menuDrawer"]')
        menu_button.click()

        setting_button = appium_driver.find_element(by=AppiumBy.XPATH,
                                                    value='//*[@resource-id="com.ajaxsystems:id/settings"]')
        setting_button.click()

        sign_out_button = appium_driver.find_element(by=AppiumBy.XPATH,
                                                     value='//*[@bounds="[0,1728][1080,1917]"]')
        sign_out_button.click()

        # Переход на домашнюю страницу
        appium_driver.press_keycode(3)

    else:
        # Негативный сценарий
        time.sleep(2)
        error_message = appium_driver.find_element(by=AppiumBy.XPATH,
                                                   value='//*[@resource-id="com.ajaxsystems:id/snackbar_text"]')
        assert error_message.text == expected_result

        time.sleep(2)
        back_button = appium_driver.find_element(by=AppiumBy.XPATH,
                                                 value='//*[@resource-id="com.ajaxsystems:id/back"]')
        back_button.click()

        # Переход на домашнюю страницу
        appium_driver.press_keycode(3)