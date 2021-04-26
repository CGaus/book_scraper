from app import books
from generators.book_generator import BookGenerator

book_list = BookGenerator(books)


def choose():
    choice = input('''
    Please select an option from the list below:

    Enter 'n' to display the next book
    Enter 'p' to display the previous book
    Enter 'c' to display the cheapest books
    Enter 'r' to display top rated books
    Enter 'q' to quit the program
    
    Enter your selection here: ''')

    while choice != 'q':
        if choice == 'n':
            next_book()
        elif choice == 'p':
            prev_book()
        elif choice == 'c':
            find_cheapest_book()
        elif choice == 'r':
            find_highest_rated()
        else:
            print('That is not a valid choice')
        choose()


def find_cheapest_book():
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    for book in cheapest_books:
        print(book)


def find_highest_rated():
    best_books = sorted(books, key=lambda x: x.rating*-1)[:5]
    for book in best_books:
        print(book)


def next_book():
    book_list.next_book


def prev_book():
    book_list.prev_book


choose()

