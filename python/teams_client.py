import websocket
import json
import esp32_client

paired = False

def on_open(ws):
    print("Connected!")

def on_message(ws, message):
    global paired

    try:
        data = json.loads(message)
        meeting_permissions = data.get("meetingUpdate", {}).get("meetingPermissions", {})
        meeting_state = data.get("meetingUpdate", {}).get("meetingState")

    except Exception as e:
         import traceback
         traceback.print_exc()

    if not paired and meeting_permissions.get("canPair") == True:
            print("Pairing...")
            paired = True

            #We need to send something to teams on websocket so that it recognises that we are observing it and lets us see meetingState
            ws.send(json.dumps({
                "action": "toggle-mute",
                "parameters": {},
                "requestId": 1
            }))

    if meeting_state:
         in_call = meeting_state.get("isInMeeting", False)
         mic_on  = not meeting_state.get("isMuted", True) if in_call else False
         cam_on  = meeting_state.get("isVideoOn", False) if in_call else False

         esp32_client.send_status(in_call, mic_on, cam_on)

def on_close(ws, close_status_code, close_msg):
    print("Disconnected")

def on_error(ws, error):
    print("Error: ", error)

def start():
    ws = websocket.WebSocketApp(
        "ws://localhost:8124?protocol-version=2.0.0&manufacturer=DeskBoxDevice&device=LEDController&app=DeskBox&app-version=1.0.0",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    ws.run_forever()