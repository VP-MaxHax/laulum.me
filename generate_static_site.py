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
    song_data = next((song for song in songs if song['id'] == song_id), None)
    if song_data:
        return render_template('song.html', song=song_data)
    return "Song not found", 404

def generate_static_site():
    output_dir = 'static_site'
    os.makedirs(output_dir, exist_ok=True)

    with app.test_request_context():
        # Generate index.html
        index_html = index()
        with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(index_html)

        # Generate song pages
        songs = read_data(SONGS_FILE)
        for song_data in songs:
            song_html = song(song_data['id'])
            with open(os.path.join(output_dir, f'song_{song_data["id"]}.html'), 'w', encoding='utf-8') as f:
                f.write(song_html)

if __name__ == '__main__':
    generate_static_site()