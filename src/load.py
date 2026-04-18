import sqlite3
from typing import List, Dict

class Load:
    """Class responsible for loading data into a relational SQLite database."""

    def __init__(self):
        pass

    def create_sqlite_table(
        self, universities_list: List[Dict], db_name: str, table_name: str
    ) -> None:
        """
        Creates a table and inserts the list of universities.

        Args:
            universities_list (List[Dict]): Data extracted from the API.
            db_name (str): The database filename (without .db extension).
            table_name (str): The name of the table to be created.
        """
        con = sqlite3.connect(f"{db_name}.db")
        c = con.cursor()

        c.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                country TEXT,
                state_province TEXT,
                web_pages TEXT,
                domains TEXT
            );
            """
        )

        for university in universities_list:
            c.execute(
                f"INSERT INTO {table_name} (name, country, state_province, web_pages, domains) VALUES (?,?,?,?,?);",
                (
                    university.get("name"),
                    university.get("country"),
                    university.get("state-province"),
                    ", ".join(university.get("web_pages", [])),
                    ", ".join(university.get("domains", [])),
                ),
            )

        con.commit()
        con.close()