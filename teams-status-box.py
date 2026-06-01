# import websocket
# import json

# paired = False

# def on_open(ws):
#     print("Connected!")

# def on_message(ws, message):
#     global paired
#     data = json.loads(message)
#     meeting_permissions = data.get("meetingUpdate", {}).get("meetingPermissions")
#     meeting_state = data.get("meetingUpdate", {}).get("meetingState")

#     #TODO: Put this in a method maybe?

#     if not paired and meeting_permissions.get("canPair") == True:
#             print("Pairing...")
#             paired = True
#             ws.send(json.dumps({
#                 "action": "toggle-mute",
#                 "parameters": {},
#                 "requestId": 1
#             }))

#     if meeting_state:
#          in_call = meeting_state.get("isInMeeting", False)
#          mic_on  = not meeting_state.get("isMuted", True)
#          cam_on  = meeting_state.get("isVideoOn", False)

#          print(f"In call: {in_call} | Mic: {mic_on} | Camera: {cam_on}")

# def on_close(ws, close_status_code, close_msg):
#     print("Disconnected")

# def on_error(ws, error):
#     print("Error: ", error)

# ws = websocket.WebSocketApp(
#     "ws://localhost:8124?protocol-version=2.0.0&manufacturer=DeskBoxDevice&device=LEDController&app=DeskBox&app-version=1.0.0",
#     on_open=on_open,
#     on_message=on_message,
#     on_error=on_error,
#     on_close=on_close
# )

# ws.run_forever()