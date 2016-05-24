#!/usr/bin/env python

from nodes import Node
from node.sort import Sort
import math

class End(Node):
    char = "e"
    args = 1
    results = 1
    contents = math.e
    
    @Node.test_func([12], [-13])
    def complement(self, inp: Node.number):
        """-(inp+1)"""
        return ~inp
    
    @Node.test_func(["Hello"], ["o"])
    @Node.test_func([[1,2,3]], [3])
    def end(self, inp: Node.indexable):
        """inp[-1]"""
        return [inp[-1]]
    
    @Node.test_func([{1:1, "2":2}], [[1,2]])
    def values(self, inp: dict):
        """sorted(inp.values)"""
        return [Sort.sort_list(inp.values())]