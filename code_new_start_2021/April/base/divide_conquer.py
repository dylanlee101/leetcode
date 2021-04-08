def print_result():
    pass


def prepare_data(problem):
    pass

def recursion(level,param1,param2):
    if level > MAX_LEVEL:
        process_result
        return

    process(level,data)
    self.recursion(level+1,param1,param2)


def divide_conquer(problem,param1,param2):

    # recursion terminator
    if problem is None:
        print_result()
        return

    data = prepare_data(problem)
    subproblems = split_problem(problem,data)

    subresult1 = self.divide_conquer(subproblems[0],p1)
    subresult2 = self.divide_conquer(subproblems[1], p1)


    result = peocess_result(subresult1,subresult2)
