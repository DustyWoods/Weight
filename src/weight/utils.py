import shutil
import plotext as plt
from statistics import median
from datetime import datetime

from .models import WeightRecord

def render(records: list[WeightRecord]):
    date = [ datetime.combine(record.date, datetime.min.time()) for record in records ]
    weight = [ record.weight for record in records ]

    fig = plt.figure
    fig.clear()

    fig.theme("colorless")

    fig.plot_size(0.8*shutil.get_terminal_size().columns, 20)
    fig.date("x").activate(form="%Y-%m-%d")
    signal = fig.signal(date, weight, marker="dot").lines()
    fig.draw(signal)
    fig.title("Recent Weight Record")

    fig.show()

    print()
    print("Overview:")
    print(f"\tMaximum: {max(weight):.1f} kg")
    print(f"\tMinimum: {min(weight):.1f} kg")
    print(f"\tAverage: {sum(weight) / len(weight):.1f} kg")
    print(f"\tMedian:  {median(weight):.1f} kg")
    print()

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

if __name__ == "__main__":
    import random
    from datetime import date

    records = [ WeightRecord(date(2026, 1, i), random.uniform(60.0, 90.0)) for i in range(1, 31) ]

    render(records)
