
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, forward_checking
from backtrack import backtracking_search


E  = Sudoku(easy1)  # construct a Sudoku problem
print("Initial state AC3:\n")
E.display(E.infer_assignment())

solved = AC3(E)
print("\nAfter AC3:\n")
E.display(E.infer_assignment())
     
H = Sudoku(harder1)  # construct a Sudoku problem
print("\nInitial state backtracking search:\n")
H.display(H.infer_assignment())

# From the textbook, we can use the MRV heuristic for variable selection and forward checking for inference.

# "If some variable X has no legal values left, the MRV
# heuristic will select X and failure will be detected immediately—avoiding pointless searches
# through other variables." (Page 216)

# AND 

# "One of the simplest forms of inference is called forward checking. Whenever a vari-
# able X is assigned, the forward-checking process establishes arc consistency for it: for each
# unassigned variable Y that is connected to X by a constraint, delete from Y ’s domain any
# value that is inconsistent with the value chosen for X. Because forward checking only does
# arc consistency inferences, there is no reason to do forward checking if we have already done
# arc consistency as a preprocessing step." (Page 217)

 
solved = backtracking_search(H, select_unassigned_variable=mrv, inference=forward_checking)
print("\nAfter backtracking search:\n")
H.display(H.infer_assignment())