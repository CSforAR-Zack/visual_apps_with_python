# Imports
import requests as req
import sqlite3 as s3
import json

import my_token as mt


def main():
    # Query Variables
    token: str = mt.TOKEN
    dataset_id: str = "GHCND"
    datatype_ids: str = "TMAX,TMIN"
    station_id: str = "GHCND:USW00003952"
    start_date: str = "2024-01-01"
    end_date: str = "2024-12-31"
    units: str = "standard"

    requests_url_parts: list = [
        "https://www.ncei.noaa.gov/cdo-web/api/v2/data?",
        f"datasetid={dataset_id}&",
        f"datatypeid={datatype_ids}&",
        f"stationid={station_id}&",
        f"startdate={start_date}&",
        f"enddate={end_date}&",
        f"units={units}&",
        "limit=1000",
    ]

    request_url: str = "".join(requests_url_parts)
    r: req.Response = req.get(request_url, headers={'token':token})
    data: dict = json.loads(r.text)

    dates: list = list()
    highs: list = list()
    lows: list = list()

    for item in data["results"]:
        date: str = item["date"]
        date = date.split("T")[0]

        if date not in dates:
            dates.append(date)

        if item["datatype"] == "TMAX":
            highs.append(item["value"])
        elif item["datatype"] == "TMIN":
            lows.append(item["value"])

    conn: s3.Connection = s3.connect("weather.db")
    c: s3.Cursor = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS weather_data (date TEXT, high REAL, low REAL)")
    conn.commit()


    for i in range(len(dates)):
        command: str = "INSERT INTO weather_data (date, high, low) VALUES (?, ?, ?)"
        c.execute(command, (dates[i], highs[i], lows[i]))
        conn.commit()

    c.close()
    conn.close()


if __name__ == "__main__":
    main()