import pandas as pd
from faker import Faker
from pathlib import Path
import random
from datetime import datetime, timedelta

OUTPUT_PATH = Path('data/raw/orders.csv')
TOTAL_ORDERS = 30
USER_ID_RANGE = (1, 20)
RECENT_DAYS = 30


def generate_orders(total: int = TOTAL_ORDERS):
    fake = Faker()
    orders = []
    for order_id in range(1, total + 1):
        order_date = datetime.now() - timedelta(days=random.randint(0, RECENT_DAYS))
        orders.append(
            {
                'order_id': order_id,
                'user_id': random.randint(*USER_ID_RANGE),
                'order_date': order_date.strftime('%Y-%m-%d'),
                'total_amount': round(random.uniform(10.0, 1000.0), 2)
            }
        )
    return pd.DataFrame(orders)


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = generate_orders()
    df.to_csv(OUTPUT_PATH, index=False)
    print(f'Saved {len(df)} orders to {OUTPUT_PATH}')


if __name__ == '__main__':
    main()
import pandas as pd
from faker import Faker
from pathlib import Path
import random
from datetime import datetime, timedelta

OUTPUT_PATH = Path('data/raw/orders.csv')
TOTAL_ORDERS = 30
USER_ID_RANGE = (1, 20)
RECENT_DAYS = 30


def generate_orders(total: int = TOTAL_ORDERS):
    fake = Faker()
    orders = []
    for order_id in range(1, total + 1):
        order_date = datetime.now() - timedelta(days=random.randint(0, RECENT_DAYS))
        orders.append(
            {
                'order_id': order_id,
                'user_id': random.randint(*USER_ID_RANGE),
                'order_date': order_date.strftime('%Y-%m-%d'),
                'total_amount': round(random.uniform(10.0, 1000.0), 2)
            }
        )
    return pd.DataFrame(orders)


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = generate_orders()
    df.to_csv(OUTPUT_PATH, index=False)
    print(f'Saved {len(df)} orders to {OUTPUT_PATH}')


if __name__ == '__main__':
    main()
