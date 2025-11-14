import pandas as pd
from faker import Faker
from pathlib import Path

OUTPUT_PATH = Path('data/raw/users.csv')
TOTAL_USERS = 20


def generate_users(total: int = TOTAL_USERS):
    fake = Faker()
    users = []
    for user_id in range(1, total + 1):
        users.append(
            {
                'user_id': user_id,
                'name': fake.name(),
                'email': fake.unique.email(),
                'address': fake.address().replace('\n', ', ')
            }
        )
    return pd.DataFrame(users)


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = generate_users()
    df.to_csv(OUTPUT_PATH, index=False)
    print(f'Saved {len(df)} users to {OUTPUT_PATH}')


if __name__ == '__main__':
    main()
