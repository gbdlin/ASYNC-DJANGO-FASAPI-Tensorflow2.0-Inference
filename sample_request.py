import requests

url = "http://159.65.126.185/api/predict"

payload = {}
headers = {}
files = [("files", ("cat.jpg", open("SampleImages/cat.jpg", "rb"), "image/jpeg"))]


response = requests.request("POST", url, headers=headers, data=payload, files=files)

assert response.status_code == 200, "Failed"
