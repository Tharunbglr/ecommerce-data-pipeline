import pandas as pd
from faker import Faker
from pathlib import Path
import random

OUTPUT_PATH = Path('data/raw/products.csv')
TOTAL_PRODUCTS = 20
CATEGORIES = [
    'Electronics',
    'Home & Kitchen',
    'Books',
    'Fashion',
    'Toys',
    'Sports',
    'Beauty'
]


def generate_products(total: int = TOTAL_PRODUCTS):
    fake = Faker()
    products = []
    for product_id in range(1, total + 1):
        products.append(
            {
                'product_id': product_id,
                'name': fake.catch_phrase(),
                'category': random.choice(CATEGORIES),
                'price': round(random.uniform(5.0, 500.0), 2),
                'stock': random.randint(0, 500)
            }
        )
    return pd.DataFrame(products)


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = generate_products()
    df.to_csv(OUTPUT_PATH, index=False)
    print(f'Saved {len(df)} products to {OUTPUT_PATH}')


if __name__ == '__main__':
    main()
