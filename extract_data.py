import requests
import json

def get_data():
    try:
        #endpoint -> https://api.openaq.org
        response = requests.get("https://api.openaq.org/v1/measurements?limit=1000")

        data = response.json()
        
        with open("measurements.json", "w") as json_file:
            json.dump(data, json_file , indent=4)

    except Exception as e:
        print("Error:", str(e))

get_data()
