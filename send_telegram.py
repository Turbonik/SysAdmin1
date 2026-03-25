#!/usr/bin/env python3
import requests
import sys

ENV_PATH = "/home/anton/Desktop/SysAdNstu/.env"
with open(ENV_PATH) as f:
    lines = f.read().splitlines()

TOKEN = lines[0].split("=")[1].strip()
CHAT_ID = lines[1].split("=")[1].strip()

login = sys.argv[1]
datetime = sys.argv[2]

text = f"Пользователь {login} вошел в систему {datetime}"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={"chat_id": CHAT_ID, "text": text})