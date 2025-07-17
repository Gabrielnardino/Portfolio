
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os datasets
customers_df = pd.read_csv("Base de Dados\customers.csv")
products_df = pd.read_csv("Base de Dados\products.csv")
transactions_df = pd.read_csv(r"Base de Dados\transactions.csv")

# Converter 'transaction_date' para datetime
transactions_df["transaction_date"] = pd.to_datetime(transactions_df["transaction_date"])

# 1. Performance de Vendas
# Receita total
total_revenue = transactions_df["total_price"].sum()
print(f"Receita Total: R${total_revenue:,.2f}\n")

# Vendas mensais
transactions_df["month"] = transactions_df["transaction_date"].dt.to_period("M")
monthly_sales = transactions_df.groupby("month")["total_price"].sum()
print("Vendas Mensais:\n", monthly_sales)

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line")
plt.title("Receita Mensal")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.grid(True)
plt.tight_layout()
plt.savefig("Dashboards/monthly_revenue.png")
plt.close()

# Produto mais vendido (quantidade)
product_quantity = transactions_df.groupby("product_id")["quantity"].sum().sort_values(ascending=False)
most_sold_product_id = product_quantity.index[0]
most_sold_product_name = products_df[products_df["product_id"] == most_sold_product_id]["category"].iloc[0] # Usando categoria como 'nome' para simplificar
print(f"\nProduto mais vendido (quantidade): {most_sold_product_name} ({most_sold_product_id})")

# Produto mais lucrativo (receita)
product_revenue = transactions_df.groupby("product_id")["total_price"].sum().sort_values(ascending=False)
most_profitable_product_id = product_revenue.index[0]
most_profitable_product_name = products_df[products_df["product_id"] == most_profitable_product_id]["category"].iloc[0]
print(f"Produto mais lucrativo (receita): {most_profitable_product_name} ({most_profitable_product_id})")

# Categoria de produto mais lucrativa
category_revenue = transactions_df.merge(products_df[["product_id", "category"]], on="product_id")
category_revenue_sum = category_revenue.groupby("category")["total_price"].sum().sort_values(ascending=False)
print("\nReceita por Categoria:\n", category_revenue_sum)

plt.figure(figsize=(10, 6))
sns.barplot(x=category_revenue_sum.index, y=category_revenue_sum.values)
plt.title("Receita por Categoria de Produto")
plt.xlabel("Categoria")
plt.ylabel("Receita (R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("Dashboards/revenue_by_category.png")
plt.close()

# 2. Comportamento do Cliente
# Distribuição de idade
plt.figure(figsize=(10, 6))
sns.histplot(customers_df["age"], bins=10, kde=True)
plt.title("Distribuição de Idade dos Clientes")
plt.xlabel("Idade")
plt.ylabel("Número de Clientes")
plt.tight_layout()
plt.savefig("Dashboards/customer_age_distribution.png")
plt.close()

# Top 10 clientes por gasto
customer_total_spent = transactions_df.groupby("customer_id")["total_price"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Clientes por Gasto:\n", customer_total_spent)

# 4. Métodos de Pagamento
# Método de pagamento mais utilizado
payment_method_counts = transactions_df["payment_method"].value_counts()
print("\nMétodos de Pagamento mais utilizados:\n", payment_method_counts)

plt.figure(figsize=(8, 8))
plt.pie(payment_method_counts, labels=payment_method_counts.index, autopct="%1.1f%%")
plt.title("Distribuição de Métodos de Pagamento")
plt.tight_layout()
plt.savefig("Dashboards/payment_method_distribution.png")
plt.close()

print("\nAnálise concluída e gráficos salvos como PNGs.")


