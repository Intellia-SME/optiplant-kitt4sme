import json

import requests

URL = "http://localhost:5000/prediction"

data = {
    "data": [
        {
            "id": "46c6b056-c2b6-4180-a97b-4f231f4a7c23",
            "type": "ElevatorMachine",
            "timestamp": {"value": "2019-01-01 16:40:00"},
            "uuid": {"value": "46c6b056-c2b6-4180-a97b-4f231f4a7c23"},
            "noise": {"value": 88},
            "vibration": {"value": 42},
            "humidity": {"value": 78},
            "motor_1_status": {"value": 0},
            "motor_1_rslr": {"value": 60000},
            "motor_1_rslm": {"value": 60000},
            "motor_1_voltage": {"value": 433},
            "motor_1_ampere": {"value": 6.9},
            "motor_2_status": {"value": 0},
            "motor_2_rslr": {"value": 60000},
            "motor_2_rslm": {"value": 60000},
            "motor_2_voltage": {"value": 435},
            "motor_2_ampere": {"value": 6.8},
            "motor_3_status": {"value": 0},
            "motor_3_rslr": {"value": 60000},
            "motor_3_rslm": {"value": 60000},
            "motor_3_voltage": {"value": 440},
            "motor_3_ampere": {"value": 6.37},
            "motor_4_status": {"value": 0},
            "motor_4_rslr": {"value": 60000},
            "motor_4_rslm": {"value": 60000},
            "motor_4_voltage": {"value": 438},
            "motor_4_ampere": {"value": 6.2},
            "motor_5_status": {"value": 0},
            "motor_5_rslr": {"value": 60000},
            "motor_5_rslm": {"value": 60000},
            "motor_5_voltage": {"value": 435},
            "motor_5_ampere": {"value": 6.15},
        }
    ]
}

headers = {"Content-type": "application/json", "Accept": "text/plain"}

response = requests.post(URL, data=json.dumps(data), headers=headers)
print(response.json())
