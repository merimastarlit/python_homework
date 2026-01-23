import pandas as pd
import sqlite3

# Using with-statement for the database connection
with sqlite3.connect("../db/lesson.db") as conn:
    query = """
    SELECT
        line_items.line_item_id,
        line_items.quantity,
        products.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    """

    df = pd.read_sql_query(query, conn)

print("Initial DataFrame:")
print(df.head())

# adding a new column 'total' which is quantity * price
df['total'] = df['quantity'] * df['price']
print(df.head())

# adding groupby and aggregation
summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
})
print(summary.head(5))

# sorting the summary by product_name
sorted_df = summary.sort_values(by='product_name')
print(sorted_df.head(5))

# exporting the sorted summary to a CSV file
sorted_df.to_csv("order_summary.csv", index=False)
