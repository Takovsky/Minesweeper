class Matrix:
    def __init__(self, rows) -> None:
        self.rows = rows

    def addRow(self, row):
        self.rows.append(row)

    def __repr__(self) -> str:
        result = 'Matrix(\n'
        for row in self.rows:
            result += repr(row) + '\n'
        result += ')'
        return result

    def __getitem__(self, index):
        return self.rows[index]

    def __setitem__(self, index, value):
        self.rows[index] = value

    def gaussianEliminate(self):
        if self.rows:
            n_rows = len(self.rows)
            n_columns = len(self.rows[0].values)

            row , column = 0, 0
            while(row < n_rows and column < n_columns):
                max_row = row
                for currentRow in range(row+1, n_rows):
                    if abs(self.rows[currentRow][column]) > abs(self.rows[max_row][column]):
                        max_row = currentRow
                
                if self.rows[max_row][column] != 0:

                    self.rows[row], self.rows[max_row] = self.rows[max_row], self.rows[row]
                    self.rows[row].multiply( 1 / self.rows[row][column] )

                    for iterRow in range(row+1, n_rows):
                        multiply_value = -1 * self.rows[iterRow][column]
                        if multiply_value != 0:
                            self.rows[row].multiply(multiply_value)
                            self.rows[iterRow].add(self.rows[row])
                            self.rows[row].multiply(1 / multiply_value)

                    row += 1

                column += 1
