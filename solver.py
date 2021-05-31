from random import randint
from typing import List
from time import sleep
from datetime import datetime, timedelta

from field import Field
from vector import Vector
from matrix import Matrix
from move import Move


class Solver():
    def __init__(self, game):
        super(Solver, self).__init__()
        self.__game = game
        self.__gameboard = self.__game.getGameboard()
        self.__gameConfiguration = self.__game.getGameConfiguration()
        self.__fieldsArray: List[Field] = []
        self.__idToFielddict = {}
        self.__fieldToIddict = {}
        ## todo: 
        ## get gameboard from game
        ## gameboard.onFieldClicked(field)
    
    def set(self):
        #set gameboard
        self.__gameboard.setGameboard(self.__gameConfiguration)

        #perform first random move to generate initial board configuration
        size = self.__gameConfiguration.getSize()
        start_x, start_y = randint(0, size - 1), randint(0, size - 1)
        self.__fieldsArray = self.__gameboard.getFieldsArray()
        startingField = self.__fieldsArray[start_x][start_y]
        self.__gameboard.onFieldClicked(startingField)

    def iterFieldsArray(self, fieldsArray):
        size = self.__gameConfiguration.getSize()
        for x in range(size):
            for y in range(size):
                yield fieldsArray[x][y]

    def getNeighbourIterator(self, field):
        neighbours_coords = self.__gameboard.findNeighbors(field)
        for neighbour in neighbours_coords:
            x, y = neighbour.getCoordinates()
            yield self.__fieldsArray[x][y]

    def getNumberedSquaresAdjacentToNonClickedFields(self):
        numbered_squares = []
        current_id = 0
        for field in self.iterFieldsArray(self.__fieldsArray):
            if field.isChecked() and isinstance(field.getValue(), int):
                for neighbour_field in self.getNeighbourIterator(field):
                    if neighbour_field.isChecked() is False and neighbour_field.isCovered() is False:
                        numbered_squares.append(field)
                        current_id = self.updateNonClickedFieldDicts(current_id, neighbour_field)
        return numbered_squares

    def updateNonClickedFieldDicts(self, current_id, field):
        if field not in self.__fieldToIddict:
            self.__idToFielddict[current_id] = field
            self.__fieldToIddict[field] = current_id
            current_id += 1
        return current_id

    def createMatrix(self, numbered_squares):
        matrix = Matrix(rows=[])
        number_of_nonclicked_fields = len(self.__fieldToIddict)
        for field in numbered_squares:
            row = Vector(size=number_of_nonclicked_fields + 1)
            row[number_of_nonclicked_fields] = field.getValue()
            for neighbour in self.getNeighbourIterator(field):
                if neighbour.isChecked() is False and neighbour.isCovered() is False:
                    id = self.__fieldToIddict[neighbour]
                    row[id] = 1
                elif neighbour.isCovered():
                    row[number_of_nonclicked_fields] -= 1
            matrix.addRow(row)
        return matrix
    
    def findFirstNonZeroRow(self, matrix):
        first_row = -1
        for row in matrix.rows[::-1]:
            if any([value != 0 for value in row.values]):
                first_row = matrix.rows.index(row)
                break
        return first_row

    def getResults(self, matrix, firstNonZeroRow):
        rows_size = len(matrix.rows[0].values) - 1
        results = Vector(size=rows_size)
        matrix_rows = matrix.rows[:firstNonZeroRow + 1]

        for index, row in reversed(list(enumerate(matrix_rows))):
            failedToFindValue = False
            pivot = index
            pivot_value = row[pivot]
            value = row[rows_size]

            for column in range(index + 1, rows_size):
                currentValue = row[column]

                if pivot_value == 0 and currentValue != 0:
                    pivot = column
                    pivot_value = currentValue
                
                if currentValue != 0:
                    if results.isPresent(column):
                        value -= currentValue * (1 if results[column] else 0)
                        row[column] = 0
                    else:
                        failedToFindValue = True

            row[rows_size] = value

            if pivot_value != 0:
                if failedToFindValue:
                    minValue = 0
                    maxValue = 0
                    for column in range(index, rows_size):
                        currentValue = row[column]
                        if currentValue > 0:
                            maxValue += currentValue
                        elif currentValue < 0:
                            minValue += currentValue
                    
                    if value == minValue:
                        for column in range(index, rows_size):
                            currentValue = row[column]
                            if currentValue > 0:
                                results[column] = False #not a mine
                            elif currentValue < 0:
                                results[column] = True #a mine
                    elif value == maxValue:
                        for column in range(index, rows_size):
                            currentValue = row[column]
                            if currentValue > 0:
                                results[column] = True #a mine
                            elif currentValue < 0:
                                results[column] = False #not a mine

                else:
                    if not results.isPresent(pivot) and (value == 0 or value == 1):
                        results[pivot] = (value == 1)

        return results

    def getMoves(self, results):
        moves = []
        for i in range(len(results.values)):
            if results.isPresent(i):
                if results[i] is True:
                    moves.append(Move(self.__idToFielddict[i], isMine=True))
                else:
                    moves.append(Move(self.__idToFielddict[i], isMine=False))
        return moves

    def run(self):
        endTime = datetime.now() + timedelta(seconds = self.__gameConfiguration.getSolverDuration())
        while datetime.now() < endTime:
            #get numbered squares and identify adjacent non clicked fields
            numbered_squares = self.getNumberedSquaresAdjacentToNonClickedFields()

            if not numbered_squares or not self.__idToFielddict:
                #There cannot be any solution.
                break

            #create matrix based on the numbered squares
            matrix = self.createMatrix(numbered_squares)
            
            #gaussian eliminate the matrix
            matrix.gaussianEliminate()

            #find first non zero row.
            nonZeroRow = self.findFirstNonZeroRow(matrix)

            #get results
            results = self.getResults(matrix, nonZeroRow)

            #create list of moves
            moves = self.getMoves(results)
            if not moves:
                break

            solverDuration = self.__gameConfiguration.getSolverDuration()
            while moves:
                move = moves.pop()
                #sleep(solverDuration)
                #print(move)
                move.perform(self.__gameboard)
 