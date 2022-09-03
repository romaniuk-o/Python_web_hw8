# Python_web_hw8
ДЗ виконане за допомогою БД PostgreSQL.
Для роботи з проектом потрібно: Docker, DBeaver
Для запуску бази даних postgres у командному рядку необхідно виконати таку команду:
docker run --name HW_8_postgres -p 5432:5432 -e POSTGRES_PASSWORD=789123 -d postgres
В DBeaver створюємо нову базу PostgreSQL, використовуючі дані звідси:
"""docker run --name HW_8_postgres -p 5432:5432 -e POSTGRES_PASSWORD=789123 -d postgres"""

Далі створюємо таблиці, запустивши creat_db.py, заповнюємо їх запустивши insert.py, 
і насолоджуємось роботою запитів запустивши execute.py.
