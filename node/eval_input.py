#!/usr/bin/env python

import copy
import sys

import __main__

import eval as safe_eval
import settings
from nodes import Node


class EvalInput(Node):
    char = "Q"
    args = 0
    results = 1
    if "web" not in __main__.__file__:
        line = input()
        new = safe_eval.evals[settings.SAFE](line)
        sys.stdin.prepend(line+"\n")
        contents = new
            
    def func(self):
        """Prompt for content at start. Returns by default."""
        return [copy.deepcopy(EvalInput.contents)]
