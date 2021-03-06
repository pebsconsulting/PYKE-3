#!/usr/bin/env python

import datetime
import math

from node.sort import Sort
from nodes import Node


class End(Node):
    char = "e"
    args = 1
    results = 1
    contents = math.e
    
    @Node.test_func([12], [6])
    @Node.test_func([11], [5])
    def floor_half(self, inp: Node.number):
        """inp//2"""
        return inp//2
    
    @Node.test_func(["Hello"], ["o"])
    @Node.test_func([[1,2,3]], [3])
    def end(self, inp: Node.indexable):
        """inp[-1]"""
        return [inp[-1]]
    
    @Node.test_func([{1:1, "2":2}], [[1,2]])
    def values(self, inp: dict):
        """sorted(inp.values)"""
        return [[i[1]for i in Sort.sort_list(inp.items())]]


    def is_weekend(self, time: Node.clock):
        new_time = datetime.datetime(*time.time_obj[:7])
        return new_time.weekday() >= 5
