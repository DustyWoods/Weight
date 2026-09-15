import shutil
import plotext as plt
from statistics import median
from datetime import datetime

from .models import WeightRecord

def render(records: list[WeightRecord], days = 30, flag_lines = True, flag_data = True, flag_graph = True):
    if flag_graph:
        _graph(records, flag_lines)
    if flag_data:
        weights = [ record.weight for record in records ]
        _data(weights, days)

def confirm_clean(times: int = 3):
    cancelled = False

    for _ in range(times):
        answer = input("Are you sure you want to clear all weight records? [y/N]").strip().lower()

        if answer in ('', 'y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            cancelled = True
            break

        print("Please enter 'y' or 'n'")

    if cancelled:
        print("Operation cancelled.")
    else:
        print("Too many invalid inputs. Operation cancelled.")

    return False

def _graph(records, flag_lines=True):

    date = [ datetime.combine(record.date, datetime.min.time()) for record in records ]
    weight = [ record.weight for record in records ]

    fig = plt.figure
    fig.clear()

    width = shutil.get_terminal_size().columns * 0.8
    height = 20

    fig.plot_size(width, height)
    fig.date("x").activate(form="%Y-%m-%d")

    if flag_lines:
        signal1 = fig.signal(date, weight, marker=plt.marker("braille", pixel="white")).lines()
        fig.draw(signal1)

    signal2 = fig.signal(date, weight, marker=plt.marker("x", pixel="cyon"))
    fig.draw(signal2)

    fig.theme("simple")
    fig.title("Recent Weight Record")
    fig.show()

def _data(weights, n_days):
    count = len(weights)
    maximum = max(weights, default=-1)
    minimum = min(weights, default=-1)
    average = sum(weights) / count if count else -1
    med = median(weights) if count else -1
    change = weights[-1] - weights[-2] if count > 1 else 0.0
    print()
    print(f"Overview in the past {n_days} days ({count} records):")
    print(f"\tMaximum: {maximum:.1f} kg")
    print(f"\tMinimum: {minimum:.1f} kg")
    print(f"\tAverage: {average:.1f} kg")
    print(f"\tMedian:  {med:.1f} kg")
    print()
    print(f"Compared with the previous record, change: {change:.1f} kg")
    print()

if __name__ == "__main__":
    import random
    from datetime import date

    records = [ WeightRecord(date(2026, 1, i), random.uniform(60.0, 90.0)) for i in range(1, 31) ]

    render(records)
