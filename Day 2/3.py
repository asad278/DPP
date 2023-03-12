import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
	s = input()
	keys = ["2", "22", "222", "3", "33", "333", "4", "44", "444", "5", "55", "555", "6", "66", "666", "7", "77", "777", "7777", "8", "88", "888", "9", "99", "999", "9999"]

	word = ""
	for i in range(len(s)):
		word += '0' if s[i]==' ' else keys[ord(s[i])-ord('A')]
	print(word)
