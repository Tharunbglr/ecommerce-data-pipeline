import pandas as pd
from pathlib import Path
import random

ORDERS_PATH = Path('data/raw/orders.csv')
PRODUCTS_PATH = Path('data/raw/products.csv')
OUTPUT_PATH = Path('data/raw/order_items.csv')
TOTAL_ORDER_ITEMS = 40


def load_source_data():
    orders = pd.read_csv(ORDERS_PATH)
    products = pd.read_csv(PRODUCTS_PATH)
    return orders['order_id'].tolist(), products['product_id'].tolist()


def generate_order_items(total: int = TOTAL_ORDER_ITEMS):
    order_ids, product_ids = load_source_data()
    if not order_ids or not product_ids:
        raise ValueError('Orders and products data must exist before generating order items.')

    order_items = []
    for item_id in range(1, total + 1):
        order_items.append(
            {
                'order_item_id': item_id,
                'order_id': random.choice(order_ids),
                'product_id': random.choice(product_ids),
                'quantity': random.randint(1, 5),
                'unit_price': round(random.uniform(5.0, 500.0), 2)
            }
        )
    return pd.DataFrame(order_items)


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = generate_order_items()
    df.to_csv(OUTPUT_PATH, index=False)
    print(f'Saved {len(df)} order items to {OUTPUT_PATH}')


if __name__ == '__main__':
    main()

