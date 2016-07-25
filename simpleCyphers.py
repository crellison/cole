import sys

# encrypts a message using a caesar cypher with a given key
def caesarEncrypt(msg,key):
  msg = msg.lower()
  #get the character code for a, we will use this as a baseline to select characters
  start = ord('a') 
  rVal = ''
  for ch in msg:
    rVal += chr(start + (ord(ch)-start+key)%26) if ch.isalpha() else ''
  print(rVal)
  return rVal

# gets character frequencies for a file
def charFrq(filename):
	freq = {}
	total = 0
	with open(filename) as file:
		while True:
			c = file.read(1)
			if not c: 
				break
			total+=1
			freq[c] = 1 if not c in freq.keys() else freq[c]+1
	for key in freq.keys():
		freq[key]/=total
	return freq

# gets character pair frequencies for a file
def pairFrq(filename):
	freq = {}
	total = 0
	with open(filename) as file:
		while True:
			c = file.read(1)
			if not c:
				break
			if not c.isalpha():
				last = False
				continue
			c = c.lower()
			if total and last:
				freq[last+c] = 1 if not last+c in freq.keys() else freq[last+c]+1
			total+=1
			last = c
			print(total)
	for key in freq.keys():
		freq[key]/=total
	return freq

# gets character frequencies for a string
def getStringFrq(string):
	freq = {}
	total = 0
	for char in string:
		total+=1
		freq[char] = 1 if not char in freq.keys() else freq[char]+1
	for key in freq.keys():
		freq[key]/=total
	return freq

if __name__ == '__main__':
	if len(sys.argv)<2:
		print ('Usage: set1.py <function-name> <arg1> <arg2> ...\n')
	else:	
		locals()[sys.argv[1]](*sys.argv[2:])