#!/usr/bin/python
import sys

def main(args):
    if len(args) < 2:
            print "Usage: python count_CC.py tag_stream_file"
            return 1
    tag_fname = args[1]
    f = open(tag_fname, 'r')
    i = 1 # document counter
	j = 0 # word counter (per document)
    count = 0 # count of CCs in each document
    for line in f:
        if set(list(line.strip())) == set(['~']):
			if i >= 1:
				print count*1.0/j
				count = 0
            i += 1
			j = 0
        else:
            ls = line.split(' ')
            last = ''
            for wd in ls:
				j += 1
                curr = wd
                if curr==last and curr=='CC':
                    count += 1
                last = curr
	return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
