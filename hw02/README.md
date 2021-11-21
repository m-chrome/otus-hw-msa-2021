# Домашнее задание #2

Сделать простейший RESTful CRUD по созданию, удалению, просмотру и обновлению пользователей. 
Пример API  - https://app.swaggerhub.com/apis/otus55/users/1.0.0 

Добавить базу данных для приложения.
Конфигурация приложения должна хранится в Configmaps. 
Доступы к БД должны храниться в Secrets.
Первоначальные миграции должны быть оформлены в качестве Job-ы, если это требуется.
Ingress-ы должны также вести на url arch.homework/ (как и в прошлом задании)

На выходе должны быть предоставлена:

1. ссылка на директорию в github, где находится директория с манифестами кубернетеса 
2. инструкция по запуску приложения.
   1. команда установки БД из helm, вместе с файлом values.yaml.
   2. команда применения первоначальных миграций
   3. команда kubectl apply -f, которая запускает в правильном порядке манифесты кубернетеса
4. Postman коллекция, в которой будут представлены примеры запросов к сервису на создание, получение, изменение и удаление пользователя. Важно: в postman коллекции использовать базовый url - arch.homework.

Задание со звездочкой:
+5 балла за шаблонизацию приложения в helm чартах