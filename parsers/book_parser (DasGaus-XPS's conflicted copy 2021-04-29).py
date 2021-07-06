import re

from locators.book_locators import BookLocators


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Title: {self.title}, Price: {self.price}, Rating: {self.rating}/5, In stock? {self.stock}>\n ' \
               f'Link: {self.link}'

    @property
    def title(self):
        locator = BookLocators.TITLE
        return self.parent.select_one(locator)['title']

    @property
    def rating(self):
        locator = BookLocators.RATING
        string_rating = self.parent.select_one(locator)['class'][1]
        number_rating = BookParser.RATINGS.get(string_rating)
        return number_rating

    @property
    def price(self):
        locator = BookLocators.PRICE
        item_price_initial = self.parent.select_one(locator).string
        pattern = '[0-9]{1,}\.[0-9]{2}'
        match = re.search(pattern, item_price_initial)
        item_price = float(match.group(0))
        return item_price

    @property
    def link(self):
        locator = BookLocators.LINK
        return self.parent.select_one(locator)['href']

    @property
    def stock(self):
        locator = BookLocators.IN_STOCK
        in_stock = self.parent.select_one(locator)['class'][0]
        if in_stock == 'icon-ok':
            return 'Yes'
        else:
            return 'No'
