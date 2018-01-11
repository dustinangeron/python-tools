#!/usr/bin/python

import re
import random
import string
import sys

if (len(sys.argv) < 2):
        print "Usage: pwgen.py <passsword length> <number of iterations>"
        quit()

for i in range(int(sys.argv[2])):
        myList = []
        for character in range(int(sys.argv[1])):
                ucase = string.uppercase[random.randrange(len(string.uppercase))]
                lcase = string.lowercase[random.randrange(len(string.lowercase))]
                digits = string.digits[random.randrange(len(string.digits))]
                punctuation = string.punctuation[random.randrange(len(string.punctuation))]
                pwAlphabets = [ucase, lcase, digits, punctuation]
                mySelection = pwAlphabets[random.randrange(len(pwAlphabets))]
                myList += mySelection
        print ''.join(myList)
