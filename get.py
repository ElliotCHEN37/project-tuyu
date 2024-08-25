import os
import json
from tinytag import TinyTag

def get_title_from_file(file_path):
    try:
        tag = TinyTag.get(file_path)
        return tag.title
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def generate_song_list(directory):
    song_list = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mp3', '.flac')):
                file_path = os.path.join(root, file)
                title = get_title_from_file(file_path)
                if title:
                    song_list[title] = file_path
    return song_list

def write_song_list_to_json(song_list, json_file):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(song_list, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    directory = '.'
    json_file = 'song_list.json'
    song_list = generate_song_list(directory)
    write_song_list_to_json(song_list, json_file)
    print(f"Song list has been written to {json_file}")
