Трекер полезных привычек

Цель проекта заключается в создании бэкенд-части SPA веб-приложения, которая позволяет 
пользователям приобретать новые полезные привычки.

Установка и использование
Для работы программы необходимо заполнить файлы:

.env своими данными (на примере файла .env.sample).
В файле settings.py необходимо указать адреса frontend-серверов в разделе CORS

Установить Docker и запустить следующие команды:

#запуск приложения
docker-compose up -d --build

#создание superuser
docker exec habit_tracker-app-1 python manage.py csu

Описание приложений
habits - отвечает за создание и управление привычками, местами выполнения привычек, 
вознаграждениями за привычки
users - отвечает за регистрацию и авторизацию пользователей сайта

Дополнительная информация
tasks.py(habits) - содержит периодическую задачу по рассылке уведомлений о наступлении времени 
выполнения привычки в telegram
Настроен вывод документации.

Рекомендации пользователям по получению telegram-рассылок:
При регистрации необходимо указать chat_id, который можно получить с помощью @getmyid_bot. 
Для этого необходимо добавить данный аккаунт в телеграм и выполнить команду /start
Для того чтобы наш бот имел возможность рассылать вам сообщения, необходимо добавить бота 
в "контакты" телеграмм и выполнить команду /start