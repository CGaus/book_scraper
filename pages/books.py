import re
from bs4 import BeautifulSoup

from locators.book_page_locator import BookPageLocator
from parsers.book_parser import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BookPageLocator.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        content = self.soup.select_one(BookPageLocator.PAGER).string.strip()
        pattern = '\w+$'
        match = re.search(pattern, content)
        page_int = int(match.group(0))
        return page_int
