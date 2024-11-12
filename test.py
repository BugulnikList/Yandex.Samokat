# Ирина Старунина Финальный проект Инженер по тестированию плюс 23 когорта
import data
import request


def test_order_inf_track():
    track = request.create_order(data.order_body).json()['track']
    response = request.get_order_inf_track(track)
    assert response.status_code == 200