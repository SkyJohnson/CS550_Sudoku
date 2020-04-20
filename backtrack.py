
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
    
    # See Figure 6.5] of your book for details

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """
        removals = [] # Removals needed for the inference arguments.

        # if assingment is complete then return assignment (missing this part)




        var = select_unassigned_variable(assignment, csp)  # var <- SELECT-UNASSIGNED-VARIABLE(csp)
        for value in order_domain_values(var, assignment, csp): # for each value in ORDER-DOMAIN-VALUES(csp)
            # if value is consistent with assignment then add {var = value} to assignment
            # In other words, no conflicts with other values
            if csp.nconflicts(var, value, assignment) == 0:
                # add {var = value} to assignment
                csp.assign(var, value, assignment)
                # inferences <- INFERENCE(csp, var, value)
                inferences = inference(csp, var, value, removals)
                # if inferences != failure then
                if inferences is not None:
                    # add inferences to assignment
                    # Combine the current var and value pair to not choose it again to removals
                    # if it is a successful pick.
                    removals.extend(csp.suppose(var, value))
                #   result <- BACKTRACK(assignment, csp)
                    backtrack_result = backtrack(assignment) # Only takes in an assignment as an argument, no csp is passed in
                    # if result != failure then
                    if backtrack_result is not None:
                        # return result
                        return backtrack_result
            # remove {var = value} and inferences from assignment
            # Essentially restore the variable's value and un-assign the assignment, if there is a conflict.
            csp.restore(removals)
            csp.unassign(var, assignment)
            # Since we are done with it at this point and no result has been returned, where it's not a successful choice.

        return None # None means failure
    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result

