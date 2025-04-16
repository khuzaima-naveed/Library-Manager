import json
import os

data_file = "library.txt"  # File to store book data

def load_libarary(): # Load the library data from the file
    # """Load the library data from the file."""
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file)

def add_book(library): # Add a new book to the library
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"


    new_book = { 
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
#to add a new book to the library
    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully.")

# def remove_book(library): # Remove a book from the library
#     title = input("Enter the title of the book to remove: ")
#     for book in library:
#         if book['title'].lower() == title.lower():
#             library.remove(book)
#             save_library(library)
#             print(f"Book '{title}' removed successfully.")
#             return
#     print(f"Book '{title}' not found in the library.")
        

def remove_book(library): # Remove a book from the library
    title = input("Enter the title of the book to remove: ")        
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title.lower()]
    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' removed successfully.")

    else:
        print(f"Book '{title}' not found in the library.")    

def search_library(library): # Search for a book in the library
    search_by = input("Search by title or author:").lower()
    search_term = input(f"Enter the {search_by}: ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"{book["title"]} by {book["author"]} - {book["year"]}-{book["genre"]} - {status}")

    else:
        print(f"No books found for {search_by}: {search_term}")        

def display_all_books(library): # Display all books in the library
       if library:
            for book in library:
                status = "Read" if book['read'] else "Unread"
                print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
       else:
                 print("No books in the library.")


def dispaly_statics(library): # Display statistics about the library
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0           
     
    print(f"Total books: {total_books}") 
    print(f"Books read: {percentage_read:.2f}%")


def menu (): # Display the main menu
    library = load_libarary()
    while True:
        print("Welcome to the Personal Library Manager")
        print("Menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2": 
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            dispaly_statics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")    

if __name__ == "__main__":
    menu()        

