#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Michael Krah
# email: mickra@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Shashank Ramachandran
# partner's email: sr31@bu.edu
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
def process_file(filename, algorithm, param):
    """Lists out all puzzles in a text file with the average moves and states tested"""
    
    file = open(filename, 'r')

    
    puzzle_solved = 0
    puzzle_moves = 0
    puzzle_states = 0
    for line in file:
        lines = line.strip('\n')
        
        init_board = Board(lines)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param) 
        
        soln = None
        try:
            soln = searcher.find_solution(init_state)
            if soln == None:
                print(lines + ": no solution")
            else:
                print(lines + ":", soln.num_moves, "moves,", searcher.num_tested, "states tested")
                puzzle_solved += 1
                puzzle_moves += soln.num_moves
                puzzle_states += searcher.num_tested
            
        except KeyboardInterrupt:
            print(lines +  ': search terminated, no solution')
        
        
            
    print()
    if puzzle_solved == 0:
       print("solved", puzzle_solved, "puzzles")
    else:
       print("solved", puzzle_solved, "puzzles")
       print("averages:", puzzle_moves/puzzle_solved, "moves,", puzzle_states/puzzle_solved, "states tested")
        
    file.close()
    
