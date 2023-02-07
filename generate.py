import pandas as pd
import requests
import io
import random

class Generator():
    # Constructor 
    def __init__(self, urlToCSV):
        self.dataValues = self.loadCSV(urlToCSV)
    
    # Load the chess opening data from a url 
    def loadCSV(self, url):
        download = requests.get(url).content

        dataFrame = pd.read_csv(io.StringIO(download.decode('utf-8')))
        return dataFrame.values
    
    # Select a random chess opening and return relevant information
    def getRandomOpening(self):
        return self.dataValues[random.randint(0, len(self.dataValues))]

    # Takes in an opening and returns the moves for that opening if it's able to find it in the databasr/csv
    def getSpecificOpening(self, specificOpening):
        openingsFound = []

        if isinstance(specificOpening, str):
            for opening in self.dataValues:
                if opening[1].lower().__contains__(specificOpening.lower()):
                    openingsFound.append(opening)

            if len(openingsFound) > 1:
                print("Multiple openings were found with that name:\n")
                i = 0
                for opening in openingsFound:
                    print(f"#{i + 1} is the {opening[1]} opening.\n")
                    i += 1
                chosenOpening = openingsFound[int(input("Please select the one you'd like.")) - 1]

                return f"The moves for the {chosenOpening[1]} are {chosenOpening[2]}"
            elif len(openingsFound) == 1:
                return f"The moves for the {openingsFound[0][1]} are {openingsFound[0][2]}"
            return f"No opening named {specificOpening} was found."
        else: 
            return f"Invalid parameter passed. Expecting type str but received {type(specificOpening)}"

    def getRandomFEN(self):
        print("TODO")

    def getSpecificFEN(self):
        print("TODO")

# Demo driver 
def testCode():
    gen = Generator("https://raw.githubusercontent.com/tomgp/chess-canvas/master/pgn/chess_openings.csv")

    randomOpening = gen.getRandomOpening()
    print(f"The random opening selected is the {randomOpening[1]}.\nThe opening's ECO is {randomOpening[0]}.\nThe opening's moves is {randomOpening[2]}")
    specificOpening = "Krazy"
    specificOpeningMoves = gen.getSpecificOpening(specificOpening)
    print(f"{specificOpeningMoves}")

# (I plan on implementing args functionality soon)
def main():
    testCode()

if __name__ == '__main__':
    main()