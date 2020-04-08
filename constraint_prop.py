'''
Constraint propagation
'''

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
    # while queue not empty:
    #   (x1, x2) = dequeue
    #   if revise(csp, x1, x2):
    #       if domain(x1) empty *not solvable* -> return false
    #       else:
    #           for x in {neighbors(x1)-x2}:
    #               enqueue((x, x1))
    # return true
    
    raise NotImplemented

def revise(csp, x1, x2):
    revised = False

    # general algorithm:
    #
    # for x in domain(x1):
    #   if no y in domain(x2) satsfies constraint(x,y):
    #       domain(x1).remove(x)
    #       revised = true

    return revised