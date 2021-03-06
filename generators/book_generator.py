class BookGenerator:
    def __init__(self, book_list):
        self.book_list = book_list
        self.list_iterator = 0

    @property
    def next_book(self):
        if self.list_iterator == 0:
            print(self.book_list[self.list_iterator])
            self.list_iterator += 1
        elif self.list_iterator < len(self.book_list):
            self.list_iterator += 1
            print(self.book_list[self.list_iterator])
        else:
            print('You are at the end of the list')
            print(self.book_list[self.list_iterator])

    @property
    def prev_book(self):
        if self.list_iterator == 0:
            print("You are at the beginning of the list")
            print(self.book_list[self.list_iterator])
        else:
            self.list_iterator -= 1
            print(self.book_list[self.list_iterator])
