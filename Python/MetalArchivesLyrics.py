import requests
from bs4 import BeautifulSoup
#song = input("enter id")
band,album,song = input("enter band album song separated by |\n>").split("|")
albumpage = requests.get(f"https://www.metal-archives.com/albums/{band}/{album}")
soup = BeautifulSoup(albumpage.text, 'html.parser')

# Find the table
table = soup.find('table', class_='display table_lyrics')

# Iterate over table rows
for row in table.find_all('tr', class_=['even', 'odd']):
    # Extract song name and ID
    song_name = row.find('td', class_='wrapWords').text.strip()
    song_id = row.find('a', class_='anchor')['name'].replace(' ', '')[:]
    # Check if the song names match
    if song_name == song:
        print(f"Song ID for '{song}': {song_id}")
        break


lyrics = requests.get(f"https://www.metal-archives.com/release/ajax-view-lyrics/id/{song_id}")
lyrics = lyrics.text.replace("<br />","")
print(lyrics)
