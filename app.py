import requests

from pages.books import BooksPage

page_content = requests.get('http://books.toscrape.com/catalogue/page-1.html').content
page = BooksPage(page_content)
books = page.books

for i in range(1, 51):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html').content
    page = BooksPage(page_content)
    books.extend(page.books)
