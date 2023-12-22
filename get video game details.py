import requests
import re

def search_games_by_name(game_name):
    api_url = "https://api.rawg.io/api/games"

    params = {
        'key': 'YOUR_key',
        'search': game_name
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        game_data = response.json()
        return game_data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

game_name = input("give a video-game name : ")
game_data = search_games_by_name(game_name)

if game_data:
    game_data=game_data.get("results")
    print(f"name : ",game_data[0].get("name"))
    platforms = (game_data[0]["platforms"])
    plat=[]
    for platform in platforms:
        plat.append(platform["platform"]["name"])
    print("platforms : "," ".join(plat))
    stores = (game_data[0]["stores"])
    store = []
    for s in stores:
        store.append(s["store"]["name"])
    print("stores : " ," ".join(store))
    print(f"release date : ",game_data[0].get("released"))
    print("img link: ",game_data[0].get("background_image"))
    print("ratint : ",game_data[0].get("rating"))
    print("last update ",game_data[0].get("updated"))
    t=game_data[0]["tags"]
    tags=[]
    for tag in t:
        tag = tag["name"]
        if re.match("^[a-zA-Z]" , tag) :
            tags.append(tag)

    print("tags : "," ".join(tags))

else:
    print(f"No games found with the name '{game}'.")
