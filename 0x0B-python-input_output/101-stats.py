#!/usr/bin/python3
"""script that Reads from standard input and computes metrics"""


if __name__ == "__main__":
    import sys

    stdin = sys.stdin

    cn = 0
    size = 0
    v = ['200', '301', '400', '401', '403', '404', '405', '500']
    st = {}

    try:
        for line in stdin:
            if cn == 10:
                print("File size: {}".format(size))
                for i in sorted(st):
                    print("{}: {}".format(i, st[i]))
                cn = 1
            else:
                cn = cn + 1

            line = line.split()

            try:
                size = size + int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in v:
                    if st.get(line[-2], -1) == -1:
                        st[line[-2]] = 1
                    else:
                        st[line[-2]] = st[line[-2]] + 1
            except IndexError:
                pass

        print("File size: {}".format(size))
        for i in sorted(st):
            print("{}: {}".format(i, st[i]))

    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for i in sorted(st):
            print("{}: {}".format(i, st[i]))
        raise
