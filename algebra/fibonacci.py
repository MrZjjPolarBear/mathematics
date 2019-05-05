# -*- coding: utf-8 -*-
"""
Created on Sun May  5 08:53:27 2019

@author: Zha_Jiajia
"""

"""
Obtain Fibonacci series by recursion.
"""
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

"""
Obtain Fibonacci series by tail recursion.
reference: http://code.activestate.com/recipes/474088/
"""
import sys

class TailRecurseException(BaseException):
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_call_optimized(g):
  """
  This function decorates a function with tail call
  optimization. It does this by throwing an exception
  if it is it's own grandparent, and catching such
  exceptions to fake the tail call optimization.
  
  This function fails if the decorated
  function recurses in a non-tail context.
  """
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException as e:
          args = e.args
          kwargs = e.kwargs
  func.__doc__ = g.__doc__
  return func

@tail_call_optimized
def tail_fib(i, current_v = 0, next_v = 1):
  if i == 0:
    return current_v
  else:
    return tail_fib(i - 1, next_v, current_v + next_v)

"""
Obtain Fibonacci series by dynamic programming.
"""
def fastfib(n, mem):
    if n not in mem:
        mem[n] = fastfib(n-1, mem) + fastfib(n-2, mem)
    return mem[n]

def fib1(n):
    mem = {0:0, 1:1}
    return(fastfib(n, mem))
    

print(fib(35))
print(fib1(35))
print(tail_fib(35))
