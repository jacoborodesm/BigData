#!/usr/bin/python3
import sys

for line in sys.stdin:
    name, *marks = line.split()
    
    for mark in marks:
        print(f'{name}\t{mark}')
