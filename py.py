import requests

# Step 1: Download parameters
params_url = "https://0xjew.com/params"
lines = requests.get(params_url).text.strip().splitlines()

# Extract values
product_name = lines[0]
barcode = lines[1]
count, transaction_id, total = lines[2].replace(',', '').split()

# Step 2: Build the message
message = (
    f"מוצר: {product_name}\n"
    f"ברקוד: {barcode}\n"
    f"נסרק {count} פעמים בעסקה מס {transaction_id} על סכום {total}₪"
)

# Step 3: Send via Nexmo
sms_url = "https://rest.nexmo.com/sms/json"
payload = {
    "type": "unicode",
    "api_key": "7e6f6017",
    "api_secret": "1qZb01p1E0HqBTJ5",
    "to": "972523819678",
    "from": "osherad",
    "text": message
}

response = requests.post(sms_url, data=payload)
print(response.text)