import sqlite3
import logging
from pathlib import Path

import pandas as pd

DATA_DIR = Path('data/raw')
DB_PATH = Path('ecom.db')
LOG_PATH = Path('logs/etl.log')

TABLE_CONFIG = {
    'users': DATA_DIR / 'users.csv',
    'products': DATA_DIR / 'products.csv',
    'orders': DATA_DIR / 'orders.csv',
    'order_items': DATA_DIR / 'order_items.csv',
    'reviews': DATA_DIR / 'reviews.csv',
}


def setup_logging():
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )


def load_csv_to_sqlite(conn, table_name, csv_path):
    logging.info('Loading %s from %s', table_name, csv_path)
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    count = len(df)
    logging.info('Inserted %d rows into %s', count, table_name)
    print(f'{table_name}: {count} rows')


def main():
    setup_logging()
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        for table, csv_path in TABLE_CONFIG.items():
            if not csv_path.exists():
                logging.warning('CSV for %s not found at %s; skipping', table, csv_path)
                print(f'{table}: missing CSV, skipped')
                continue
            load_csv_to_sqlite(conn, table, csv_path)

    logging.info('ETL process completed.')


if __name__ == '__main__':
    main()

