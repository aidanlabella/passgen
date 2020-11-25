#!/usr/bin/env python

# Simple password generator for db passwords and such
# Author: Aidan LaBella - apl1341@rit.edu

import string
import sys

from random import *

def main(argv):
    passlen = int(argv[1])

    if (passlen < 8):
        print("Password length is too short!", file = sys.stderr)
        sys.exit(1)
    
    acc_punc = "#@!?%&"
    charset = string.ascii_letters + string.digits + acc_punc

    out = ""
    for i in range(passlen):
        out = out + choice(charset)

    print(out)

if __name__ == "__main__":
    main(sys.argv)
