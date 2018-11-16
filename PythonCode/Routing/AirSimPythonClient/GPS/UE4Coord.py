

class UE4Coord:
    '''A coordinate which represents an objects location in an unreal engine environment'''
    def __init__(self, x, y, z = 0):
        self.x, self.y, self.z = x, y, z
        if not isinstance(self.x, float):
            try:
                self.x = float(self.x)
            except Exception as e:
                raise(e)
        
        if not isinstance(self.y, float):
            try:
                self.y = float(self.y)
            except Exception as e:
                raise(e)
                
        if not isinstance(self.z, float):
            try:
                self.z = float(self.z)
            except Exception as e:
                raise(e)
        
    def __add__(self, other):
        return UE4Coord(self.x + other.x, self.y + other.y, self.z + other.z)
        
    def __sub__(self, other):
        return UE4Coord(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def mul(self, int):
        pass
    
    def get_dist_to_other(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)**0.5
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    
    def __str__(self):
        return '{x}, {y}, {z}'.format(x = self.x, y = self.y, z = self.z)
    
    def __repr__(self):
        return '{x}, {y}, {z}'.format(x = self.x, y = self.y, z = self.z)