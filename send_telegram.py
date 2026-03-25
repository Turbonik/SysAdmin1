#!/usr/bin/env python3
import requests
import sys

print('Send starting')

TOKEN = "8784963710:AAHfZAxRTNSqB12wZ2ypNW7dlXZJ7MdV6OM"
CHAT_ID = "5741136303"

login = sys.argv[1]
datetime = sys.argv[2]

text = f"Пользователь {login} вошел в систему {datetime}"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={"chat_id": CHAT_ID, "text": text})