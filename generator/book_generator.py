class BookGenerator:
    def __init__(self, book_list):
        self.list = book_list
        self.num = 0

    @property
    def next_book(self):
        if self.num <= len(self.list):
            print(self.list[self.num])
            self.num += 1
        else:
            print('There are no more books in the list')
