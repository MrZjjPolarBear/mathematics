# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:14:14 2019

@author: Zha_Jiajia
"""

def SquarerootBi(x, epsilon):
    '''Return the squareroot of a nonnegative number x 
    with the precision epsilon'''
    assert x >= 0, '%f is not a nonnegative number' %x
    assert epsilon > 0, '%f is not a positive number' %epsilon
    low = 0
    high = x
    guess = (low + high) / 2
    ctn = 1
    while abs(guess**2 - x) >= epsilon and ctn < 100:
        if guess**2 > x: 
            high = guess
            guess = (low + high) / 2
        else: 
            low = guess
            guess = (low + high) / 2
        ctn += 1
    print("SquarerootBI, Iteration time: %i, Answere: %f" %(ctn, guess))
    
def SquarerootNR(x, epsilon):
    '''Return the squareroot of a nonnegative number x 
    with the precision epsilon'''
    assert x >= 0, '%f is not a nonnegative number' %x
    assert epsilon > 0, "%f is not a positive number" %epsilon
    guess = epsilon
    ctn = 1
    while abs(guess**2 -x) >= epsilon and ctn < 100:
        guess = (x - guess**2) / (2 * guess) + guess
        ctn += 1
    print("SquarerootNR, Iteration time: %i, Answere: %f" %(ctn, guess))
    
if __name__ == "__main__":
    SquarerootBi(1e7, 0.001)
    input()
    SquarerootNR(1e7, 0.001)