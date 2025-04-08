#  I'm going to import sqlite3 to create a database for the eBookstore
import sqlite3

#  I'm going to create a file called eBookstore.db
#  I'm going to create a cursor object to execute SQL commands
def intialize_db():
    db = sqlite3.connect('eBookstore.db')
    cursor = db.cursor()
    #  I'm going to create a table called books with the following columns:
    #  id, title, author, quantity
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
#  I'm going to add some books with their ID to the table
    books = [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, 'Harry Potter and The Philosophers Stone', 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12),
    ]
#  I'm going to insert the books into the table
#  And check if they already exist
    for book in books:
        cursor.execute("SELECT * FROM books WHERE id = ?", (book[0],))
        existing = cursor.fetchone()
        if not existing:
            cursor.execute("INSERT INTO books (id, title, author, quantity) VALUES (?, ?, ?, ?)", book)
#  I'm going to commit the changes to the database
    db.commit()
#  I'm going to close the connection to the database
    db.close()

#  Create a programme that can be used by a bookstore clerk
#  Create a menu that displays the following options:
#  1. Add new books
#  2. Update book information
#  3. Delete books from the database
#  4. Search database for specific books
#  0. Exit the programme

#  Create menu options that will allow the user to select
#  the option they want to perform.
def display_menu():
    print("Welcome to the eBookstore Management System")
    print("Please select an option:")
    print("1. Add new books")
    print("2. Update book information")
    print("3. Delete books from the database")
    print("4. Search database for specific books")
    print("0. Exit")

#  1. Created function to update the book information.
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    quantity = int(input("Enter the quantity of the books: "))
    #  I'm going to create a connection to the database
    #  I'm going to create a cursor object to execute SQL commands
    conn = sqlite3.connect('eBookstore.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)
    ''', (title, author, quantity))
    conn.commit()
    conn.close()
    print(f"Book '{title}' added successfully!")

#  2. Created function to update the book information.
def update_book():
    book_id = input("Enter the ID of the book: ")
    #  I'm going to create a connection to the database
    #  I'm going to create a cursor object to execute SQL commands
    conn = sqlite3.connect('eBookstore.db')
    cursor = conn.cursor()
    cursor.execute('''0
        SELECT * FROM books WHERE id = ?
    ''', (book_id,))
    book = cursor.fetchone()

    if book:
        new_title = input("Enter the new title (leave blank to keep current): ")
        new_author = input("Enter the new author (leave blank to keep current): ")
        new_quantity = input("Enter the new quantity (leave blank to keep current): ")

        updated_title = new_title if new_title else book[1]
        updated_author = new_author if new_author else book[2]
        updated_quantity = int(new_quantity) if new_quantity else book[3]

        cursor.execute('''
            UPDATE books
            SET title = ?, author =?, quantity = ?
            WHERE id = ?
        ''', (updated_title, updated_author, updated_quantity, book_id))

        conn.commit()
        print(f"Book ID {book_id} updated successfully.")
    else:
        print(f"No book with that ID found {book_id}")

    conn.close()

#  3. Created function to delete a book from the database.
def delete_book():
    book_id = input("Enter the ID of the book you want to delete: ")
    #  I'm going to create a connection to the database
    #  I'm going to create a cursor object to execute SQL commands
    conn = sqlite3.connect("eBookstore.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id))
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No book with that ID found {book_id}.")
    else:
        print(f"Book ID {book_id} has been successfully deleted.")

    conn.close()

#  4. Created function to search for a specific book in the database.
def search_book():
    title = input("Enter the title of the book you want to search for: ")

    conn = sqlite3.connect("eBookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    result = cursor.fetchone()

    if result:
        print(f"""
            Book found:
            ID: {result[0]}
            Title: {result[1]}
            Author: {result[2]}
            Quantity: {result[3]}
            """)
    else:
        print(f"Book '{title}' not found.")

    conn.close()

#  This is the main function that will run the programme
#  It will display the menu and call the appropriate functions
#  based on user's input.
def main():
    intialize_db()
    while True:
        display_menu()
        choice = input("Enter your choice from 0-4: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_book()
        elif choice == '0':
            print("Exiting the programme. See ya later!")
            break
        else:
            print("Not a valid choice. Please try again.")
#  Run the main function to start the programme
#  This code creates a simple bookstore management system
#  that allows the user to add, update, delete, and search for books
if __name__ == "__main__":
    main()
