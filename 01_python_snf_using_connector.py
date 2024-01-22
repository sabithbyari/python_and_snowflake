# Install the package
# pip install snowflake-connector-python

import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account_url',
    warehouse='your_warehouse',
    database='your_database'
)

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM your_table_name")

# Fetch the results
results = cur.fetchall()
print (results)
# Close the connection
cur.close()
conn.close()
