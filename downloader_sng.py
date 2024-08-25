import requests
import urllib.parse
import os

def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def generate_download_url(file_path):
    file_path = file_path.replace(".\\", "https://github.com/ElliotCHEN37/project-tuyu/raw/main/").replace("\\", "/")
    if file_path.startswith('https://'):
        file_path = 'https://' + urllib.parse.quote(file_path[8:])
    return file_path

def download_file(url, destination):
    print(f"Downloading from {url}")
    response = requests.get(url)
    response.raise_for_status()
    with open(destination, 'wb') as f:
        f.write(response.content)

def main():
    print('''
=================================
| Welcome to                    |
| Project-Tuyu Downloader (SNG) |
| By ElliotCHEN37               |
| Only Support japanese title   |
| Titles were separated by "|"  |
=================================
    ''')
    
    print("Fetching song list...")
    json_url = "https://github.com/ElliotCHEN37/project-tuyu/raw/main/song_list.json"
    song_list = fetch_json(json_url)
    print("Fetched")
    
    titles = input("Title(s): ").strip().split('|')
    
    for title in titles:
        title = title.strip()
        if title in song_list:
            file_path = song_list[title]
            download_url = generate_download_url(file_path)
            
            file_name = os.path.basename(urllib.parse.unquote(download_url))
            download_file(download_url, file_name)
            print(f"File downloaded: {file_name}")
        else:
            print(f"Title '{title}' not listed")
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
