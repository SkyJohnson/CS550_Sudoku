'''
Constraint propagation
'''
from queue import Queue
def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation
    
    """
    
    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    csp.neighbors[x] is the neighbors of variable x

    # General algorithm:
    #
    # queue(constraints)
    queue = Queue()
    for x1 in csp.variables:
        for x2 in csp.neighbors[x1]:
            queue.put((x1, x2))
    # while queue not empty:
    while not queue.empty():
    #   (x1, x2) = dequeue
        (x1, x2) = queue.get()
    #   if revise(csp, x1, x2):
        if revise(csp, x1, x2):
    #       if domain(x1) empty *not solvable* -> return false
            if len(csp.domains[x1]) == 0:
                return False
    #       else:
            else:
    #           for x in {neighbors(x1)-x2}:
                for x in (csp.neighbors[x1] - set(x2)):
    #               enqueue((x, x1))
                    queue.put((x, x1))
    # return true
    return True

def revise(csp, x1, x2):
    revised = False

    # general algorithm:
    #
    # for x in domain(x1):
    for x in csp.domains[x1]:
    #   if no y in domain(x2) satsfies constraint(x,y):
        for y in csp.domains[x2]:
    # #       domain(x1).remove(x)
            if y in csp.choices(x1) and not csp.constraints(x1, x, x2, y):
                csp.prune(x1, x, None)
    # #       revised = true
                revised = True
                break

    return revised


