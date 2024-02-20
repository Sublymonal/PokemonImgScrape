import requests
from pathlib import Path
import os
from lxml import html
import urllib
import sys

userHomePath = Path.home() #current user's main directory
downloadFolderPath = userHomePath  / "Downloads" / "scrape" #stores the user's downloads directory into a variable

page = 0
lastPage = 64
cardNumber = 0
lastCard = 60
while page <= lastPage:
    page+=1
    card = 1
    pageCounter = 1
    url = f"https://pkmncards.com/format/e-g-standard-2024/page/{page}"

    response = requests.get(url)


    print(response)#check if listening

    #parse html
    tree = html.fromstring(response.content)

    while card <= lastCard:
        #img xpath
        xpath = f"/html/body/div/div/div/div[2]/main/article[{card}]/div/a/img"

        image_elements = tree.xpath(xpath)
        print(pageCounter)
        pageCounter+=1

        # Download images
        for index, img in enumerate(image_elements):
            # Get the image source URL
            img_url = img.get('src') 
            # Download the image
            if img_url:
                img_name = f'image_{cardNumber}.jpg'
                img_path = os.path.join(downloadFolderPath, img_name)
                urllib.request.urlretrieve(img_url, img_path)
                print(f"Downloaded: {img_name}")
                cardNumber += 1
                card+=1
            else:
                print(f"No image URL found for element {index}")
                exit = input("Please press the return key to exit")
                sys.exit()
                