import requests
import logging

from pages.books import BooksPage

logging.basicConfig()

page_content = requests.get('http://books.toscrape.com/catalogue/page-1.html').content
page = BooksPage(page_content)
books = page.books

for i in range(1, page.page_count):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html').content
    page = BooksPage(page_content)
    books.extend(page.books)
