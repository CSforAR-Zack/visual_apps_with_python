import calendar
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3 as s3
import tkinter as tk


def main():

    # Graph
    root: tk.Tk = tk.Tk()
    root.title("Database and Visual")

    font: tuple = ("Arial", 18)

    # Select Month
    month_label: tk.Label = tk.Label(
        root,
        text="Select Month:",
        anchor="w",
        font=font,
    )
    month_label.pack(expand=True, fill="both", padx=5, pady=5)

    months: list = list(calendar.month_name)
    months.remove("")
    months.insert(0, "Full Year")

    graph_command = lambda: graph_data(
        months.index(month_spinbox.get()),
        ax,
        canvas,
    )

    month_spinbox: tk.Spinbox = tk.Spinbox(
        root,
        values=months,
        state="readonly",
        command=graph_command,
        font=font,
    )

    month_spinbox.pack(expand=True, fill="both", padx=5, pady=5)

    fig, ax = plt.subplots()
    ax.set_title("Little Rock Daily Temps")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (\u00b0F)")
    
    fig.autofmt_xdate()
    canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(fig, master=root)
    canvas_widget: tk.Widget = canvas.get_tk_widget()
    canvas_widget.pack(padx=5, pady=5)
    
    graph_command()

    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))

    root.mainloop()


def graph_data(selection: str, ax: plt.Axes, canvas: FigureCanvasTkAgg
) -> None:
    """Graph the data in the database."""
    
    raw_data: list = get_data(selection)
    data: dict = process_data(raw_data)

    ax.clear()
    ax.set_title("Little Rock Daily Temps")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (\u00b0F)")
    fig: plt.Figure = ax.figure
    fig.autofmt_xdate()
    ax.plot(data["dates"], data["highs"], c="red")
    ax.plot(data["dates"], data["lows"], c="blue")
    ax.legend(["High", "Low"], loc="upper left")
    canvas.draw()


def on_closing(root: tk.Tk) -> None:
    """Handle the window closing event.
    This function is called when the window is closed.
    Matplotlib will not close the window automatically and is
    blocking the main thread with its event loop.
    """

    root.quit()
    root.destroy()


def get_data(selection: str) -> list:
    """Get the data from the database."""

    if selection == 0:
        start_date: str = "2024-01-01"
        end_date: str = "2024-12-31"
    else:
        start_date: str = f"2024-{selection:02}-01"
        end_date: str = f"2024-{selection:02}-31"

    conn: s3.Connection = s3.connect("weather.db")
    c: s3.Cursor = conn.cursor()

    command: str = f"SELECT * FROM weather_data WHERE date BETWEEN '{start_date}' AND '{end_date}'"

    rows: list = c.execute(command).fetchall()

    c.close()
    conn.close()

    return rows


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
        "lows": lows
    }


if __name__ == "__main__":
    main()