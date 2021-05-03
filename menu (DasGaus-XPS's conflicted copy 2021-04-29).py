from app import books
from generator.book_generator import BookGenerator

book_gen = BookGenerator(books)


def print_best_books():
    print('------Top 5 Best Books------')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:5]
    for book in best_books:
        print(f'{book.title}.  {book.rating}/5 stars.')


def print_cheapest_books():
    print('------Top 5 Cheapest Books------')
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    for book in cheapest_books:
        print(f'{book.title}, ${book.price}.')


def get_user_choice():
    return input('''Enter one of the following:

- 'b' to look for 5-star books
- 'c' to look at the cheapest books
- 'n' to look at the next available book in the catalog
- 'q' to exit

Enter your choice: ''')


USER_CHOICE = get_user_choice()


while USER_CHOICE != 'q':
    if USER_CHOICE == 'b':
        print_best_books()
        USER_CHOICE = get_user_choice()
    elif USER_CHOICE == 'c':
        print_cheapest_books()
        USER_CHOICE = get_user_choice()
    elif USER_CHOICE == 'n':
        book_gen.next_book
        USER_CHOICE = get_user_choice()
    else:
        print('That is not a valid selection')
        USER_CHOICE = get_user_choice()
