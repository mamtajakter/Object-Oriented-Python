class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def move(self, dx: int, dy: int ):
        self.x +=dx
        self.y +=dy

    def __eq__(self, other:"Point")->bool:
        if self.x==other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self)->str:
        return f"({self.x}, {self.y})"