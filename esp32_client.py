import requests
from config import ESP32_IP

def send_status(in_call, mic_on, cam_on):
    try:
        requests.get(
            f"{ESP32_IP}/update",
            params={"call": int(in_call), "mic": int(mic_on), "camera": int(cam_on)},
            timeout=2
        )
    except Exception as e:
        print(f"[esp32] Warning: could not send status = {e}")