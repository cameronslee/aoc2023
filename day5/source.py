# Day 5: If You Give A Seed A Fertilizer

with open('input1') as f:
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
    print(seeds)
    destination = [0 for i in range(len(seeds))]
    curr += 1

  if len(l[curr]) != 0 and l[curr][0].isalpha():
    curr += 1
    while curr < len(l) and len(l[curr].strip()) != 0:
      temp = l[curr].strip('\n').split(" ")
      data[curr_map].append(temp)
      curr += 1
    print(curr_map, ":", data[curr_map])
    curr_map += 1
  curr += 1

for i in range(0, len(seeds)): #FIXME
  for mp in data[0]:
    print("log", mp)
    dest = int(mp[0])
    src = int(mp[1])
    r = int(mp[2])


    if int(seeds[i]) in range(src,src+r):
      # range [50, 98) 
      # example:60
      #  yes -> 99 - 98 + dest
      # 52 = (50(src)- 48(r)) + 50(src)

      destination[i] = dest + (int(seeds[i]) - src)
    else:
      destination[i] = int(seeds[i])




for i in range(1,len(data)):
  for mp in data[i]:
    dest = mp[0]
    src = mp[1]
    range = mp[2]

print(seeds)
print(destination)
