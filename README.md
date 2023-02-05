# API для базы данных горных перевалов. Описание.
В данном проекте реализовано API для взаимодействия базы данных горных перевалов и мобильного приложения.
***
## Решённые задачи
* Спроектирована структура базы данных
* Реализован API на базе Django REST Framework
* Реализованы методы для взаимодействия с БД согласно поставленным задачам
* Добавлена документация на базе Swagger
***
## Структура базы данных
С целью обеспечения оптимальной связанности данных и удобства доступа к данным БД состоит из пяти моделей:
* Модель Пользователь, отправляющий данные. Содержит поля:
	* Имя (макс. 200 символов)
	* email (идентификационное поле; не может повторяться у разных пользователей)
	* Телефон (макс. 20 символов)

* Модель Глобальные географические зоны. Содержит поле:
	* Название (макс. 50 символов)

* Модель Локальные географические зоны. Подразумевает горный массив, например, Восточный Саян. Содержит поля:
	* Название (макс. 50 символов)
	* Глобальная зона (связь с моделью Глобальные географические зоны)

* Модель Горные перевалы. Содержит ключевую информацию о перевалах. Поля модели:
	* Название (макс. 100 символов)
	* Время внесения записи в БД (генерируется автоматически)
	* Географическая широта (разрешённые значения от 0 до 90)
	* Зона географической широты (разрешённые значения "N", "S")
	* Географическая долгота (разрешённые значения от 0 до 180)
	* Зона географической долготы (разрешённые значения "W", "E")
	* Высота перевала (разрешённые значения от 0 до 8878)
	* Пользователь, внёсший информацию (связь с моделью Пользователь)
	* Горный массив, в котором расположен перевал (связь с моделью Локальные географические зоны)
	* Зимняя сложность маршрута через перевал (разрешённые значения "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B")
	* Весенняя сложность маршрута через перевал (разрешённые значения "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B")
	* Летняя сложность маршрута через перевал (разрешённые значения "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B")
	* Осенняя сложность маршрута через перевал (разрешённые значения "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B")
	* Доступные виды транспорта на перевале. Массив может содержать несколько значений (разрешённые значения "FT" (пешком), "SK" (лыжи), "CN" (катамаран), "KK" (байдарка), "RT" (плот), "RR" (сплав), "BC" (велосипед), "AU" (автомобиль), "MB" (мотоцикл), "SA" (парус), "HR" (верхом))
	* Статус модерации. При добавлении автоматически присваивается значение "N" (разрешённые значения: "N" (новый), "P" (на рассмотрении), "A" (принят), "R" (отклонён))

* Модель Фотографии. Содержит поля:
	* Фотография
	* Время внесения записи в БД (генерируется автоматически)
	* Перевал (связь с моделью Горные перевалы)
***
## URL проекта
	* /passes/ - доступ к модели Горные перевалы посредством Django REST Framework
	* /photos/ - доступ к модели Фотографии посредством Django REST Framework
	* /api/ - корневая страница Django REST Framework
	* /swagger/ - страница с документацией по доступу к API посредством Swagger
	* /submitdata/ - API, принимающий POST запрос на добавление объекта в БД. Формат запроса и ответа - JSON
	* /submitdata/id - API, принимающий GET и PATCH запросы. Формат PATCH запроса - JSON. Формат ответа на любой запрос - JSON
	* /submitdata/user/email - API, принимающий GET запрос и возвращающий все перевалы, добавленные пользователем
***
## Формат JSON для POST и PATCH запросов и GET ответа

            "title": название (макс. 100 символов),
            "latitude": широта (разрешённые значения от 0 до 90),
            "latitude_zone": зона широты (разрешённые значения "N", "S"),
            "longitude": долгота (разрешённые значения от 0 до 180),
            "longitude_zone": зона долготы (разрешённые значения "W", "E"),
            "height": высота (разрешённые значения от 0 до 8878),
            "winter_dif": сложность зимой (разрешённые значения "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B"),
            "spring_dif": сложность осенью (разрешённые значения "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B"),
            "summer_dif": сложность летом (разрешённые значения "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B"),
            "autumn_dif": сложность осенью (разрешённые значения "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B"),
            "activities": транспорт [(разрешённые значения "FT", "SK", "CN", "KK", "RT", "RR", "BC", "AU", "MB", "SA", "HR")] ,
            "username": имя пользователя (макс. 200 симоволов),
            "email": email пользователя,
            "phone": телефон пользователя (макс. 20 симоволов),
            "photos": [список фотографий],


При получении POST запроса выполняется проверка наличия email пользователя в БД. При наличии создаётся связь полученной информации с существующим пользователем, поля "имя" и "телефон" обновляются.
PATCH запрос возможен только если статус модерации объекта установен как "N".
При получении PATCH запроса ключи "username", "email", "phone" игнорируются.
Ответ на GET запрос дополнительно содержит поля "id", "zone", "g_zone", "status".
***
## Формат JSON для ответа на POST, PATCH запросы и неудавшиеся GET запросы

                "status": 0 - PATCH не удался, 1 - PATCH удался, 200 - POST удался, 40x - неверная структура запроса, 500 - неверный тип запроса
                "message": подробности проблемы,
                "id": id объекта,

***
## Формат JSON для ответа на запрос \submitdata\user\email

                "id перевала": {JSON по формату GET ответа},