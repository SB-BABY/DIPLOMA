##Windows

### Установка:
```cmd
    cd TelegramCloutAlphaBot
    python -m venv ./venv
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt
```
### Конфигурирование:
Переменные окружения можно задать через .env файл.\
Список переменных окружения:
- TOKEN: string


###Запуск (при уже активированном venv) :
```cmd
    python .\bot_telegram.py
```