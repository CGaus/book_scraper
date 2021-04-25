class BookGenerator:
    def __init__(self, book_list):
        self.book_list = book_list
        self.list_iterator = 0

    @property
    def next_book(self):
        if self.list_iterator <= len(self.book_list):
            print(self.book_list[self.list_iterator])
            self.list_iterator += 1
        else:
            print('There are no more books in the list')
