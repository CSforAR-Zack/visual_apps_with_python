import sqlite3 as s3
import matplotlib.pyplot as plt
import datetime as dt


def main():
    # Get data from db
    conn: s3.Connection = s3.connect("weather.db")
    c: s3.Cursor = conn.cursor()

    rows: list = c.execute("SELECT * FROM weather_data").fetchall()

    c.close()
    conn.close()

    # Process for graphing
    dates: list = list()
    highs: list = list()
    lows: list = list()

    for row in rows:
        date: dt.datetime = dt.datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(date)
        highs.append(row[1])
        lows.append(row[2])

    # Graph
    plt.plot(dates, highs, c="red")
    plt.plot(dates, lows, c="blue")

    plt.title("Little Rock Daily Temps")
    plt.xlabel("Date", fontsize=18)
    plt.ylabel("Temperature (\u00b0F)", fontsize=18)
    
    plt.legend(["High", "Low"], loc="upper left")
    plt.gcf().autofmt_xdate()

    plt.show()


if __name__ == "__main__":
    main()