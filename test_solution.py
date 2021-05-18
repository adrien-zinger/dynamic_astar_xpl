import pytest
import solution

#nb_floor, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators
inputs = [
    "10", #number or floors
    "19", #width
    "47", #number of rounds
    "9",  #exit floor
    "9",  #exit position
    "41", #number of clones
    "0",  #number of additional elevators
    "17" #number of elevators
]
elevators = ["3 4","4 3","7 4","1 17","8 9","4 9","2 3","0 3","5 4","7 17","1 4","3 17","2 9","6 9","5 17","0 9","6 3"]


def test_neighboors():
    pass


#def test_solution():
#    iit = iter(inputs + elevators)
#    solution.input = lambda: next(iit)
#    class st:
#        _o = ''
#    def p(o):
#        print(o)
#        st._o = o
#    solution.run()

if __name__ == "__main__":
    test_solution()