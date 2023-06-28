from http.server import HTTPServer, SimpleHTTPRequestHandler
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json


def on_reload():
    books_db = get_books_data()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        books=books_db,
    )

    with open('index.html', 'w', encoding="utf8") as file:
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
