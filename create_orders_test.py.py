import sender_stand_request
import data

# Наталья Волкова, 08 а когорта — Финальный проект. Инженер по тестированию плюс


def test_get_orders_track(): # Получение данных о заказе по треку
    track = sender_stand_request.post_orders_body(data.orders_body).json()['track']
    response = sender_stand_request.get_orders_track(track)

    assert response.status_code == 200  # Проверка кода ответа
