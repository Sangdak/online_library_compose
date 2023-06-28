from http.server import HTTPServer, SimpleHTTPRequestHandler
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from more_itertools import chunked
import os
from pathlib import Path


BOOKS_ON_PAGE_AMOUNT = 20


def on_reload():
    books_db = get_books_data()
    book_db = [{k: v} for k, v in books_db.items()]

    os.makedirs('pages', exist_ok=True)

    books_divided_by_pages = chunked(book_db, BOOKS_ON_PAGE_AMOUNT)

    print(books_divided_by_pages)

    for page_number, page_content in enumerate(books_divided_by_pages, start=1):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html', 'xml'])
        )

        template = env.get_template('template.html')

        rendered_page = template.render(
            books=chunked(page_content, 2),
        )

        filepath = Path('pages', f'index{page_number}.html')
        with open(filepath, 'w', encoding="utf8") as file:
            file.write(rendered_page)

        print("Content refreshed")


def get_books_data():
    with open('results.json', 'r') as results:
        results_json = results.read()

    return json.loads(results_json)


def main():
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')


if __name__ == '__main__':
    main()
