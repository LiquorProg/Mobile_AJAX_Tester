import pytest

from selenium.webdriver.common.by import By
from appium_driver import create_appium_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope="function")
def appium_driver():
    driver = create_appium_driver()  # Использование функции

    yield driver  # Возвращает драйвер тесту

    # Завершить сеанс после выполнения теста
    driver.quit()


# Параметры для тестов
@pytest.mark.parametrize("username, password, expected_result", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", "successful authorization"),  # Позитивный тест
    ("qa.ajax.app.automation@gmail.com", "fdgdfgdfg", "Wrong login or password"),  # Негативный тест
    ("fdgdfdfgdfghl", "fgdfgdfgdf", "Invalid email format"),  # Негативный тест
])
def test_user_application_login(username, password, expected_result, appium_driver):
    wait = WebDriverWait(appium_driver, 5)  # Максимальное время ожидания в секундах

    # Открытие приложения
    appium_driver.press_keycode(3)
    application = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@text="Ajax"]')))
    application.click()

    # Нажатия кнопки для перехода на страницу авторизации
    first_login_button = wait.until(ec.presence_of_all_elements_located((By.XPATH, '//*[@class="android.widget.Button"]')))
    first_login_button[0].click()

    # Ввод логина и пароля в поля авторизации
    text_fields = wait.until(ec.presence_of_all_elements_located((By.XPATH, '//*[@class="android.widget.EditText"]')))
    if text_fields[0].text:
        text_fields[0].clear()
    text_fields[0].send_keys(username)
    text_fields[1].send_keys(password)

    # Нажатия кнопки логина
    second_login_button = wait.until(ec.presence_of_all_elements_located((By.XPATH,
                                                                          '//*[@class="android.widget.Button"]')))
    second_login_button[1].click()

    # Проверка на наличие поля с ошибкой авторизации
    try:
        result_message = wait.until(ec.presence_of_all_elements_located((By.XPATH,
                                                                         '//*[@resource-id="com.ajaxsystems:id/snackbar_text"]')))
    except Exception as e:
        print(e)
        result_message = False

    if not result_message:
        # Успешный сценарий
        try:
            # Еще одна проверка авторизации, через нахождение элемента "SideBar"
            menu_button = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                 '//*[@resource-id="com.ajaxsystems:id/menuDrawer"]')))
            menu_button.click()
            result_message = "successful authorization"
        except Exception:
            result_message = "failed authorization"
        assert result_message == expected_result

        # Нажатие на кнопку "Settings"
        setting_button = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                    '//*[@resource-id="com.ajaxsystems:id/settings"]')))
        setting_button.click()

        # Выход из учетной записи приложения
        sign_out_button = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                     '//*[@bounds="[0,1728][1080,1917]"]')))
        sign_out_button.click()

        # Переход на домашнюю страницу
        appium_driver.press_keycode(3)

    else:
        # Негативный сценарий
        assert result_message[0].text == expected_result

        # Нажатие на кнопку "Back"
        back_button = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                 '//*[@resource-id="com.ajaxsystems:id/back"]')))
        back_button.click()

        # Переход на домашнюю страницу
        appium_driver.press_keycode(3)