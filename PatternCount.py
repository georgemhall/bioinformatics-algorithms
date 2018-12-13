import sys, argparse

def PatternCount(data, pattern):
    count = 0
    for i in range(len(data)):
        if data[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

if __name__ == '__main__':
    argp = argparse.ArgumentParser(description=__doc__)
    argp.add_argument('-d', '--dataset', metavar='DATASET', default='', help='dataset input')
    argp.add_argument('-p', '--pattern', metavar='PATTERN', default='', help='pattern to match against dataset')
    args = argp.parse_args()
    print(PatternCount(args.dataset, args.pattern))
