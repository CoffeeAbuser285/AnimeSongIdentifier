from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import time

# Set up headless Chrome
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Open the website
driver.get("https://anisongdb.com/")
time.sleep(5)  # Wait for JS to load content

# Scroll to load more if infinite scroll (optional, for deep scraping)
# for _ in range(5):  # Adjust range for depth
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

# Parse the page
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

songs = []

# Extract all song entries
entries = soup.select(".song-entry")
for entry in entries:
    title = entry.select_one(".song-title")
    anime = entry.select_one(".anime-title")
    artist = entry.select_one(".song-artist")
    song_type = entry.select_one(".song-type")

    songs.append({
        "title": title.text.strip() if title else None,
        "anime": anime.text.strip() if anime else None,
        "artist": artist.text.strip() if artist else None,
        "type": song_type.text.strip() if song_type else None
    })

# Save to JSON
with open("anisongdb_songs.json", "w", encoding="utf-8") as f:
    json.dump(songs, f, indent=4, ensure_ascii=False)

print(f"✅ Scraped {len(songs)} songs and saved to anisongdb_songs.json")