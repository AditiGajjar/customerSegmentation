# only run this once to generate random dataase
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

def generate_customers(num_customers):
    customers = []
    # to be more specific about probabilities of each status
    for _ in range(num_customers):
        marital_status = np.random.choice(
            ['Divorced', 'Married', 'Single'], 
            p=[0.1, 0.45, 0.45]
        )
        customer = {
            # Faker for fake id, city, and job
            # Numpy random for the rest
            'customer_id': fake.uuid4(),
            'age': np.random.randint(18, 70),
            'gender': fake.random_element(elements=('Male', 'Female')),
            'annual_income': round(np.random.uniform(20000, 150000), 2),
            'spending_score': np.random.randint(1, 101),
            'num_transactions': np.random.randint(1, 200),
            'avg_transaction_amount': round(np.random.uniform(10, 500), 2),
            'total_transaction_amount': round(np.random.uniform(500, 100000), 2),
            'location': fake.city(),
            'marital_status': marital_status,
            'occupation': fake.job(),
            'num_dependents': np.random.randint(0, 5)
        }
        customers.append(customer)
    return pd.DataFrame(customers)

# Generate 800,000 synthetic customers
num_customers = 800000
df_customers = generate_customers(num_customers)
# save to a file
df_customers.to_csv('synthetic_customers.csv', index=False)

