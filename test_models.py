import urllib.request, json, os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
models = ['gemini-2.5-pro', 'gemini-flash-latest', 'gemini-pro-latest', 'gemini-2.5-flash-lite']
data = {'contents': [{'parts': [{'text': 'hi'}]}]}
for m in models:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={api_key}'
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req)
        print(f'SUCCESS: {m}')
        break
    except Exception as e:
        print(f'FAIL {m}: {e}')
