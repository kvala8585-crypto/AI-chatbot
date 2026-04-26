import requests

url = "https://hooks.zapier.com/hooks/catch/27370622/uv2dwvm/"

data = {
    "query": "hello"
}

response = requests.post(url, json=data)

print(response.text)