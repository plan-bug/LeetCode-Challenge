class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):

        self.rec = {}
	
        for i, row in enumerate(rectangle):

            self.rec[i] = row
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
	
        for i in range(row1, row2+1):
		
            self.rec[i] = self.rec[i][:col1] + [newValue]*(col2-col1+1) + self.rec[i][col2+1:]

    def getValue(self, row: int, col: int) -> int:
		
        return self.rec[row][col]