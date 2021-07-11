import re
import logging

from bs4 import BeautifulSoup
from locators.book_page_locator import BookPageLocator
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.all_books_page')


class BooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{BookPageLocator.BOOK}`.')
        locator = BookPageLocator.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalog pages available...')
        content = self.soup.select_one(BookPageLocator.PAGER).string.strip()
        logger.info(f'Found number of catalog pages available: `{content}`.')
        pattern = '\w+$'
        match = re.search(pattern, content)
        page_int = int(match.group(0))
        logger.debug(f'Extracted number of pages as integer: `{page_int}`.')
        return page_int
