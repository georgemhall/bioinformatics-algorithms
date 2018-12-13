import sys, argparse

def CountBases(data):
    adenine = 0
    cytosine = 0
    guanine = 0
    thymine = 0
    for i in data:
        if i == 'A':
            adenine = adenine + 1
        if i == 'C':
            cytosine = cytosine + 1
        if i == 'G':
            guanine = guanine + 1
        if i == 'T':
            thymine = thymine + 1
    return "%s %s %s %s" % (adenine, cytosine, guanine, thymine)

if __name__ == '__main__':
    argp = argparse.ArgumentParser(description=__doc__)
    argp.add_argument('-d', '--dataset', metavar='DATASET', default='', help='dataset input')
    args = argp.parse_args()
    print(CountBases(args.dataset))
