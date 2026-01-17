import sqlite3

# Task 3: Creating functions to each table to add data to the tables
def add_magazine(cursor, title, publisher_id):
    try:
        cursor.execute("SELECT * FROM Magazines WHERE title = ?", (title,))
        result = cursor.fetchone()
        if result is not None:
            print(f"Magazine {title} is already in the database.")
            return result[0]
        cursor.execute(
            "INSERT INTO Magazines (title, publisher_id) VALUES (?, ?)", (title, publisher_id))
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Magazine {title} caused an error.")


def add_publisher(cursor, name, established_year):
    try:
        cursor.execute(
            "SELECT publisher_id FROM Publishers WHERE name = ?", (name,))
        result = cursor.fetchone()
        if result:
            print(f"Publisher {name} is already in the database.")
            return result[0]
        cursor.execute(
            "INSERT INTO Publishers (name, established_year) VALUES (?, ?)", (name, established_year))
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Publisher {name} caused an error.")
        return None


def add_subscriber(cursor, subscriber_name, address):
    try:
        cursor.execute(
            "SELECT * FROM Subscribers WHERE subscriber_name = ? AND address = ?", (subscriber_name, address))
        result = cursor.fetchone()
        if result is not None:
            print(
                f"Subscriber {subscriber_name} with address {address} is already in the database.")
            return result[0]
        cursor.execute(
            "INSERT INTO Subscribers (subscriber_name, address) VALUES (?, ?)", (subscriber_name, address))
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Subscriber {subscriber_name} caused an error.")


def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("""
            SELECT * FROM Subscriptions
            WHERE subscriber_id = ? AND magazine_id = ?
        """, (subscriber_id, magazine_id))
        result = cursor.fetchone()
        if result is not None:
            print("Subscription already exists.")
            return
        cursor.execute("""
            INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
        """, (subscriber_id, magazine_id, expiration_date))
    except sqlite3.IntegrityError:
        print("Subscription caused an error.")


# Task 1: Connect to the database
# writing inside try-except block to catch potential errors
try:
    # Connect to the database
    with sqlite3.connect("../db/magazines.db") as conn:
        #Task 3: adding the foreign keys
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        print("Connection to the database was successful.")

        # Task 2: Create the tables
        # Creating tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        established_year INTEGER
        )
        
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
        )
        """)

    print("Tables created successfully.")

    #Task 3: Inserting 3 samples of data into each table
    # Add publishers and store their IDs
    publisher1_id = add_publisher(cursor, 'ABC', 2003)
    publisher2_id = add_publisher(cursor, 'NYT', 2005)
    publisher3_id = add_publisher(cursor, 'LAT', 2008)

    # Add magazines with the correct publisher IDs
    mag1_id = add_magazine(cursor, 'Tech Today', publisher1_id)
    mag2_id = add_magazine(cursor, 'IT Innovation', publisher2_id)
    mag3_id = add_magazine(cursor, 'Tech Tomorrow', publisher3_id)

    # Add subscribers
    sub1_id = add_subscriber(cursor, 'John Doe', '234 Main St')
    sub2_id = add_subscriber(cursor, 'Jane Smith', '123 North St')
    sub3_id = add_subscriber(cursor, 'Albi Bee', '125 South St')

    # Add subscriptions using real IDs
    add_subscription(cursor, sub1_id, mag1_id, '2025-06-01')
    add_subscription(cursor, sub2_id, mag2_id, '2025-07-01')
    add_subscription(cursor, sub3_id, mag3_id, '2025-08-01')

    # Commiting the changes to the database to save the inserted data
    conn.commit()
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")

    # Task 4: Querying the database

    #Writing a query to retrieve all information from the subscribers table
    cursor.execute("SELECT * FROM Subscribers")
    subscribers = cursor.fetchall()
    print("All subscribers:")
    for row in subscribers:
        print(row)

    # Writing a query to retrieve all magazines sorted by name
    cursor.execute("SELECT * FROM Magazines ORDER BY title ASC")
    magazines = cursor.fetchall()
    print("All magazines sorted by title:")
    for row in magazines:
        print(row)

    #Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN
    cursor.execute("""
        SELECT Magazines.*
        FROM Magazines
        JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id
        WHERE Publishers.name = ?
    """, ('ABC',))
    abc_mags = cursor.fetchall()
    print("Magazines published by ABC:")
    for row in abc_mags:
        print(row)

# End of the try block with except to catch potential errors
except sqlite3.Error as e:
    print(f"An error occurred while connecting to the database: {e}")
