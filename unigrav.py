#!/usr/bin/python

import sys

G = 6.67384 * 10**-11   # Universal gravitational constant

def f(m1, m2, d):
    return (G * m1 * m2) / d**2

if len(sys.argv) < 4:
    print "Usage: %s m1 m2 d" % sys.argv[0]
    print "Example: %s 5.98e+24 70 6.38e+6" % sys.argv[0]
    
else:
    print f(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
