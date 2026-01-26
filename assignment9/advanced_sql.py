# Task 1

import datetime
import sqlite3

# Connecting to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Aggregation with GROUP BY
query = """
SELECT orders.order_id AS order_id,
       SUM(products.price * line_items.quantity) AS total_price
FROM line_items
JOIN orders ON line_items.order_id = orders.order_id
JOIN products ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id
LIMIT 5;


"""

# Execute and fetch results
cursor.execute(query)
results_task1 = cursor.fetchall()
print(results_task1)

conn.close()


# Task 2

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Aggregation with LEFT JOIN
query2 = """

SELECT customers.customer_name, AVG(subquery.total_price) AS average_total_price
FROM customers
LEFT JOIN (
    SELECT orders.customer_id AS customer_id_b,
           SUM(products.price * line_items.quantity) AS total_price
    FROM line_items
    JOIN orders ON line_items.order_id = orders.order_id
    JOIN products ON line_items.product_id = products.product_id
    GROUP BY line_items.order_id
) AS subquery
ON customers.customer_id = subquery.customer_id_b
GROUP BY customers.customer_id;


"""

# Execute and fetch results
cursor.execute(query2)
results_task2 = cursor.fetchall()
print(results_task2)

conn.close()


# Task 3


conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

try:
    # Step 1: Getting the customer_id
    cursor.execute("""
        SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';
    """)
    customer_id = cursor.fetchone()[0]

    # Step 2: Getting the employee_id
    cursor.execute("""
        SELECT employee_id FROM employees 
        WHERE first_name = 'Miranda' AND last_name = 'Harris';
    """)
    employee_id = cursor.fetchone()[0]

    # Step 3: Getting product_ids
    cursor.execute("""
        SELECT product_id FROM products ORDER BY price LIMIT 5;
    """)
    product_ids = [row[0] for row in cursor.fetchall()]

    # Step 4: Inserting new order
    order_date = datetime.date.today().isoformat()
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id, date)
        VALUES (?, ?, ?)
        RETURNING order_id;
    """, (customer_id, employee_id, order_date))
    order_id = cursor.fetchone()[0]

    # Step 5: Inserting line items
    for product_id in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?);
        """, (order_id, product_id, 10))

    # Step 6: Confirming with SELECT
    cursor.execute("""
        SELECT line_items.line_item_id, products.product_name, line_items.quantity
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
        WHERE line_items.order_id = ?;
    """, (order_id,))

    results = cursor.fetchall()
    for row in results:
        print(row)

    # Step 7: Commiting the transaction
    conn.commit()

except Exception as e:
    print("Something went wrong. Rolling back...")
    conn.rollback()
    print("Error:", e)

# Closing the connection
finally:
    conn.close()


# Task 4

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Aggregation with HAVING
query4 = """
SELECT e.employee_id, e.first_name, e.last_name, 
       COUNT(orders.order_id) AS order_count
FROM employees AS e
JOIN orders ON e.employee_id = orders.employee_id
GROUP BY e.employee_id
HAVING COUNT(orders.order_id) > 5;

"""

# Execute and fetch results
cursor.execute(query4)
results4 = cursor.fetchall()
print(results4)

conn.close()
