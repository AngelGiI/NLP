"""
ENLP A0: The Basics

Usage: on the Unix command line,
  python basics.py
to run doctests. If all tests pass, the program will exit silently.

@author: Nathan Schneider

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""


import re, doctest
import collections as clt


def validate1(s):
    """
    Checks whether the string is a valid employee ID using a single regular expression.
    An employee ID is valid if and only if it consists
    only of 6-10 alphabetic characters (letters), followed by 2 numeric digits.

    (Assumes s is a string without any non-ASCII characters.
    Otherwise, does not make any assumptions about the string.)

    The lines below give example inputs and correct outputs using doctest notation,
    and can be run to test the code. Passing these tests is NOT sufficient
    to guarantee your implementation is correct. You may add additional test cases.

    >>> validate1('AbCdEf00')
    True
    >>> validate1('$0RQLpCHz49')
    False
    """
    EMPLOYEE_RE = r'^[a-zA-Z]{6,10}\d{2}$'
    if re.search(EMPLOYEE_RE, s):
        return True
    return False

def validate2(s):
    """
    >>> validate2('AbCdEf00')
    True
    >>> validate2('$0RQLpCHz49')
    False
    """
    if len(s) < 8 or len(s) > 12:    # S must be between length 8 and 12
        return False
    
    for i in range(len(s)):
        
        if i < len(s) - 2:           # Up until last 2 characters, they must be
            if not s[i].isalpha():   # alphabetic
                return False
            
        else:                        # The last 2 must be numeric
            if not s[i].isdigit():   
                return False
    return True

def dna_prob(seq):
    """
    Given a sequence of the DNA bases {A, C, G, T},
    stored as a string, returns a conditional probability table
    in a data structure such that one base (b1) can be looked up,
    and then a second (b2), to get the probability p(b2 | b1)
    of the second base occurring immediately after the first.
    (Assumes the length of seq is >= 3, and that the probability of
    any b1 and b2 which have never been seen together is 0.
    Ignores the probability that b1 will be followed by the
    end of the string.)

    >>> tbl = dna_prob('ATCGATTGAGCTCTAGCG')
    >>> tbl['T']['T']
    0.2
    >>> tbl['G']['A']
    0.5
    >>> tbl['C']['G']
    0.5
    """
    # Initialize a dictionary to store the counts of each base pair.
    Counts = clt.defaultdict(lambda: clt.Counter())

    # Iterate over each pair of adjacent characters in the sequence.
    for i in range(len(seq) - 1):
        # Update the counts for each pair of bases.
        Counts[seq[i]][seq[i+1]] += 1

    # Compute the conditional probabilities based on the counts.
    Probs = {}
    for b1, c in Counts.items():
        Probs[b1] = {}
        total = sum(c.values())
        for b2 in ['A', 'C', 'G', 'T']:
            Probs[b1][b2] = c[b2] / total

    return Probs


def dna_bp(seq):
    """
    Given a string representing a sequence of DNA bases,
    returns the paired sequence, also as a string,
    where A is always paired with T and C with G.

    >>> dna_bp('ATCGATTGAGCTCTAGCG')
    'TAGCTAACTCGAGATCGC'
    """
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([pairs[b] for b in seq])

if __name__=='__main__':
    doctest.testmod() # This runs the doctests and prints any failures.