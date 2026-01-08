import requests

BOT_TOKEN = ""
CHAT_ID =


def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Ошибка отправки уведомления в Telegram")
        print(response.text)
