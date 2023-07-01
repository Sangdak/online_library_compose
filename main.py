import json
import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


BOOKS_ON_PAGE_AMOUNT = 20
NUMBER_COLUMNS_ON_PAGE = 2


def on_reload():
    books_db = get_books_data()
    book_db = [{k: v} for k, v in books_db.items()]

    os.makedirs('pages', exist_ok=True)

    books_divided_by_pages = list(chunked(book_db, BOOKS_ON_PAGE_AMOUNT))
    total_num_of_pages = len(books_divided_by_pages)

    for page_number, page_content in enumerate(books_divided_by_pages, start=1):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html', 'xml'])
        )

        template = env.get_template('template.html')

        rendered_page = template.render(
            books=chunked(page_content, NUMBER_COLUMNS_ON_PAGE),
            current_page_number=page_number,
            total_number_of_pages=total_num_of_pages,
        )

        filepath = Path('pages', f'index{page_number}.html')
        with open(filepath, 'w', encoding="utf8") as file:
            file.write(rendered_page)


def get_books_data():
    with open('media/results.json', 'r') as results:
        results_json = results.read()

    return json.loads(results_json)


if __name__ == '__main__':
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')
