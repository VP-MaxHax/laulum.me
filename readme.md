# Seinäm.me

This project is a simple Flask application that generates a static site with songs about walls.

## Prerequisites

- Python 3.10 or higher
- Poetry

## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the dependencies using Poetry:

    ```sh
    poetry install
    ```

## Running the App

1. Activate the virtual environment:

    ```sh
    poetry shell
    ```

2. Run the Flask application:

    ```sh
    python app.py
    ```

3. Open your web browser and navigate to `http://127.0.0.1:5000` to view the app.

## Generating the Static Site

1. Run the [generate_static_site.py](http://_vscodecontentref_/0) script:

    ```sh
    python generate_static_site.py
    ```

2. The static site will be generated in the [static_site](http://_vscodecontentref_/1) directory.

## Project Structure

- [app.py](http://_vscodecontentref_/2): Main Flask application.
- [generate_static_site.py](http://_vscodecontentref_/3): Script to generate the static site.
- [songs.json](http://_vscodecontentref_/4): JSON file containing the songs.
- [static](http://_vscodecontentref_/5): Directory containing static files (images, CSS).
- [templates](http://_vscodecontentref_/6): Directory containing HTML templates.
- [pyproject.toml](http://_vscodecontentref_/7): Poetry configuration file.
- [poetry.lock](http://_vscodecontentref_/8): Poetry lock file.
- [readme.md](http://_vscodecontentref_/9): This file.

## License

This project is licensed under the MIT License.