
from csp_lib.backtrack_util import (first_unassigned_variable,
                                    unordered_domain_values,
                                    no_inference)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """
    # Call with empty assignments, variables accessed through dynamic scoping (variables in outer scope can be accessed in Python)
    # See Figure 6.5] of your book for details
    
    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """
        

        # if assingment is complete then return assignment (missing this part)

        # When every variable has been assigned a value, the assignment is complete and we can return it as a solution.
        if len(assignment) == len(csp.variables): 
            return assignment

        var = select_unassigned_variable(assignment, csp)  # var <- SELECT-UNASSIGNED-VARIABLE(csp)
        for value in order_domain_values(var, assignment, csp): # for each value in ORDER-DOMAIN-VALUES(csp)
            # if value is consistent with assignment then add {var = value} to assignment
            # In other words, no conflicts with other values
            if csp.nconflicts(var, value, assignment) == 0:
                # add {var = value} to assignment
                removals = [] # Removals needed for the inference arguments. Each candidate value will have its own removals list, so we need to reset it for each value.
                csp.assign(var, value, assignment)
                removals.extend(csp.suppose(var, value))
                # Removals are used to keep track of the values that have been removed from the domain of the variable.
                # This is important for backtracking, as it allows us to restore the original state of the CSP when we backtrack.
                
                
                
                # inferences <- INFERENCE(csp, var, value)
                inferences = inference(csp, var, value, assignment, removals)
                # if inferences != failure then
                
                # Forward_checking returns False when a branch has no solution. 
                # "False is not None:" is still true, so the previously implemented inferences check would recurse into that failed branch. 
                
                if inferences:
                    # add inferences to assignment
                    # Combine the current var and value pair to not choose it again to removals
                    # if it is a successful pick.
                #   result <- BACKTRACK(assignment, csp)
                    backtrack_result = backtrack(assignment) # Only takes in an assignment as an argument, no csp is passed in
                    # if result != failure then
                    if backtrack_result is not None:
                        # return result
                        return backtrack_result
                # remove {var = value} and inferences from assignment
                # Essentially restore the variable's value and un-assign the assignment, if there is a conflict.
                csp.restore(removals) # It has to be in the if statement because if there is a conflict, we need to restore the variable's value and un-assign the assignment.
                csp.unassign(var, assignment)
                # Since we are done with it at this point and no result has been returned, where it's not a successful choice.

        return None # None means failure
    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result

