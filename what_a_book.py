# Nicholas Zeller
# CYBR410
# Assignment 12.3 WhatABook.py

import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    # Database Connection Configuration
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    # Display Main Menu
    print("\n   Main Menu: \n   What would you like to see?   \n")

    print("    1. Books\n    2. Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      Enter the number for the option you would like: '))
        return choice
    except ValueError:
        print("\n  Invalid option, exiting...\n")
        sys.exit(0)

def show_books(_cursor):
    # Show all books in database
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()
    print("\n  BOOK LISTINGS: \n")    
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[1], book[2], book[3]))

def show_locations(_cursor):
    # Show all store locations
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()
    print("\n  -- STORE LOCATIONS --\n")
    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def validate_user():
    # Validates user ID
    try:
        # Fetches user_ids in table user then compares input to that list
        cursor.execute("SELECT user_id FROM user")
        user_ids = [row[0] for row in cursor.fetchall()] 
        customer_id = int(input('\n  Enter a Customer ID: '))      
        if int(customer_id) in user_ids:
            return customer_id
        else:
            print("\n  Invalid Customer ID, exiting...\n")
            sys.exit(0)
    except ValueError:
        print("\n  Invalid Customer ID, exiting...\n")
        sys.exit(0)

def show_account_menu():
    #Display Customer Account Menu
    try:
        print("\n      Customer Menu:")
        print("        1. View Wishlist\n        2. Add Book\n        3. Return to Main Menu\n")
        account_menu_choice = int(input('      \nEnter the number for the option you would like: '))
        return account_menu_choice
    except ValueError:
        print("\n  Invalid option, exiting...\n")
        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    #Query DB and display user's wishlist
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))    
    wishlist = _cursor.fetchall()
    print("\n        Customer Wishlist:\n")
    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def list_available_books(_cursor, _user_id):
    # Display books not in customer's wishlist
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        AVAILABLE BOOKS:")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n        Book Author: {}\n".format(book[0], book[1], book[2]))

def validate_book_id():
    # Validates selected book to add to wishlist
    try:
        # Fetches book_ids in table book then compares input to that list
        cursor.execute("SELECT book_id FROM book")
        book_ids = [row[0] for row in cursor.fetchall()]      
        if int(book_id_to_add) in book_ids:
            return book_id_to_add
        else:
            print("\n  Invalid Book ID, exiting...\n")
            sys.exit(0)
    except ValueError:
        print("\n  Invalid Book ID, exiting...\n")
        sys.exit(0)

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    # Adds selected book to wishlist
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    print("\n  Welcome to WhatABook! ")
    user_selection = show_menu()
    # User Interactions
    while user_selection != 4:

        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                if account_option == 2:
                    list_available_books(cursor, my_user_id)
                    book_id_to_add = int(input('\n  Enter a Book ID: '))
                    book_id_to_add = validate_book_id()
                    add_book_to_wishlist(cursor, my_user_id, book_id_to_add)
                    db.commit()
                    print("\n        Book id: {} was added to your wishlist!".format(book_id_to_add))

                account_option = show_account_menu()
        
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please try again...")
            
        user_selection = show_menu()

    print("\n\n  Exiing Program...")

except mysql.connector.Error as err:
    # Connection Error Handling 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()