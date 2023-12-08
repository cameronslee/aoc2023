# Day 5: If You Give A Seed A Fertilizer

with open('input') as f:
  l = f.readlines()

seeds = []
destination = [] # seed to location
data = [[] for i in range(0,7)]

curr = 0
curr_map = 0
while curr < len(l):
  l[curr] = l[curr].strip('\n')
  if "seeds:" in l[curr]:
    start = l[curr].find(':') + 2
    seeds = l[curr][start:].split(" ")
    destination = [0 for i in range(len(seeds))]
    curr += 1

  if len(l[curr]) != 0 and l[curr][0].isalpha():
    curr += 1
    while curr < len(l) and len(l[curr].strip()) != 0:
      temp = l[curr].strip('\n').split(" ")
      data[curr_map].append(temp)
      curr += 1
    curr_map += 1
  curr += 1

# Part 1
def f(x,data):
  for mp in data:
    dest = int(mp[0])
    src = int(mp[1])
    r = int(mp[2])
    if src <= x < src + r:
      return dest + (x-src)
  return x

res = []
for s in seeds:
 s = int(s)
 for d in data:
   s = f(s, d)
 res.append(s)

print("PART 1: ", min(res))

# Part 2
''' get ranges ( Brute Force)
res = []
seeds2 = []
for i in range(0,len(seeds), 2):
  for j in range(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])):
    seeds2.append(j)

res = []
for s in seeds2:
 s = int(s)
 for d in data:
   s = f(s, d)
 res.append(s)
'''
