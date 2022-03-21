def test_calc_addition(client):
    response = client.post("/calc", json={
        "firstNum": 3,
        "secondNum": 10,
        "operation": "+"
    })
    assert response.status_code == 200
    assert response.json['result'] == 13


def test_calc_multipication(client):
    response = client.post("/calc", json={
        "firstNum": 3,
        "secondNum": 10,
        "operation": "*"
    })
    assert response.status_code == 200
    assert response.json['result'] == 30
