import requests
import time
import random

chapter = "20"
page = "3"
manga = "boruto_two_blue_vortex"
base_url = f"https://images.mangafreak.me/mangas/{manga}/{manga}_{chapter}/{manga}_{chapter}_{page}.jpg"
url = "https://images.mangafreak.me/mangas/boruto_two_blue_vortex/boruto_two_blue_vortex_20/boruto_two_blue_vortex_20_3.jpg"

for i in range(1,50):
    chapter = "20"
    page = str(i)
    base_url = f"https://images.mangafreak.me/mangas/{manga}/{manga}_{chapter}/{manga}_{chapter}_{page}.jpg"
    time.sleep(random.uniform(1, 3))
    response = requests.get(base_url, stream=True)
    if response.status_code == 200:
        with open(f"{manga}_{chapter}_{page}.jpg","wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    else:
        #this means we have reached the end of the page
        print(f"failed to dowload image {base_url}")
        break