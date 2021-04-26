import requests

from pages.books import BooksPage

page_content = requests.get('http://books.toscrape.com/').content
page = BooksPage(page_content)
books = page.books
