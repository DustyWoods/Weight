import sqlite3
from datetime import date
from pathlib import Path

from .models import WeightRecord

class DB:

    def __init__(self, path: Path):
        self.conn = sqlite3.connect(path)

    def __enter__(self):
        self.init()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def init(self) -> None:
        # 初始化数据库，创建表weight
        self.conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS Weight (
                date TEXT PRIMARY KEY,
                weight REAL NOT NULL
            )
            '''
        )
        self.conn.commit()

    def add(self, record: WeightRecord) -> None:
        # 添加一条体重信息
        self.conn.execute(
            '''
            INSERT INTO Weight (date, weight)
            VALUES (?, ?)
            ON CONFLICT(date)
            DO UPDATE SET weight = excluded.weight
            ''',
            (
                record.date.isoformat(),
                record.weight,
            ),
        )
        self.conn.commit()

    def get_range(self, start: date, end: date) -> list[WeightRecord]:
        # 获取指定日期范围内的数据
        cursor = self.conn.execute(
            '''
            SELECT date, weight
            FROM Weight
            WHERE date BETWEEN ? AND ?
            ORDER BY date
            ''',
            (
                start.isoformat(),
                end.isoformat(),
            ),
        )

        return [ WeightRecord(date=date.fromisoformat(row[0]), weight=row[1]) for row in cursor]

    def get_all(self) -> list[WeightRecord]:
        # 获取全部数据
        cursor = self.conn.execute(
            '''
            SELECT date, weight
            FROM Weight
            ORDER BY date
            ''',
        )

        return [ WeightRecord(date=date.fromisoformat(row[0]), weight=row[1]) for row in cursor]
    def clean(self):
        # Clean all the data in the database
        self.conn.execute(
            '''
            DELETE FROM weight
            ''',
        )

        self.conn.commit()
