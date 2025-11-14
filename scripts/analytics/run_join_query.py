import sqlite3
from pathlib import Path

import pandas as pd

DB_PATH = Path('ecom.db')
QUERY_PATH = Path('sql/join_query.sql')
OUTPUT_PATH = Path('data/output/joined_output.csv')


def load_query():
    if not QUERY_PATH.exists():
        raise FileNotFoundError(f'Query file not found: {QUERY_PATH}')
    return QUERY_PATH.read_text()


def run_query(query: str):
    if not DB_PATH.exists():
        raise FileNotFoundError(f'Database not found: {DB_PATH}')

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(query, conn)
    return df


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    query = load_query()
    df = run_query(query)

    print(df)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f'Saved output to {OUTPUT_PATH}')


if __name__ == '__main__':
    main()

