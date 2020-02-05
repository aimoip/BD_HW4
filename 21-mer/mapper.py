import sys
for line in sys.stdin:
  line = line.strip()
  for i in range (len(line)-21):
    print ('{0}\t{1}'.format(line[i:i+21],1))