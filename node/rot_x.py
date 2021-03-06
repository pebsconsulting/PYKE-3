#!/usr/bin/env python

from nodes import Node
from node.numeric_literal import NumericLiteral 

class RotX(Node):
    char = "R"
    args = 0
    results = 0
    default_arg = 2
    reverse_first = True
    
    def __init__(self, amount: Node.NumericLiteral):
        self.args = self.results = amount
        
    def prepare(self, stack):
        if self.args == 1:
            self.args = self.results = len(stack)
            
    @Node.test_func([1,0], [1,0])
    @Node.test_func([1,2,3,4], [1,2,3,4], "4")
    def func(self, *args):
        """Rotate the top `amount` items on the stack by 1."""
        return list(args[:1]+args[1:])
    