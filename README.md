### Установка и запуск

1. Склонировать репозиторий:

```
git clone "using the web URL"
```

2. Перейти в директорию проекта
3. Создать виртуальное окружение:

```
python3.10 -m venv venv
```

4. Активировать окружение:

```
source venv/bin/activate
```

5. Установка зависимостей:

```
pip install -r requirements.txt
```

6.1. Запустить тесты:

```
pytest --alluredir=allure-results
```

6.2. Запустить тесты параллельно:

```
pytest -n 4 --alluredir=allure-results
```

7. Запустить allure отчет:

```
allure serve allure-results
```