from PIL import Image
import urllib.request
import Utils
import os
from pathlib import Path

from gameServices.CardService import CardService

BASE_URL = "https://images.ygoprodeck.com/images/cards/"
IMAGE_EXTENSION = ".jpg"
# HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
class YGOCardService(CardService):
    def getCardsFromFile(totalCards):
        cardImages = []
        cardCount = 0
        with open(Path.cwd()/'input'/'ygoInput.txt', 'r') as f:
            lines = f.readlines()
            f.close()
        for line in lines:
            cardImages.append(getCardById(line.rstrip()))
            cardCount += 1
            print("Loaded card: " + line.rstrip() + ", " + str(round(((cardCount/totalCards)*100), 2)) +"% done")
        return cardImages


def getCardById(id):
    urllib.request.urlretrieve((BASE_URL + id + IMAGE_EXTENSION), Utils.getTempFilePath())
    img = Image.open(Utils.getTempFilePath())
    img.getdata() ## Genuinamente no tengo idea por que pero hacer eso hace que la resolucion sea buena, sin esto es terrible (sleep no funciona)
    return img