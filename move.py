from field import Field
from gameboard import Gameboard


class Move:
    def __init__(self, field: Field, isMine: bool) -> None:
        self.field = field
        self.isMine = isMine

    def perform(self, gameboard: Gameboard):
        if self.isMine:
            # print("clicking if")
            self.field.toggleCover()
            gameboard.updateLeftMines()
        else:
            # print("clicking else")
            gameboard.onFieldClicked(self.field)
        
        # x, y = self.field.getCoordinates().getX(), self.field.getCoordinates().getY()
        # val = self.field.getValue()
        # if val == "M" and self.field.isCovered():
            # val = "C"
        # print("[" + str(x) + ", " + str(y) + "] - " + str(val))
    
    def __repr__(self) -> str:
        return f'Move({self.field}, isMine={self.isMine})'

    def __hash__(self) -> int:
        return hash(self.field)