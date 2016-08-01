import sys

# encrypts a message using a caesar cypher with a given key
def caesarEncrypt(msg,key):
  msg = msg.lower()
  #get the character code for a, we will use this as a baseline to select characters
  start = ord('a') 
  rVal = ''
  for ch in msg:
    rVal += chr(start + (ord(ch)-start+int(key))%26) if ch.isalpha() else ch
  # print(rVal)
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
				# last = False
				continue
			c = c.lower()
			if total and last:
				freq[last+c] = 1 if not last+c in freq.keys() else freq[last+c]+1
			total+=1
			last = c
	for key in freq.keys():
		freq[key]/=total
	examples = ['ae','qu','po','rs','ek','gn','cc']
	# for pair in examples: print(freq[pair])
	return freq

def pairStringFrq(string):
	freq = {}
	total = 0
	for i in range(len(string)-1):
		if not (string[i].isalpha() and string[i+1].isalpha()):
			continue
		total+=1
		freq[string[i:i+2]] = 1 if not string[i:i+2] in freq.keys() else freq[string[i:i+2]]+1
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

def decryptFile(filename,encryption):
   # open the file and change it to a string
  with open(filename, 'r') as myfile:
    data=myfile.read().replace('\n', '') 
  # get character (pair) frequencies from a large text doc
  nativeFrq = pairFrq('dist/txt/alice.txt')
  # decrypt for each key in the possible keys
  for i in range(1,26): 
    temp = globals()[encryption](data,-i)
    freq = pairStringFrq(temp)
    score = 0
    # decide how to score each translated message
    for key in freq.keys():
      if key in nativeFrq.keys():
        score+=abs(freq[key] - nativeFrq[key])
      else:
        score+=0.1
    # choose a score limit to filter output
    if score < 1:
      print('score: {}'.format(score))
      print('key: {}'.format(i))
      print(temp)
      print('\n')

def stringTo64(string):
	string = '0' + bin(int.from_bytes(string.encode(), 'big'))[2:]
	while (len(string))%24:
		string+='00000000'
	print([for i in range(len(string)/6): string[i]])

# open a file
# encrypt each line with given cypher and key
# append each line to end of file
def writeEncrypt(file1,file2,encryption,key):
	file = open(file1, 'r')
	target = open(file2, 'w')
	target.write('\n')
	for line in file:
		target.write(globals()[encryption](line,key))
		target.write('\n')
	file.close()

if __name__ == '__main__':
	if len(sys.argv)<2:
		print ('Usage: set1.py <function-name> <arg1> <arg2> ...\n')
	else:	
		locals()[sys.argv[1]](*sys.argv[2:])