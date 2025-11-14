import pandas as pd
from pathlib import Path
import random
from faker import Faker
from datetime import datetime, timedelta

USERS_PATH = Path('data/raw/users.csv')
PRODUCTS_PATH = Path('data/raw/products.csv')
OUTPUT_PATH = Path('data/raw/reviews.csv')
TOTAL_REVIEWS = 25
RECENT_DAYS = 60


def load_source_data():
    users = pd.read_csv(USERS_PATH)
    products = pd.read_csv(PRODUCTS_PATH)
    return users['user_id'].tolist(), products['product_id'].tolist()


def generate_reviews(total: int = TOTAL_REVIEWS):
    fake = Faker()
    user_ids, product_ids = load_source_data()

    if not user_ids or not product_ids:
        raise ValueError('Users and products data must exist before generating reviews.')

    reviews = []
    for review_id in range(1, total + 1):
        review_date = datetime.now() - timedelta(days=random.randint(0, RECENT_DAYS))
        reviews.append(
            {
                'review_id': review_id,
                'user_id': random.choice(user_ids),
                'product_id': random.choice(product_ids),
                'rating': random.randint(1, 5),
                'review_date': review_date.strftime('%Y-%m-%d'),
                'comment': fake.sentence(nb_words=12)
            }
        )
    return pd.DataFrame(reviews)


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = generate_reviews()
    df.to_csv(OUTPUT_PATH, index=False)
    print(f'Saved {len(df)} reviews to {OUTPUT_PATH}')


if __name__ == '__main__':
    main()

