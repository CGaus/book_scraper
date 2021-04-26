import re

from locators.book_locators import BookLocators

rating_dict = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}


class BookParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Title: {self.title}, Price: {self.price}, Rating: {self.rating} out of Five, In stock? {self.stock}>'

    @property
    def title(self):
        locator = BookLocators.TITLE
        return self.parent.select_one(locator)['title']

    @property
    def rating(self):
        locator = BookLocators.RATING
        rating_str = self.parent.select_one(locator)['class'][1]
        rating_int = rating_dict.get(rating_str)
        return rating_int

    @property
    def price(self):
        locator = BookLocators.PRICE
        price_str = self.parent.select_one(locator).string
        pattern = '[0-9]{1,}\.[0-9]{2}'
        match = re.search(pattern, price_str)
        price_fl = float(match.group(0))
        return price_fl

    @property
    def stock(self):
        locator = BookLocators.IN_STOCK
        in_stock = self.parent.select_one(locator)['class'][0]
        if in_stock == 'icon-ok':
            return 'Yes'
        else:
            return 'No'
