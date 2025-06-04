import tkinter as tk
import calendar
import sqlite3 as s3
import datetime as dt

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def main():
    root: tk.Tk = tk.Tk()
    root.title("Database and Visual")

    font: tuple = ("Arial", 18)

    month_label: tk.Label = tk.Label(
        root,
        text="Select Month:",
        anchor="w",
        font=font,
    )
    month_label.pack(expand=True, fill="both", padx=5, pady=5)

    months: list = list(calendar.month_name)
    months[0] = "Full Year"
    
    graph_command = lambda: graph_data(
        months.index(month_spinbox.get()),
        ax,
        canvas,
    )

    month_spinbox: tk.Spinbox = tk.Spinbox(
        root,
        values=months,
        state="readonly",
        font=font,
        command=graph_command,
    )
    month_spinbox.pack(expand=True, fill="both", padx=5, pady=5)

    fig, ax = plt.subplots()

    canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(fig, root)
    canvas_widget: tk.Widget = canvas.get_tk_widget()
    canvas_widget.pack(padx=5, pady=5)

    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))

    graph_command()

    root.mainloop()


def graph_data(
    selection: int, ax: plt.Axes, canvas: FigureCanvasTkAgg
) -> None:
    """Graph the data in the database."""

    raw_data: list = get_data(selection)
    data: dict = process_data(raw_data)
    
    ax.clear()
    ax.set_title("Little Rock Daily Temps - 2024")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (\u00b0F)")
    ax.plot(data["dates"], data["highs"], c="red")
    ax.plot(data["dates"], data["lows"], c="blue")
    ax.legend(["High", "Low"], loc="upper left")

    fig: plt.Figure = ax.figure
    fig.autofmt_xdate()
    canvas.draw()


def process_data(rows: list) -> dict:
    """Process the data for graphing."""

    dates: list = list()
    highs: list = list()
    lows: list = list()

    for row in rows:
        date: dt.datetime = dt.datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(date)
        highs.append(row[1])
        lows.append(row[2])

    return {
        "dates": dates,
        "highs": highs,
        "lows": lows,
    }


def get_data(selection: int) -> list:
    """Get the data from the database."""

    if selection == 0:
        start_date: str = "2024-01-01"
        end_date: str = "2024-12-31"
    else:
        start_date: str = f"2024-{selection:02}-01"
        end_date: str = f"2024-{selection:02}-31"

    conn: s3.Connection = s3.connect("weather.db")
    cursor: s3.Cursor = conn.cursor()

    command: str = f"SELECT * FROM weather_data WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    rows: list = cursor.execute(command).fetchall()

    cursor.close()
    conn.close()

    return rows


def on_closing(root: tk.Tk) -> None:
    """Close all windows and widgets."""

    root.quit()
    root.destroy()


if __name__ == "__main__":
    main()