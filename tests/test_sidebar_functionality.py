import pytest

from config import LOGIN, PASSWORD
from selenium.webdriver.common.by import By
from logging_in_file import write_in_log_info
from appium_driver import create_appium_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login(driver):
    write_in_log_info(f"Выполняется вход в аккаунт Ajax Systems")
    try:
        wait = WebDriverWait(driver, 5)  # Максимальное время ожидания в секундах

        # Открытие приложения
        driver.press_keycode(3)
        application = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@text="Ajax"]')))
        application.click()

        # Нажатия кнопки для перехода на страницу авторизации
        first_login_button = wait.until(ec.presence_of_all_elements_located((By.XPATH,
                                                                             '//*[@class="android.widget.Button"]')))
        first_login_button[0].click()

        # Ввод логина и пароля в поля авторизации
        text_fields = wait.until(ec.presence_of_all_elements_located((By.XPATH,
                                                                      '//*[@class="android.widget.EditText"]')))
        if text_fields[0].text:
            text_fields[0].clear()
        text_fields[0].send_keys(LOGIN)
        text_fields[1].send_keys(PASSWORD)

        # Нажатия кнопки логина
        second_login_button = wait.until(ec.presence_of_all_elements_located((By.XPATH,
                                                                              '//*[@class="android.widget.Button"]')))
        second_login_button[1].click()
    except Exception as e:
        write_in_log_info(f"Произошла ошибка при авторизации: {str(e)}", log_type="error")
        raise e
    else:
        write_in_log_info(f"Авторизация прошла успешно")


def sign_out(driver):
    write_in_log_info(f"Выполняется выход из аккаунта Ajax Systems")
    try:
        wait = WebDriverWait(driver, 5)  # Максимальное время ожидания в секундах

        # Еще одна проверка авторизации, через нахождение элемента "SideBar"
        menu_button = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                 '//*[@resource-id="com.ajaxsystems:id/menuDrawer"]')))
        menu_button.click()

        # Нажатие на кнопку "Settings"
        setting_button = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                    '//*[@resource-id="com.ajaxsystems:id/settings"]')))
        setting_button.click()

        # Выход из учетной записи приложения
        sign_out_button = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                     '//*[@bounds="[0,1728][1080,1917]"]')))
        sign_out_button.click()

        # Переход на домашнюю страницу
        driver.press_keycode(3)

    except Exception as e:
        write_in_log_info(f"Произошла ошибка при выходе из аккаунта: {str(e)}", log_type="error")
        raise e
    else:
        write_in_log_info(f"Выход из аккаунта произошел успешно")


@pytest.fixture(scope="module")
def appium_driver():
    driver = create_appium_driver()
    login(driver)

    yield driver  # Возвращает драйвер тесту

    sign_out(driver)

    # Завершить сеанс после выполнения теста
    driver.quit()


@pytest.mark.parametrize("resource_id, expected_result", [
    ("com.ajaxsystems:id/settings", "successful authorization"),  # Проверка элемента "App Settings"
    ("com.ajaxsystems:id/help", "Invalid email format"),  # Проверка элемента "Help"
    ("com.ajaxsystems:id/logs", "Wrong login or password"),  # Проверка элемента "Report a Problem"
    ("com.ajaxsystems:id/addHub", "Wrong login or password"),  # Проверка кнопки "Add Hub"
])
def test_sidebar_functionality(resource_id, expected_result, appium_driver):
    write_in_log_info(
        f"Выполняется тест с данными: node_detail={resource_id}, expected_result={expected_result}")
    try:
        wait = WebDriverWait(appium_driver, 5)  # Максимальное время ожидания в секундах
        #
        # # Открытие приложения
        # appium_driver.press_keycode(3)
        # application = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@text="Ajax"]')))
        # application.click()
        #
        # # Нажатия кнопки для перехода на страницу авторизации
        # first_login_button = wait.until(ec.presence_of_all_elements_located((By.XPATH,
        #                                                                      '//*[@class="android.widget.Button"]')))
        # first_login_button[0].click()
        #
        # # Ввод логина и пароля в поля авторизации
        # text_fields = wait.until(ec.presence_of_all_elements_located((By.XPATH,
        #                                                               '//*[@class="android.widget.EditText"]')))
        # if text_fields[0].text:
        #     text_fields[0].clear()
        # text_fields[0].send_keys(LOGIN)
        # text_fields[1].send_keys(PASSWORD)
        #
        # # Нажатия кнопки логина
        # second_login_button = wait.until(ec.presence_of_all_elements_located((By.XPATH,
        #                                                                       '//*[@class="android.widget.Button"]')))
        # second_login_button[1].click()

        # Нажатия элемента "SideBar"
        menu_button = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                     '//*[@resource-id="com.ajaxsystems:id/menuDrawer"]')))
        menu_button.click()

            # Нажатие на одну из кнопок на "SideBar"
        setting_button = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                        f'//*[@resource-id="{resource_id}"]')))
        setting_button.click()

        appium_driver.press_keycode(4)

    except Exception as e:
        write_in_log_info(f"Произошла ошибка: {str(e)}", log_type="error")
        raise e
    else:
        write_in_log_info(f"Тест успешный")