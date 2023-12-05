# Day 4: Scratchcards
with open('input') as f:
  lines = f.readlines()

copies = [1 for i in range(0,len(lines))]
print(len(copies))

pt1 = 0
curr_game = 1
for l in lines:
  l = l.strip('\n')
  start = l.find(":") + 1
  l = l[start:]

  temp = l.split('|')
  temp[0] = temp[0].strip()
  temp[1] = temp[1].strip()
  
  winning = temp[0].split(" ")
  curr = temp[1].split(" ")
  winning = [i for i in winning if i != '']
  curr = [i for i in curr if i != ''] 

  res = 0

  for i in curr:
    if i in winning:
      res += 1
  if res == 0:
    ans = 0
  else:
    ans = 2**(res-1)

    # Part 2
    for j in range(0,copies[curr_game-1]):
      for i in range(1,res+1):
        copies[(curr_game-1) + i] += 1

  pt1 += ans
  curr_game += 1

print("PART 1: ", pt1)

pt2 = 0
for i in copies:
  pt2 += i
print("PART 2: ", pt2)
