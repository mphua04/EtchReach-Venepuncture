#pip install websockets first 

# my comments: 
# esp32-pi.py should be the communication btwn esp32 & raspberry pi & give data to websocket.py
# websocket.py forwards imu data to front end dashboard.html in real time 
# use three.js for 3d visualisation and establish websocket connection to receive live imu data from websocket.py


import asyncio
import websockets

# WebSocket server host and port
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 8765       # WebSocket port

async def send_imu_data(websocket, path):
    try:
        while True:
            # Replace this line with your Bluetooth data reading logic
            # Example: Simulate IMU data as JSON
            imu_data = {
                "pitch": 0.5,  # Replace with actual pitch from ESP32
                "yaw": 1.0,    # Replace with actual yaw from ESP32
                "roll": -0.3   # Replace with actual roll from ESP32
            }
            await websocket.send(str(imu_data))  # Send IMU data as JSON string
            await asyncio.sleep(0.1)  # Adjust based on your data frequency
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

# Start the WebSocket server
start_server = websockets.serve(send_imu_data, HOST, PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
