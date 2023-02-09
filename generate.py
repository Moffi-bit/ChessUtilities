import argparse
import pandas as pd
import requests
import io
import random

class Generator():
    # Constructor 
    def __init__(self):
        self.parseArgs()
        self.dataValues = self.loadCSV()
        self.randomOpening = self.args.randopen
        self.specificOpening = self.args.open
        self.randomFEN = self.args.randfen
        self.specificFEN = self.args.fen

    def parseArgs(self):
        parser = argparse.ArgumentParser(description="Welcome to Chess Utilities!")
        parser.add_argument("-o", "--open", help="enter a specific chess opening you want to gather information about", type=str, nargs="+")
        parser.add_argument("-ro", "--randopen", help="use this argument if you want information about a random opening", action="store_true")
        parser.add_argument("-rf", "--randfen", help="use this argument if you want a random fen", action="store_true")
        parser.add_argument("-f", "--fen", help="use this argument if you want the fen of your specific opening", action="store_true")
        args = parser.parse_args()
        self.args = args

    def evaluateArguments(self):
        if self.specificOpening != None:
            temp = ""
            for element in self.specificOpening:
                temp += element + " "
            self.specificOpening = temp

        if isinstance(self.specificOpening, str):
            self.getSpecificOpening()

            if self.specificFEN:
                self.getSpecificFEN()

        if self.randomOpening:
            self.getRandomOpening()
        
        if self.randomFEN:
            self.getRandomFEN()
    
    # Load the chess opening data from a url 
    def loadCSV(self):
        url = "https://raw.githubusercontent.com/tomgp/chess-canvas/master/pgn/chess_openings.csv"
        download = requests.get(url).content
        dataFrame = pd.read_csv(io.StringIO(download.decode('utf-8')))

        return dataFrame.values
    
    # Select a random chess opening and return relevant information
    def getRandomOpening(self):
        return self.dataValues[random.randint(0, len(self.dataValues))]

    # Takes in an opening and returns the moves for that opening if it's able to find it in the databasr/csv
    def getSpecificOpening(self):
        openingsFound = []

        for opening in self.dataValues:
            if opening[1].lower().__contains__(self.specificOpening.lower()):
                openingsFound.append(opening)

        if len(openingsFound) > 1:
            print("Multiple openings were found with that name:\n")
            i = 0
            for opening in openingsFound:
                print(f"#{i + 1} is the {opening[1]} opening.\n")
                i += 1
            chosenOpening = openingsFound[int(input("Please select the one you'd like.\n")) - 1]

            print(f"The moves for the {chosenOpening[1]} are {chosenOpening[2]}\n")
        elif len(openingsFound) == 1:
            print(f"The moves for the {openingsFound[0][1]} are {openingsFound[0][2]}\n")
        else:   
            print(f"No opening named {self.specificOpening}was found.\n")

    def getRandomFEN(self):
        print("TODO : rand fen")

    def getSpecificFEN(self):
        print("TODO : specific fen")

def main():
    gen = Generator()
    gen.evaluateArguments()

if __name__ == '__main__':
    main()