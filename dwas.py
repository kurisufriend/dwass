#!/usr/bin/env python3
#
# TODO: use map counters to avoid max() + .count
#
import sys
import random
#print(sys.argv, sys.argv.index("--debug")); sys.exit()
#no point in doing anything fancy for 2 flags
if not("--debug" in sys.argv): sys.tracebacklimit = 0
else: sys.argv.remove("--debug")

best = False
if "--best" in sys.argv:
	best = True
	sys.argv.remove("--best")

assert (len(sys.argv) >= 4),"missing (an) argument(s)!\nthe syntax is 'dwas.py <source file> <prompt word> <response size>'\noptional flags:\n--debug: enable tracebacks\n--best: only uses the highest weighted words"

try:
	open(sys.argv[1], "r")
except FileNotFoundError:
	pass

f = open(sys.argv[1], "r")
words = f.read().replace("\n", "").replace(".", " ").replace(",", " ").replace("\"", "").replace("  ", " ").lower().split(" ")

#generated "weighted" wordmap -- append every instance individually
#would be cleaner to make it actually weighted, an array of "word":count maps
wordmap = {}
for i in range(0, len(words) - 1):
	if wordmap.get(words[i]) == None:
		wordmap[words[i]] = []
	wordmap[words[i]].append(words[i + 1])

assert not(wordmap.get(sys.argv[2]) == None), "prompt word not in source file"

print(sys.argv[2], end=" ")
last = sys.argv[2]
for i in range(0, int(sys.argv[3])):
	last = max(set(wordmap[last]), key=wordmap[last].count) if best else random.choice(wordmap[last])
	print(last, end=" ")
print("")
