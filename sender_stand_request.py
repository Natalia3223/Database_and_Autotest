# Наталья Волкова, 08 а когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


def post_orders_body(orders_body):  # Функция на создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS, json=orders_body, headers=data.headers)


def get_orders_track(track_number):  # Функция на получение заказа по треку
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params={'t': track_number},
                        headers=data.headers)
    
