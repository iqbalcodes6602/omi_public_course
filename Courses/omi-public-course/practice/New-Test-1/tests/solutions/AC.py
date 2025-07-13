#!/usr/bin/python

from __future__ import print_function

def _main():
    A, B = (int(x) for x in raw_input().strip().split())
    print(A + B)

if __name__ == '__main__':
    _main()
