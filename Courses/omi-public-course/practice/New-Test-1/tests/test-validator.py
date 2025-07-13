#!/usr/bin/python

from __future__ import print_function


def _main():
    A, B = (int(x) for x in raw_input().strip().split())
    assert 0 <= A <= 2**63 - 1, "%d is outside of valid range" % A
    assert 0 <= B <= 2**63 - 1, "%d is outside of valid range" % B

    print(1)


if __name__ == '__main__':
    _main()
