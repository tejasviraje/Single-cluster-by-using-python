import sys
for line in sys.stdin:
    line=line.strip()
    words=line.strip()
    for word in words:
        print('%s\t%s' % (word,1))
