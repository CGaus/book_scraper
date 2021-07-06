import requests
import logging

from pages.books import BooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')


page_content = requests.get('http://books.toscrape.com/catalogue/page-1.html').content
page = BooksPage(page_content)
books = page.books

for i in range(1, page.page_count):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html').content
    logger.debug('Creating BooksPage from page content.')
    page = BooksPage(page_content)
    books.extend(page.books)
