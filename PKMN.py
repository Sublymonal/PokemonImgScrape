import requests
from pathlib import Path
import os
from lxml import html
import urllib
import sys

userHomePath = Path.home() #current user's main directory
downloadFolderPath = userHomePath  / "Downloads" #downloads folder variable
scrapeFolderPath = downloadFolderPath / "scrape" #new folder variable for scrape folder
newFolder = os.path.join(downloadFolderPath, "scrape") #create new folder in downloads folder


print("Creating new folder in your downloads folder for the images")

if not os.path.exists(newFolder):
	os.mkdir(newFolder)

page = 0
lastPage = 51
cardNumber = 0
lastCard = 60
while page <= lastPage:
    page+=1
    card = 1
    counter = 1
    url = f"https://pkmncards.com/format/f-on-standard-2025/{page}"

    response = requests.get(url)


    print(response)#check if listening, will print out if new page

    #parse html
    tree = html.fromstring(response.content)

    while card <= lastCard:
        #img xpath
        xpath = f"/html/body/div/div/div/div[2]/main/article[{card}]/div/a/img"

        image_elements = tree.xpath(xpath)
        #print(counter) #uncomment to see the card number on page
        counter+=1

        # Download images
        for index, img in enumerate(image_elements):
            # Get the image source URL
            img_url = img.get('src') 
            # Download the image
            if cardNumber < 3992: #3992 is the last card number as of Paldean Fates
                img_name = f'image_{cardNumber}.jpg'
                img_path = os.path.join(scrapeFolderPath, img_name)
                urllib.request.urlretrieve(img_url, img_path)
                print(f"Downloaded: {img_name}")
                cardNumber += 1
                card+=1
            else:
                print("Download complete!!!")
                exit = input("Please press the return key to exit")
                sys.exit()
                
