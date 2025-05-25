import requests

# --- CONFIG ---
PARAMS_URL = "https://0xjew.com/params"
NEXMO_API_URL = "https://rest.nexmo.com/sms/json"
API_KEY = "7e6f6017"
API_SECRET = "1qZb01p1E0HqBTJ5"
TO_NUMBER = "972523819678"
FROM_NAME = "osherad"


# --- FUNCTIONS ---

def fetch_params(url):
    """Download and parse key=value lines from remote file."""
    response = requests.get(url)
    response.raise_for_status()
    data = {}
    for line in response.text.strip().splitlines():
        if '=' in line:
            key, value = line.split('=', 1)
            data[key.strip()] = value.strip()
    return data


def build_message(params):
    """Build final SMS message from param dict."""
    try:
        return (
            f"מוצר: {params['product']}\n"
            f"ברקוד: {params['barcode']}\n"
            f"נסרק {params['count']} פעמים בעסקה מס {params['transaction_id']} על סכום {params['total']}₪"
        )
    except KeyError as e:
        raise ValueError(f"Missing required field: {e}")


def send_sms(message):
    """Send SMS through Nexmo."""
    payload = {
        "type": "unicode",
        "api_key": API_KEY,
        "api_secret": API_SECRET,
        "to": TO_NUMBER,
        "from": FROM_NAME,
        "text": message
    }
    response = requests.post(NEXMO_API_URL, data=payload)
    response.raise_for_status()
    return response.text


# --- MAIN EXECUTION ---

try:
    params = fetch_params(PARAMS_URL)
    msg = build_message(params)
    result = send_sms(msg)
    print("SMS sent successfully:\n", result)
except Exception as e:
    print("Error:", e)