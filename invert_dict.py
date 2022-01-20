"""
Read the documentation ofthe dictionary method setdefault and use it to write a more
concise version of invert_dict.
"""

def invert_dict_og(d):
    
    inverse = dict()
    for key in d:
        val = d[key]

        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    
    return inverse


def invert_dict(d: dict):

    inverse = dict()

    for key in d:

        val = d[key]
        inverse.setdefault(val, []).append(key)
    
    return inverse


if __name__ == '__main__':

    d = dict(a=1, b=2, c=3, z=1)

    inverse = invert_dict(d)

    for val in inverse:
        keys = inverse[val]
        print(val, keys)
        