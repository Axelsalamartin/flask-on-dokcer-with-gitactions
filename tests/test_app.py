import json

def test_index(app, client):
    data = {'sl': [5.84, 4.38], 'sw': [3.0, 2.16], 'pl': [3.75, 7.65], 'pw': [1.1, 1.23]}
    req = client.post('/predict', data=json.dumps(data))
    assert req.status_code == 200
    assert req.json["results"] == [[1, 0]]