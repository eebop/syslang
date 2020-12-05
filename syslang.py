#!/usr/bin/env python
import sys
import options
import expressions
ops = options.run(sys.argv[1:])
def run_file(name):
    with open(name, 'r') as f:
        data = f.read()
    ex = expressions.superexpression(data)
    ex()

run_file(__file__[:__file__.rfind('/')] + '/launch.sl')
