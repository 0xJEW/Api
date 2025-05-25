import requests

url = "https://rest.nexmo.com/sms/json"
payload = {
    "type": "unicode",
    "api_key": "7e6f6017",
    "api_secret": "1qZb01p1E0HqBTJ5",
    "to": "972523819678",
    "from": "osherad",
    "text": (
        "מוצר: קוקה קולה 1.5\n"
        "ברקוד: 7290110115227\n"
        "נסרק 25 פעמים בעסקה מס 1234567 על סכום 1432.99₪"
    )
}

response = requests.post(url, data=payload)
print(response.text)