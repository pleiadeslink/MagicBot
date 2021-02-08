import requests, json, os, random
from mastodon import Mastodon

# Mastodon token and domain
mastodon = Mastodon(
    access_token = "abcdef",
    api_base_url = "https://domain.com/"
)

# Get a random card
card = json.loads(requests.get("https://api.scryfall.com/cards/random").content)

# Save the card image
img = requests.get(card["image_uris"]["art_crop"]).content
with open("card.png", "wb") as png:
    png.write(img)

# Post in Mastodon
media = mastodon.media_post("card.png")
mastodon.status_post(card["name"] + "\nArtwork by " + card["artist"], media_ids=media)

# Delete the image, since it is no longer needed
os.remove("card.png")