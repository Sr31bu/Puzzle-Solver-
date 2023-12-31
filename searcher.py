#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def  __init__(self, depth_limit):
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_state(self,new_state):
        """adds a state to the list of states"""
        self.states += [new_state]
    
    def should_add(self,state):
        """ sees if it should add to the state"""
        if self.depth_limit < state.num_moves and self.depth_limit != -1:
            return False
        elif state.creates_cycle():
            return False
        else:
            return True 
    
    def add_states(self,new_states):
        """that takes a list State objects called new_states, and that processes
        the elements of new_states one at a time"""
        for i in new_states:
            if self.should_add(i):
                self.add_state(i)
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self,init_state):
        """ returns the goal state or none after testing the states"""
        self.add_state(init_state)
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
            
        return None 
    
    
    
    
                
    
  
    
    

                
        
        
        


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """ Breadth first searcher"""
    def next_state(self):
        """replaces the next_state method that is inherited from Searcher"""
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """ Depth first searcher"""
    def next_state(self):
        """replaces the next_state method that is inherited from Searcher"""
        s = self.states[-1]
        self.states.remove(s)
        return s

    




def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def  h1(state):
    """ returns the number of misplaced pieces in the board"""
    return state.board.num_misplaced()

def h2(state):
    """ finds the distance between a tile and its goal state and adds all the values"""
    return state.board.aStar()



### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        super().__init__(-1)
        self. heuristic = heuristic
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """  that overrides (i.e., replaces) the add_state method that is inherited from Searcher"""
        self.states += [[self.priority(state),state]]
    
    def  next_state(self):
        """that overrides (i.e., replaces) the next_state method that is inherited from Searcher"""
        s = max(self.states)
        self.states.remove(s)
        return s[-1]

class AStarSearcher(GreedySearcher):
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
        
      
     
    

        
    
   
        
  
    
   


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###

