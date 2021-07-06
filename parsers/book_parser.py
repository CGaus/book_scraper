import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')

rating_dict = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}


class BookParser:
    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Title: {self.title}, Price: {self.price}, Rating: {self.rating} out of Five, In stock? {self.stock}>'

    @property
    def title(self):
        logger.debug('Finding book name...')
        locator = BookLocators.TITLE
        book_name = self.parent.select_one(locator)['title']
        logging.debug(f'Found book name, `{book_name}`.')
        return book_name

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING
        rating_str = self.parent.select_one(locator)['class'][1]
        rating_int = rating_dict.get(rating_str)
        logging.debug(f'Found book rating, `{rating_int}`.')
        return rating_int

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE
        price_str = self.parent.select_one(locator).string
        pattern = '[0-9]{1,}\.[0-9]{2}'
        match = re.search(pattern, price_str)
        price_fl = float(match.group(0))
        logging.debug(f'Found book price, $`{price_fl}`.')
        return price_fl

    @property
    def stock(self):
        locator = BookLocators.IN_STOCK
        in_stock = self.parent.select_one(locator)['class'][0]
        if in_stock == 'icon-ok':
            return 'Yes'
        else:
            return 'No'
