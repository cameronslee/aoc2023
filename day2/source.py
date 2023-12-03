# Day 2: Cube Conundrum

with open('input.txt') as f:
  lines = f.readlines()

curr_id = 1
res = 0
res2 = 0

for l in lines:
  score = 0
  min_red = 1
  min_green = 1
  min_blue = 1

  l = l.strip('\n')
  
  start = l.find(":") + 2

  l = l[start:]
 
  games = l.split(";")

  for g in games:
    colors = g.split("', ") 

    for c in colors:
      c = c.strip()

      temp = c.split(',')
      for t in temp:
        pair = t.split()
        print(pair)

        if pair[1] == 'red':
          if int(pair[0]) > min_red:
            min_red = int(pair[0])
          if int(pair[0]) > 12:
            score = -1

        if pair[1] == 'green':
          if int(pair[0]) > min_green:
            min_green = int(pair[0])
          if int(pair[0]) > 13:
            score = -1

        if pair[1] == 'blue':
          if int(pair[0]) > min_blue:
            min_blue = int(pair[0])
          if int(pair[0]) > 14:
            score = -1
  
  cube_power = min_red * min_green * min_blue
  res2 += cube_power

  if score == 0:
    res += curr_id

  curr_id += 1

print("Part 1: ", res)
print("Part 2: ", res2)
