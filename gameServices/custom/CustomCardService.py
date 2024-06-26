from PIL import Image, ImageFile
import urllib.request
import Utils
import json
import os

from gameServices.CardService import CardService

class CustomCardService(CardService):
    def getCardsFromFile(pathToFile):
        cardImages = []
        files = os.listdir(pathToFile)
        for file in files:
            cardImages.append(Image.open(f'{pathToFile}/{file}'))
        return cardImages

def getCardInfo(fullCardname):
    return fullCardname