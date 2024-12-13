from flask import Flask, render_template
import os
import json

app = Flask(__name__)

# Path to the JSON files
SONGS_FILE = 'songs.json'

def read_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

@app.route('/')
def index():
    songs = read_data(SONGS_FILE)
    return render_template('index.html', songs=songs)

@app.route('/song/<int:song_id>')
def song(song_id):
    songs = read_data(SONGS_FILE)
    song = next((song for song in songs if song['id'] == song_id), None)
    if song:
        return render_template('song.html', song=song)
    return "Song not found", 404

def generate_static_site():
    with app.test_request_context():
        # Generate index.html
        index_html = index()
        with open('static_site/index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)

        # Generate song pages
        songs = read_data(SONGS_FILE)
        for song in songs:
            song_html = song(song['id'])
            with open(f'static_site/song_{song["id"]}.html', 'w', encoding='utf-8') as f:
                f.write(song_html)

if __name__ == '__main__':
    app.run(debug=True)