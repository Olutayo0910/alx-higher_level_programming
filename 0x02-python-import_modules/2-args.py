#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argN = len(sys.argv) - 1
    if argN == 0:
        print("{} arguments.".format(argN))
    elif argN == 1:
        print("{} argument:".format(argN))
    else:
        print("{} arguments:".format(argN))

    if argN >= 1:
        argN = 0

        for arg in sys.argv:
            if argN != 0:
                print("{}: {}".format(argN, arg))
            argN += 1
