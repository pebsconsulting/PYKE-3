import lang_ast
from nodes import Node
from type.type_infinite_list import DummyList
from itertools import tee
import copy

class DeepMap(Node):
    char = "M"
    args = 0
    results = None
    contents = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def __init__(self, node:Node.NodeSingle):
        self.node = node
        self.args = node.args
    
    @Node.test_func([[[0,1,2,3],[4,5,6,7]]], [[[0, 2, 4, 6], [8, 10, 12, 14]]], "}")
    def func(self, *args):
        """Deeply map an operation across a nD tree.
Takes a list or tuple with a varying depth.
Returns a list with the same depth all round with the function applied."""
        seq, *args = copy.deepcopy(args)
        assert(isinstance(seq,Node.sequence))
        return [self.recurse(seq, args)]
        

    def recurse(self, seq, args):
        rtn = []
        for i in seq:
            if isinstance(i, Node.sequence):
                rtn.append(self.recurse(i, args))
            else:
                rtn.append(self.run(i, args))
        return rtn
    
    def run(self, obj, args):
        rtn = self.node([obj]+args)
        if len(rtn) == 1: rtn = rtn[0]
        return rtn

    def apply_inf_list(self, a:Node.infinite, b:Node.infinite):
        def apply_iterator(a, b):
            a, a_copy = tee(a, 2)
            b, b_copy = tee(b, 2)
            yield self.run(next(a_copy), [next(b_copy)])
            size = 1
            while 1:
                next_a = next(a_copy)
                next_b = next(b_copy)
                a, new_a = tee(a, 2)
                b, new_b = tee(b, 2)
                yield from (self.run(next(new_a), [next_b]) for i in range(size))
                yield from (self.run(next_a, [next(new_b)]) for i in range(size))
                yield self.run(next_a, [next_b])
                size += 1
        return DummyList(apply_iterator(a, b))
