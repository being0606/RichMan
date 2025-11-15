import requests
import pandas as pd

url = "https://api.bithumb.com/public/ticker/BTC_KRW"
response = requests.get(url).json()

data = response["data"]
df = pd.DataFrame([data])   # 딕셔너리를 DF로 만들려면 리스트로 감싸기

print(df)