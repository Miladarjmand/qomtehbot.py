import requests
import time
import datetime

# 🔹 اطلاعات تلگرام
BOT_TOKEN = "7830152929:AAH4ZvDDdtA8kOzSbbi3G4WDmvwL9KnF8Pc"
CHAT_ID = "@Miladarjmand1"

# 🔹 آدرس جستجوی سفرمی (مثال)
URL = "https://mrbilit.com/trains/qom-tehran?departureDate=1404-07-16"

# 🔹 تابع ارسال پیام در تلگرام
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("خطا در ارسال پیام:", e)

# 🔹 بررسی بلیط‌ها
def check_tickets():
    try:
        response = requests.get(URL, timeout=10)
        if "14:45" in response.text:
            send_telegram_message("🎫 بلیط قم → تهران ساعت 14:45 باز شد!")
        else:
            print(f"[{datetime.datetime.now()}] هنوز باز نشده...")
    except Exception as e:
        print("خطا در بررسی سایت:", e)

# 🔹 حلقه بررسی مداوم (هر 5 دقیقه)
while True:
    check_tickets()
    time.sleep(300)  # 5 دقیقه مکث
