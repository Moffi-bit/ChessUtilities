import pandas as pd
import requests
import io
import random

class Generator():
    def __init__(self, urlToCSV):
        self.dataValues = self.loadCSV(urlToCSV)
    
    def loadCSV(self, url):
        download = requests.get(url).content

        dataFrame = pd.read_csv(io.StringIO(download.decode('utf-8')))
        return dataFrame.values
    
    def getRandomOpening(self):
        return self.dataValues[random.randint(0, len(self.dataValues))]

    def getSpecificOpening(self, specificOpening):
        if isinstance(specificOpening, str):
            for opening in self.dataValues:
                if opening[1].lower().__contains__(specificOpening.lower()):
                    return f"The moves for the {opening[1]} are {opening[2]}"
            return f"No opening named {specificOpening} was found."
        else: 
            return f"Invalid parameter passed. Expecting type str but received {type(specificOpening)}"

    def getRandomFEN(self):
        print("TODO")

    def getSpecificFEN(self):
        print("TODO")

def testCode():
    gen = Generator("https://raw.githubusercontent.com/tomgp/chess-canvas/master/pgn/chess_openings.csv")
    randomOpening = gen.getRandomOpening()
    print(f"The random opening selected is the {randomOpening[1]}.\nThe opening's ECO is {randomOpening[0]}.\nThe opening's moves is {randomOpening[2]}")
    specificOpening = "Alekhine"
    specificOpeningMoves = gen.getSpecificOpening(specificOpening)
    print(f"{specificOpeningMoves}")
    
def main():
    testCode()

if __name__ == '__main__':
    main()