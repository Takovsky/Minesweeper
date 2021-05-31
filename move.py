from field import Field
from gameboard import Gameboard


class Move:
    def __init__(self, field: Field, isMine: bool) -> None:
        self.field = field
        self.isMine = isMine

    def perform(self, gameboard: Gameboard):
        if self.isMine:
            self.field.toggleCover()
            gameboard.updateLeftMines()
        else:
            gameboard.onFieldClicked(self.field)
    
    def __repr__(self) -> str:
        return f'Move({self.field}, isMine={self.isMine})'

    def __hash__(self) -> int:
        return hash(self.field)