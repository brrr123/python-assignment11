import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT o.order_id, SUM(li.quantity * p.price) as total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""

df = pd.read_sql_query(query, conn)

def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

# Using cumsum
df['cumulative'] = df['total_price'].cumsum()


plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o')
plt.title('Cumulative Revenue by Order')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.grid(True)
plt.tight_layout()


plt.show()

conn.close()
