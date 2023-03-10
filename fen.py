import random

class Fen():
    # Starting FEN: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    # White pieces are capitalized, black pieces are left lowercase, empty cells are denoted by a number 

    def __init__(self):
        self.fen = []
        self.pieces = [("r", 2), ("n", 2), ("b", 2), ("q", 1), ("k", 1) ,("R", 2), ("N", 2), ("B", 2), ("Q", 1), ("K", 1)]

    def createFenRow(self):
        sum = 0
        row = ""
        piece = True

        while sum < 8:
            if piece and self.piecesLeft():
                sum += 1
                row += self.randomPieceForRow()
                piece = False
            else:
                value = self.randomEmptyCellsForRow(sum)

                while sum + value > 8:
                    value = self.randomEmptyCellsForRow(sum)

                row += str(value)
                sum += value
                piece = True

        row = self.processRow(row)
        return row
    
    def processRow(self, row):
        processedRow = ""
        sum = 0

        for i in row:
            if str(i).isdigit():
                sum += int(i)
            else:
                processedRow += str(sum) + i if sum > 0 else i
                sum = 0
            
        if sum > 0:
            processedRow += str(sum)
            
        return processedRow
            
    def getNewFen(self):
        self.createFen()
        fenString = ""

        for i in range(0, len(self.fen)):
            if i != len(self.fen) - 1:
                fenString += self.fen[i] + "/"
            else:
                fenString += self.fen[i]

        self.refresh()

        return fenString

    def refresh(self):
        self.fen = []
        self.pieces = [("r", 2), ("n", 2), ("b", 2), ("q", 1), ("k", 1) ,("R", 2), ("N", 2), ("B", 2), ("Q", 1), ("K", 1)]

    def createFen(self):
        while len(self.fen) != 8:
            self.fen.append(self.createFenRow())

    def piecesLeft(self):
        piecesLeft = False

        for i in self.pieces:
            if i[1] == 0:
                pass
            else:
                piecesLeft = True
        
        return piecesLeft

    def randomPieceForRow(self):
        randNum = random.randint(0, len(self.pieces) - 1)

        while self.pieces[randNum][1] == 0:
            randNum = random.randint(0, len(self.pieces) - 1)

        x = list(self.pieces[randNum])
        x[1] -= 1
        self.pieces[randNum] = tuple(x)

        return self.pieces[randNum][0]

    def randomEmptyCellsForRow(self, sum):
        return 0 if sum == 8 else random.randint(1, 8 - sum)