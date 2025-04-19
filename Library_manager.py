import json

class PersonalLibraryManager:
    def _init_(self):
        self.library = []

    def add_book(self, title, author, year, genre, read_status):
        book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read_status': read_status
        }
        self.library.append(book)
        print(f'Added book: {title}')

    def remove_book(self, title):
        for book in self.library:
            if book['title'].lower() == title.lower():
                self.library.remove(book)
                print(f'Removed book: {title}')
                return
        print(f'Book not found: {title}')

    def search_books(self, search_term):
        results = [book for book in self.library if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]
        if results:
            for book in results:
                print(f"{book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {book['read_status']}")
        else:
            print('No books found.')

    def show_statistics(self):
        total_books = len(self.library)
        read_books = len([book for book in self.library if book['read_status']])
        unread_books = total_books - read_books
        print(f'Total books: {total_books}, Read: {read_books}, Unread: {unread_books}')

    def save_library(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.library, f)
        print(f'Library saved to {filename}')

    def load_library(self, filename):
        try:
            with open(filename, 'r') as f:
                self.library = json.load(f)
            print(f'Library loaded from {filename}')
        except FileNotFoundError:
            print(f'File not found: {filename}')

    def menu(self):
        while True:
            print("\nPersonal Library Manager")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Search Books")
            print("4. Show Statistics")
            print("5. Save Library")
            print("6. Load Library")
            print("7. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter author: ")
                year = input("Enter publication year: ")
                genre = input("Enter genre: ")
                read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'
                self.add_book(title, author, year, genre, read_status)
            elif choice == '2':
                title = input("Enter book title to remove: ")
                self.remove_book(title)
            elif choice == '3':
                search_term = input("Enter title or author to search: ")
                self.search_books(search_term)
            elif choice == '4':
                self.show_statistics()
            elif choice == '5':
                filename = input("Enter filename to save library: ")
                self.save_library(filename)
            elif choice == '6':
                filename = input("Enter filename to load library: ")
                self.load_library(filename)
            elif choice == '7':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library_manager = PersonalLibraryManager()
    library_manager.menu()
