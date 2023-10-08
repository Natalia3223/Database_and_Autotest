# Наталья Волкова, 08 а когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


def post_orders_body(orders_body):  # Функция на создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         # Ключевое слово и название пакета
                         json=orders_body,  # Тело
                         headers=data.headers)  # Заголовки


response = post_orders_body(data.orders_body)  # Сохранение ответа на запрос
print(response.status_code)  # Выведение на экран код ответа
print(response.json())  # Выведение на экран тело ответа


def get_orders_track(track_number):
    response = requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDERS_TRACK, params={'t': track_number}, headers=data.headers)
    return response
