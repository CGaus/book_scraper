from app import books
from generators.book_generator import BookGenerator

book_list = BookGenerator(books)


def get_input():
    return input('''
    Please select an option from the list below:

    Enter 'n' to display the next book
    Enter 'p' to display the previous book
    Enter 'c' to display the cheapest books
    Enter 'r' to display top rated books
    Enter 'q' to quit the program
    
    Enter your selection here: ''')


def find_cheapest_book():
    print('---Top 5 Cheapest Books---')
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    for book in cheapest_books:
        print(book)


def find_highest_rated():
    print("---Top 5 Highest Rated Books---")
    best_books = sorted(books, key=lambda x: x.rating*-1)[:5]
    for book in best_books:
        print(book)


def next_book():
    book_list.next_book


def prev_book():
    book_list.prev_book


user_choices = {
    "n": next_book,
    "p": prev_book,
    "c": find_cheapest_book,
    "r": find_highest_rated,
}


def menu():
    user_input = get_input()

    while user_input != 'q':
        if user_input in user_choices:
            user_choices[user_input]()
        else:
            print('That is not a valid choice')
        user_input = get_input()


menu()

