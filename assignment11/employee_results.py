import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("../db/lesson.db")

sql_query = """
SELECT last_name, SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""

employee_results = pd.read_sql_query(sql_query, conn)

conn.close()

print(employee_results)


ax = employee_results.plot(
    kind='bar',
    x='last_name',
    y='revenue',
    color='skyblue',
    figsize=(10, 6)
)


plt.title('Employee Revenue', fontsize=16)
plt.xlabel('Employee', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45)


plt.show()
