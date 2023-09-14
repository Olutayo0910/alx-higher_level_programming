#!/usr/bin/python3
'''100-append_after.py'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts new_string to a file, after find shows searchstring'''
    with open(filename, "r+") as f:
        lines = f.readlines()
        changed = []
        for line in range(len(lines)):
            changed.append(lines[line])
            if search_string in lines[line]:
                changed.append(new_string)

        f.seek(0)
        f.write("".join(changed))
