import lang_ast
from nodes import Node
import copy

class DeepForApply(Node):
    char = "a"
    args = 1
    results = 1
    
    def __init__(self, ast: Node.EvalLiteral):
        self.ast = ast
    
    @Node.test_func([[[(0, 0), (0, 1)], [(1, 0), (1, 1)]]], [[[1, 2], [2, 3]]], "+h")
    def func(self, seq: Node.sequence):
        """Deeply apply a node to a nD tree"""
        return [self.recurse(seq)]

    def recurse(self, seq):
        if isinstance(seq[0][0], Node.sequence):
            return [self.recurse(i) for i in seq]
        else:
            rtn = []
            for i in copy.deepcopy(seq):
                try:
                    val = self.ast.run(list(i))
                except AssertionError:
                    val = self.ast.run([list(i)])
                if len(val) > 1: rtn.append(val)
                else: rtn.extend(val)
            return rtn