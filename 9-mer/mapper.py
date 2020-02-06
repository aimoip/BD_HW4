import sys
for line in sys.stdin:
  line = line.strip()
  for i in range (len(line)-9+1):
    print ('{0}\t{1}'.format(line[i:i+9],1))
