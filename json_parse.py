import json
import csv

try:
    with open("measurements.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    with open("measurements.csv", "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["location", "parameter", "value", "unit", "utc_date", "local_date", "latitude", "longitude", "country", "city"])

        for item in data['results']:
            location = item['location']
            parameter = item['parameter']
            value = item['value']
            unit = item['unit']
            utc_date = item['date']['utc']
            local_date = item['date']['local']
            latitude = item['coordinates']['latitude']
            longitude = item['coordinates']['longitude']
            country = item['country']
            city = item['city']

            csv_writer.writerow([location, parameter, value, unit, utc_date, local_date, latitude, longitude, country, city])

except Exception as e:
    print("Error:", str(e))
