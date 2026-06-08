import time
import threading
import requests
from config import ESP32_IP

def _heartbeat_loop():
    while True:
        try:
            requests.get(f"{ESP32_IP}/heartbeat", timeout=2)
        except Exception as e:
            print(f"[heartbeat] Warning: could not reach ESP32 - {e}")
            time.sleep(1)

def start():
    thread = threading.Thread(target=_heartbeat_loop, daemon=True)
    thread.start()