
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Seed para reprodutibilidade
np.random.seed(42)

# Número de registros
num_customers = 1000
num_products = 500
num_transactions = 10000

# Gerar dados de clientes
customer_ids = [f'CUST{i:04d}' for i in range(num_customers)]
customer_data = {
    'customer_id': customer_ids,
    'age': np.random.randint(18, 70, num_customers),
    'gender': np.random.choice(['Male', 'Female', 'Other'], num_customers, p=[0.48, 0.48, 0.04]),
    'city': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba'], num_customers, p=[0.3, 0.2, 0.2, 0.15, 0.15]),
    'membership_level': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], num_customers, p=[0.4, 0.3, 0.2, 0.1])
}
customers_df = pd.DataFrame(customer_data)

# Gerar dados de produtos
product_ids = [f'PROD{i:04d}' for i in range(num_products)]
product_data = {
    'product_id': product_ids,
    'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Beauty'], num_products, p=[0.25, 0.25, 0.2, 0.15, 0.15]),
    'price': np.round(np.random.uniform(10, 1000, num_products), 2),
    'stock_quantity': np.random.randint(0, 500, num_products)
}
products_df = pd.DataFrame(product_data)

# Gerar dados de transações
transaction_data = {
    'transaction_id': [f'TRANS{i:05d}' for i in range(num_transactions)],
    'customer_id': np.random.choice(customer_ids, num_transactions),
    'product_id': np.random.choice(product_ids, num_transactions),
    'quantity': np.random.randint(1, 5, num_transactions),
    'transaction_date': [datetime.now() - timedelta(days=np.random.randint(0, 365)) for _ in range(num_transactions)],
    'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'Bank Transfer', 'Boleto'], num_transactions, p=[0.5, 0.3, 0.1, 0.1])
}
transactions_df = pd.DataFrame(transaction_data)

# Calcular o total da transação
transactions_df = transactions_df.merge(products_df[['product_id', 'price']], on='product_id', how='left')
transactions_df['total_price'] = transactions_df['quantity'] * transactions_df['price']

# Salvar os dados em arquivos CSV
customers_df.to_csv('data/customers.csv', index=False)
products_df.to_csv('data/products.csv', index=False)
transactions_df.to_csv('data/transactions.csv', index=False)

print('Datasets gerados com sucesso em ./data/')


