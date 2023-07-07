import argparse
import json
import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


BOOKS_ON_PAGE_AMOUNT = 20
NUMBER_COLUMNS_ON_PAGE = 2


def on_reload(db_path='media/results.json'):
    with open(db_path, 'r') as results:
        books_db = json.load(results)

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
        with open(filepath, 'w', encoding='utf8') as file:
            file.write(rendered_page)


def main():
    parser = argparse.ArgumentParser(
        prog='get_books',
        description='Downloading books by category from "tululu.org".',
    )

    parser.add_argument(
        '--file',
        help='Specify filepath for json file with books'
             'data (by default "media/results.json").',
        type=str,
        default='media/results.json',
    )
    args = parser.parse_args()
    db_file_path = args.file

    on_reload(db_file_path)
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='./pages/index1.html')


if __name__ == '__main__':
    main()
