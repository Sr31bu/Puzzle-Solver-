#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Shashank Ramachandran
# email:sr31@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Michael Krah
# partner's email: mickra@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        count = 0
        for i in range(3):
            for c in range(3):
                self.tiles[i][c] = str(digitstr[count])
                count = count + 1
                if self.tiles[i][c] == '0':
                    self.blank_r = i
                    self.blank_c = c
    
    def __repr__(self):
        """represents the string version of rep"""
        word = ""
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    word = word + '_ '
                else:
                    word = word + self.tiles[r][c] + ' '
            word = word + '\n'
        return word 
    
    def move_blank(self,direction):
        """moves in a specefied direction"""
        if direction == 'up':
            if self.blank_r == 0:
                return False
            else:
                pos = self.tiles[self.blank_r-1][self.blank_c]
                self.tiles[self.blank_r-1][self.blank_c] = '0'
                self.tiles[self.blank_r][self.blank_c] = pos
                self.blank_r -= 1
                return True  
            
        elif direction == 'down':
            if self.blank_r == 2:
                return False
            else:
                pos = self.tiles[self.blank_r+1][self.blank_c]
                self.tiles[self.blank_r+1][self.blank_c] = '0'
                self.tiles[self.blank_r][self.blank_c] = pos
                self.blank_r += 1
                return True
            
        elif direction == 'left':
            if self.blank_c == 0:
                return False
            else:
                pos = self.tiles[self.blank_r][self.blank_c-1]
                self.tiles[self.blank_r][self.blank_c-1] = '0'
                self.tiles[self.blank_r][self.blank_c] = pos
                self.blank_c -= 1
                return True 
            
            
        elif direction == 'right':
            if self.blank_c == 2:
                return False
            else:
                pos = self.tiles[self.blank_r][self.blank_c+1]
                self.tiles[self.blank_r][self.blank_c+1] = '0'
                self.tiles[self.blank_r][self.blank_c] = pos
                self.blank_c += 1
                return True
        else:
            return False
    
    def digit_string(self):
        """ digital string version of the board"""
        word = ''
        for i in range(3):
            for j in range(3):
                word = word + self.tiles[i][j]
        return word 
    
    def copy(self):
        """creates a deep copy"""
        b2 = Board(self.digit_string())
        return b2
    
    def num_misplaced(self):
        """number of misplaced pieces"""
        count = 0
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] != '0':
                    if self.tiles[i][j] != GOAL_TILES[i][j]:
                        count = count + 1
        return count 
    
    def __eq__(self,other):
        """ if they are equal to each other """
        return  self.tiles == other.tiles
    
    def aStar(self):
       """ Finds how far each tile is from goal state"""
       count = 0
       r_current = -1
       c_current = -1
       r_goal = -1
       c_goal = -1
       for i in range(1, 9):
           for r in range(3):
               for c in range(3):
                   if self.tiles[r][c] == str(i):
                       r_current = r
                       c_current = c
           for r in range(3):
               for c in range(3):
                   if GOAL_TILES[r][c] == str(i):
                       r_goal = r
                       c_goal = c
           
           count += (abs(r_goal-r_current) + abs(c_goal - c_current))
       
       return count

def process(s,c):
    count = 0
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            count = count + 1
            index = i
    return [index,count ]

def create_2d(height,width):
    list1 = [[0]*width] * height
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            list1[i][j] = i *j
    return list1
       
    
def remove_vowels(s):
    if s == '':
        return ''
    else:
        vrest = remove_vowels(s[1:])
        if s[0] in 'aeiou':
            return vrest
        else:
            return s[0] + vrest
                
            
        
        
        
    
        
        
    
        
    
    rest
            
            
        
        
                
                
        
        
           
        
        
    
                
                
            
        
            


    ### Add your other method definitions below. ###
