from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Path to the JSON files
DATA_FILE = 'data.json'
SONGS_FILE = 'songs.json'

def read_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def write_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    data = read_data(DATA_FILE)
    songs = read_data(SONGS_FILE)
    return render_template('index.html', data=data, songs=songs)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        data = read_data(DATA_FILE)
        data.append({'name': name})
        write_data(DATA_FILE, data)
        return redirect('/')

@app.route('/song/<int:song_id>')
def song(song_id):
    songs = read_data(SONGS_FILE)
    song = next((song for song in songs if song['id'] == song_id), None)
    if song:
        return render_template('song.html', song=song)
    return "Song not found", 404

@app.route('/new', methods=['GET', 'POST'])
def new_song():
    if request.method == 'POST':
        title = request.form['title']
        lyrics = request.form['lyrics']
        songs = read_data(SONGS_FILE)
        new_id = max(song['id'] for song in songs) + 1 if songs else 1
        new_song = {
            'id': new_id,
            'title': title,
            'lyrics': lyrics
        }
        songs.append(new_song)
        write_data(SONGS_FILE, songs)
        return redirect(url_for('song', song_id=new_id))

    return render_template('new_song.html')

if __name__ == '__main__':
    app.run(debug=True)