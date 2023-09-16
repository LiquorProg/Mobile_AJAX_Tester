import subprocess
from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_udid():
    try:
        # Полный путь к adb.exe
        adb_path = 'C:\\Users\\sasha\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe'

        result = subprocess.run([adb_path, 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output_lines = result.stdout.strip().split('\n')

        # Поиск строк с устройствами
        devices = [line.split('\t')[0] for line in output_lines[1:] if '\t' in line]

        if devices:
            return devices[0]

        return None
    except Exception as e:
        print(f"Ошибка при определении udid: {e}")
        return None


def create_appium_driver():
    udid = get_udid()
    if udid:
        print(f"Найдено устройство с udid: {udid}")

        # Настройки для подключения к Appium серверу
        options = UiAutomator2Options()
        options.platformVersion = '12'
        options.udid = udid

        # Создание драйвера Appium
        driver = webdriver.Remote('http://26.177.237.19:4723', options=options)
        return driver
    else:
        print("Устройство не найдено, не удается создать драйвер Appium.")


if __name__ == "__main__":
    print(get_udid())