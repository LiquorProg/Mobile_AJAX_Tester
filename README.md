### Тестування програми Ajax Systems
Цей проект є тестовим завданням автоматизації тестування мобільного додатка Ajax Systems з використанням Appium і Python. Проект включає тести для авторизації користувача в додатку з позитивними і негативними сценаріями, а також базові функції для взаємодії з додатком.

### Встановлення
1) Встановлення Node.js: Appium працює на основі Node.js, тому першим кроком необхідно встановити Node.js. Завантажте та встановіть його з офіційного сайту [Node.js](https://nodejs.org/).
2) Встановлення Java Development Kit (JDK): Appium вимагає встановленої JDK. Ви можете завантажити та встановити JDK з офіційного сайту [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html)
3) Встановлення Android Studio: Appium вимагає Android SDK для взаємодії з Android-пристроями та емуляторами. Для встановлення Android SDK рекомендується встановити Android Studio. Завантажте Android Studio з [офіційного сайту](https://developer.android.com/studio)
4) Після встановлення Android Studio, запустіть його та перейдіть в "More Actoins" > "SDK Manager". Встановіть необхідні компоненти SDK, включаючи платформи Android та інструменти для створення емуляторів (AVD).
5) Тепер установіть Appium за допомогою npm (Node Package Manager), який встановлюється разом із Node.js. Відкрийте командний рядок (Command Prompt) та виконайте наступну команду: 
```shell
npm install -g appium
```
6) Також робота appium потребує встановленного драйверу - UiAutomator2, детальніше про його встановлення можна почитати в [документаціі](https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/).
7) Встановіть необхідні бібліотеки Python, виконавши команду:
```shell
pip install -r requirements.txt
```

### Використання
1) Запустіть Appium Server: Переконайтеся, що Appium Server запущено на вашому комп'ютері. Ви можете використовувати офіційний сайт Appium для отримання інструкцій із запуску.
2) Запустіть емулятор Android пристрою, детальніше можна почитати [тут](https://developer.android.com/studio/run/emulator).
3) Запустіть тести: Запустіть тести за допомогою фреймворку тестування, такого як PyTest.
