import os
import Utils

def prepareDigimon() -> int:
  cardCount = 0
  with open(Utils.getPath('input', 'digimonInput.txt'), 'w') as outfile:
    for fname in os.listdir(Utils.getPath('digimonInput')):
      with open(Utils.getPath('digimonInput', fname)) as infile:
        next(infile)
        next(infile)
        for line in infile:
          textInLine = line.split()
          quantity = int(textInLine[-1])
          id = textInLine[0]
          for i in range(quantity):
            outfile.writelines(id+"\n")
            cardCount += 1
  return cardCount