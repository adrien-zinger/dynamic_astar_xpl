from math import sqrt

class Node():
    def __init__(self, x, y):
        self.x, self.y = [x, y]
        self.dist, self.cost, self.path = [None, 0, ""]

def equals(a, b): return a.x == b.x and a.y == b.y
def sort(li): return li if len(li) == 1 else sorted(li, key=lambda n: n.dist)
def distance(a, b): return sqrt((b.x - a.x)**2 + (b.y - a.y)**2) if a.dist is None else a.dist
def contains(li, n):
    for u in li:
        if equals(u, n): return u
    return None

def neighboors(u):
    return [Node(u.x, u.y + 1), Node(u.x + 1, u.y)]

def astar(begin, target):
    cl = []
    op = [begin]
    while len(op) > 0:
        op = sort(op)
        u = op.pop(0)
        if equals(u, target):
            return u
        for n in neighboors(u):
            cost = u.cost + 1
            n.dist = distance(n, target)
            cont_op = contains(op, n)
            cont_cl = contains(cl, n)
            if cont_cl != None:
                if cont_cl.cost <= cost: continue
                cl.remove(cont_cl)
                cont_cl.path = f"{(f'{u.path}, ','')[u.path == '']}{n.x} {n.y}"
                op.append(cont_cl)
            elif cont_op == None:
                n.cost = cost
                n.path = f"{(f'{u.path}, ','')[u.path == '']}{n.x} {n.y}"
                op.append(n)
        cl.append(u)
    return None

if __name__ == "__main__":
    print(astar(Node(1, 1), Node(5, 5)).path)
