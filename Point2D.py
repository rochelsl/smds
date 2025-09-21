class Point2D:

    def __init__(self, x_Pos=0, y_Pos=0): # constructor with default values
        self.x_Pos = x_Pos
        self.y_Pos = y_Pos

    def getX(self): # get the x position
        return self.x_Pos
    
    def getY(self): # get the y position
        return self.y_Pos
    
    def setX(self, x_Pos): # set the x position
        self.x_Pos = x_Pos

    def setY(self, y_Pos): # set the y position
        self.y_Pos = y_Pos

    def __str__(self): # string representation
        return f'Point2D({self.x_Pos}, {self.y_Pos})'
    
    def __repr__(self): # official string representation
        return f'Point2D(xPos={self.x_Pos}, yPos={self.y_Pos})'