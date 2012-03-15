#!/usr/bin/env python3
# coding: utf-8

"""Hamming coding

"""

from __future__ import division
from __future__ import print_function
from coding import base

__author__ = 'Arpad Horvath'
# wh for def cl defs ifmain imp fr _ pdb + <Tab>

class Hamming(object):
    """Hamming code
    """
    def __init__(self, n=4):
        super(Hamming, self).__init__()
        self.n = n

    def code_part(self, part):
        """Codes the n-long-part of the message.
        >>> hamming = Hamming(4)
        >>> hamming.code_part("0110")
        '1100110'
        """
        if isinstance(part, base.Bits):
            part = part.message
        else:
            assert isinstance(part, str)
        i = 1
        two_powers = [2**j for j in range(len(part)+1)]
        hamming_code = []
        while part:
            if i in two_powers:
                hamming_code.append(None)
            else:
                hamming_code.append(part[0])
                part = part[1:]
            i += 1

        i = 0
        for tp in two_powers:
            if tp > len(hamming_code):
                break
            number_of_ones = 0
            for j in range(tp, len(hamming_code)):
                if j+1 & tp != 0 and hamming_code[j] == "1":
                    number_of_ones += 1
            parity_bit = 0 if number_of_ones % 2 == 0 else 1
            hamming_code[tp - 1] = str(parity_bit)

        return "".join(hamming_code)

