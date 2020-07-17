import requests

url = "http://0.0.0.0:8000/custom-logger"
to_predict_dict = {"id":"Phan Van Hoai Duc"}
r = requests.post(url, json=to_predict_dict)
print(r.text)