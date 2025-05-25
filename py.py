def fetch_params(url):
    """Download and parse key=value lines from params file."""
    response = requests.get(url)
    response.raise_for_status()
    lines = response.text.strip().splitlines()
    data = {}
    for line in lines:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            data[key] = value
    required_keys = ['product', 'barcode', 'count', 'transaction_id', 'total']
    if not all(k in data for k in required_keys):
        raise ValueError("Missing required fields in params file")
    return data

def build_message(data):
    """Construct the SMS message from key-value data."""
    return (
        f"מוצר: {data['product']}\n"
        f"ברקוד: {data['barcode']}\n"
        f"נסרק {data['count']} פעמים בעסקה מס {data['transaction_id']} על סכום {data['total']}₪"
    )