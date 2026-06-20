import pylast
import os
import json

def get_lastfm_client():
    network = pylast.LastFMNetwork(
        api_key=os.environ["LASTFM_API_KEY"],
        api_secret=os.environ["LASTFM_API_SECRET"]
    )
    print("Last.fm connected successfully")
    return network

def fetch_tracks(mood, limit=5):
    network = get_lastfm_client()
    tag = network.get_tag(mood)
    top_tracks = tag.get_top_tracks(limit=limit)
    results = []
    for item in top_tracks:
        track = item.item
        try:
            cover_image = track.get_cover_image()
        except Exception:
            cover_image = None
        song_data = {
            "song": track.get_title(),
            "artist": track.get_artist().get_name(),
            "cover_image": cover_image,
            "url": track.get_url()
        }
        results.append(song_data)
    return results

all_results = {}
for mood in ["joy", "sadness", "anger", "fear", "love", "surprise"]:
    all_results[mood] = fetch_tracks(mood)

with open("lastfm_results.json", "w") as f:
    json.dump(all_results, f, indent=2)

print("Saved to lastfm_results.json")