__author__ = 'loj'

import sys
import getopt















if __name__=="__main__":
    print "hi, dude"
    print sys.argv
    # args = sys.argv.split()
    opts, argvs = getopt.getopt(sys.argv[1:], "abc:d:")
    print opts
    print argvs