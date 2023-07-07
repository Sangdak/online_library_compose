# Project: Library layout for online and offline use.

This project is based on the `parse_tululu.py` script created earlier. For more details see: https://github.com/Sangdak/library_parsing__2/blob/master/README.md.

Using the above script you can download books by genre from the library and the files will automatically be placed in the appropriate folders:
1. information on all downloaded books - file `results.json` (in the root directory of the script).
2. Files of the downloaded books - in the folder `books`.
3. Picture files of the covers of the downloaded books (if any) - in the folder `images`.

File `main.py` contains a script for the automatic formation of pages of the library site.

## How to install

Python3.11, Git and Poetry must be installed beforehand.

1. Download the repository code:
```shell.
git clone <link to repository
```

2. Next, install poetry dependencies (run in the repository's root directory):
```shell
poetry install
```
3. optionally:
Run the ``parse_tulu.py'' script to download files from the library. See https://github.com/Sangdak/library_parsing__2/blob/master/README.md for details.

## Example run:
```shell
python main.py
```

The script itself generates pages from existing files and saves them into the `pages` directory.

Created pages can work locally without connecting to the network.

Try it by go to the link with your browser: [Open your library](http://127.0.0.1:5500/)

You can check out the look and feel of the site by following this link:
https://sangdak.github.io/online_library_compose/pages/index1.html

## Project goals

The code is written for educational purposes - this is a lesson in a course on Python and web development at [Devman](https://dvmn.org/).