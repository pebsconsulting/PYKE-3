from nodes import Node
import copy
from node.sort import Sort

class SortEval(Node):
    char = ".#"
    args = None
    results = None
    default_arg = 1
    
    def __init__(self, args: Node.NumericLiteral, ast:Node.EvalLiteral):
        self.args = args
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node("_")
        
    @Node.test_func([[1,5,2]], [[5,2,1]], "")
    def func(self, *args):
        """Sort input values by final outcome of loop"""
        args = list(args)
        args = copy.deepcopy(args)
        is_int = isinstance(args[0], int)
        if is_int:
            args[0] = list(range(args[0]))
        max_len = len(args[0])
        for i, arg in enumerate(args):
            if i == 0: continue
            args[i] = [arg]*max_len
        results = []
        for i in zip(*args):
            rtn = self.ast.run(list(i))
            results.append(rtn)
        sorted_results = Sort.sort_list(results)
        return [list(list(zip(*sorted(enumerate(args[0]), key = lambda x:sorted_results.index(results[x[0]]))))[1])]
    