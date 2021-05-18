from math import sqrt

class Cost():
    def __init__(tt_clones, tt_rounds, tt_elevators):
        self.tt_clones = tt_clones
        self.tt_rounds = tt_rounds
        self.tt_elevators = tt_elevators
    def add(cost):
        self.tt_clones += cost.tt_clones
        self.tt_rounds += cost.tt_rounds
        self.tt_elevators += cost.tt_elevators
    def is_valid():
        return self.tt_clones <= Game.nb_total_clones
            and self.tt_rounds <= Game.nb_additional_elevators
            and self.tt_rounds <= Game.nb_rounds

class Node():
    def __init__(self, x, y, direction, cost):
        self.x, self.y = [x, y]
        self.dist, self.cost, self.path = [None, cost, ""]
        self.direction = direction

class Game():
    nb_additional_elevators
    nb_total_clones
    nb_rounds
    direction
    width
    nb_floors
    elevators

def has_elevator(n):
    for e in Game.elevators:
        if e[0] == n.x and e[1] == n.y:
            return True
    return False

def equals(a, b): return a.x == b.x and a.y == b.y
def sort(li): return li if len(li) == 1 else sorted(li, key=lambda n: n.dist)
def distance(a, b): return sqrt((b.x - a.x)**2 + (b.y - a.y)**2) if a.dist is None else a.dist
def contains(li, n):
    for u in li:
        if equals(u, n): return u
    return None

def neighboors(u):
    ret = []
    if u.direction is "LEFT" and (u.y - 1) >= 0:
        cost = Cost(0,1,0).add(u.cost)
        if cost.is_valid():
            ret.append(Node(u.x, u.y - 1, "LEFT", cost))
    if u.direction is "RIGHT" and (u.y + 1) < width:
        cost = Cost(0,1,0).add(u.cost)
        if cost.is_valid():
            ret.append(Node(u.x, u.y + 1, , "RIGHT", cost))
    # Build elevator
    if has_elevator(u):
        cost = Cost(0,1,0).add(u.cost)
        if cost.is_valid():
            ret.append(Node(u.x + 1, u.y, cost))
    elif Game.nb_floor > u.x:
        cost = Cost(1, 3, 1).add(u.cost)
        if cost.is_valid():
            ret.append(Node(u.x + 1, u.y, cost))
    # Block
    cost = Cost(1,3,0).add(u.cost)
    if cost.is_valid():
        ret.append(Node(u.x, u.y + 1, , ("RIGHT", "LEFT")[u.direction is "RIGHT"), cost))
    return ret

def astar(begin, target):
    cl = []
    op = [begin]
    while len(op) > 0:
        op = sort(op)
        u = op.pop(0)
        if equals(u, target):
            return u
        for n in neighboors(u):
            n.dist = distance(n, target)
            cont_op = contains(op, n)
            cont_cl = contains(cl, n)
            if cont_cl != None:
                if better(cont_cl.cost, n.cost): continue
                cl.remove(cont_cl)
                cont_cl.cost = n.cost
                cont_cl.path = f"{(f'{u.path}, ','')[u.path == '']}{n.x} {n.y}"
                op.append(cont_cl)
            elif cont_op == None:
                n.cost = cost
                n.path = f"{(f'{u.path}, ','')[u.path == '']}{n.x} {n.y}"
                op.append(n)
        cl.append(u)
    return None

def run():
    Game.nb_floors, Game.width, Game.nb_rounds, exit_floor, exit_pos,
    Game.nb_total_clones, Game.nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
    elevators = [map(int, input().split()) for _ in range(nb_elevators)]
    clone_floor, clone_pos, Game.direction = input().split()
    path = astar(Node(*map(int, [clone_floor, clone_pos])), Node(exit_floor, exit_pos))


if __name__ == "__main__":
    print(astar(Node(1, 1), Node(5, 5)).path)
