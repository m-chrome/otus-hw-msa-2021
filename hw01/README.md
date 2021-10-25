# Домашнее задание 1

## Задача

Создать минимальный сервис, который отвечает на порту 8000 и имеет http-метод `GET /health RESPONSE: {"status": "OK"}`.
Собрать локально образ приложения в docker. Запушить образ в dockerhub.

Написать манифесты для деплоя в k8s для этого сервиса.
Манифесты должны описывать сущности Deployment, Service, Ingress. 
В Deployment могут быть указаны Liveness, Readiness пробы. 
Количество реплик должно быть не меньше 2. Image контейнера должен быть указан с Dockerhub. Хост в Ingress-е должен быть arch.homework. В итоге после применения манифестов GET запрос на http://arch.homework/health должен отдавать {“status”: “OK”}.
Extra задание - в Ingress-е должно быть правило, которое форвардит все запросы с /otusapp/{student name}/* на сервис с rewrite-ом пути. Где {student name} - это имя студента.

## Реализация

### Сервис и деплой в Docker

В директории service - минимальный сервис на Python + FastApi.
Образ залит на [dockerhub](https://hub.docker.com/r/bananasoul/otus-msa-hw-1).

### k8s манифесты

Загрузка манифестов в k8s:
```shell
cd k8s-manifests
kubectl create ns otus
kubectl apply -f .
```

Urls:
```shell
curl -i -XGET -H "Host: arch.homework" http://{{ ingress IP }}/health
curl -i -XGET -H "Host: arch.homework" http://{{ ingress IP }}/otusapp/michail/health
```
