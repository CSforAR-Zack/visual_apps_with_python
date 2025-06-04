import requests as req
import json
import sqlite3 as s3

import my_token as mt


def main():
    # Query Variables
    token: str = mt.TOKEN
    dateset_id: str = "GHCND"
    datatype_ids: str = "TMAX,TMIN"
    station_id: str = "GHCND:USW00003952"
    start_date: str = "2024-01-01"
    end_date: str = "2024-12-31"
    units: str = "standard"
    limit: str = "1000"

    requests_url_parts: list = [
        "https://www.ncei.noaa.gov/cdo-web/api/v2/data?",
        f"datasetid={dateset_id}&",
        f"datatypeid={datatype_ids}&",
        f"stationid={station_id}&",
        f"startdate={start_date}&",
        f"enddate={end_date}&",
        f"units={units}&",
        f"limit={limit}",
    ]

    request_url: str = "".join(requests_url_parts)
    response: req.Response = req.get(request_url, headers={"token":token})
    data: dict = json.loads(response.text)
    
    dates: list = list()
    highs: list = list()
    lows: list = list()

    for item in data["results"]:
        date: str = item["date"].split("T")[0]
        if date not in dates:
            dates.append(date)
        if item["datatype"] == "TMAX":
            highs.append(item["value"])
        elif item["datatype"] == "TMIN":
            lows.append(item["value"])

    conn: s3.Connection = s3.connect("weather.db")
    cursor: s3.Cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS weather_data (date TEXT, high REAL, low REAL)"
    )

    for i in range(len(dates)):
        command: str = "INSERT INTO weather_data (date, high, low) VALUES (?, ?, ?)"
        cursor.execute(command, (dates[i], highs[i], lows[i]))
        conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()