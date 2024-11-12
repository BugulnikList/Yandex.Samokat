# Ирина Старунина Финальный проект Инженер по тестированию плюс 23 когорта
import requests

import config


def create_order(order_body):
    return requests.post(config.BASE_URL + config.CREATE_ORDERS, json=order_body)
def get_order_inf_track(track_numer):
    return requests.get_order_inf_track(config.BASE_URL + config.ORDER_INF + str(track_numer))